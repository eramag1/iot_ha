from flask import Flask
from flask import request, redirect, render_template, url_for
from fiware.orion.ngsiv2_client import NGSIv2Client

from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

import time
from random import randint

app = Flask(__name__)

client = NGSIv2Client()
num_jobs = 10
chunk_size = 1
num_workers = 2


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/list_entities', methods=['GET'])
def list_entities():
    try:
        entity_list = client.get_entities()
        template = "list_entities.html"
    except Exception as ex:
        print("Error {0}".format(ex))
        entity = None
        template = "error.html"
    return render_template(template, entity_list=entity_list)

@app.route('/create_entity', methods=['GET','POST'])
def create_entity():
    if request.method == 'GET':
        return render_template("create_entity.html")

    id = request.form['id']
    temperature = request.form['temperature']
    pressure = request.form['pressure']
    try:
        entity = client.create_entity(id=id, temperature=temperature, pressure=pressure)
        template = "show_entity.html"
    except Exception as ex:
        print("ex".format(ex))
        entity = "ex".format(ex)
        template = "error.html"
    return render_template(template, entity=entity)

@app.route('/show_entity', methods=['GET','POST'])
def show_entity():

    id = request.args.get('id')

    try:
        entity = client.get_entity(id)
        template = "show_entity.html"
    except Exception as ex:
        print("ex".format(ex))
        entity = "ex".format(ex)
        template = "error.html"
    return render_template(template, entity=entity)


@app.route('/update_entity', methods=['GET','POST'])
def update_entity():

    id=request.form['id']
    temperature=request.form['temperature']
    pressure=request.form['pressure']
    try:
        entity = client.set_entity_attrs(id, temperature, pressure)
        template = "entity_updated.html"
    except Exception as ex:
        print("ex".format(ex))
        entity = "ex".format(ex)
        template = "error.html"
    return render_template(template, entity=entity)

@app.route('/delete_entity',methods = ['POST'])
def delete_entity():
    if request.method == 'GET':
        return render_template("delete_entity.html")

    id = request.form['id']
    try:
        template = "entity_deleted.html"
        entity = None
    except Exception as ex:
        print("ex".format(ex))
        entity = "ex".format(ex)
        template = "error.html"
    return render_template(template, entity=entity)

def multi_update_account(arg):
    """
    :param arg: tuple data to convert in arguments
    :param kwarg: dict data to convert in arguments
    :return: tuples (account_id, result update)
    """

    ip = "1.0.0." + str(randint(0, 1))
    client.set_source_ip(ip)
    return arg[0], ip, client.set_entity_attrs(*arg)

def get_entities_as_job_args(num_jobs, chunk):
    """
    :param num_jobs: Number of update jobs
    :param chunk: Entities used in update jobs
    :return: tuples (id, temperature, pressure)
    """
    job_args = []
    while num_jobs > 0:
        for i in range(chunk):
            tupla = (str(i+1), "40", "100")
            job_args.append(tupla)
        num_jobs -= chunk
    return job_args

@app.route('/send_bulk_request', methods=['GET'])
def send_bulk_request():
        #pool = Pool(processes=num_workers)
        pool = ThreadPool(processes=num_workers)
        job_args = get_entities_as_job_args(num_jobs, chunk_size)
        start = time.time()
        result = pool.map(multi_update_account, job_args) # job_args = [(1, 40, 100), (2, 40, 100) ...
        # result [(id,ip,update_result) ,()...,()]
        end = time.time()
        print
        "Updated " + str(num_jobs) + \
        " Accounts (" + str(num_workers) + " process workers) TIME: " + str(end - start)

        print
        "RESULT", result

        return render_template('bulk_updated.html', result=result)


if __name__ == '__main__':
    app.run()
