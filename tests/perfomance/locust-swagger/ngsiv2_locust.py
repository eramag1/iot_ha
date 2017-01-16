from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task
    def get_entities(self):
        self.client.get("/v2/entities", name="/entities")

    @task
    def get_entities_entity_id(self):
        self.client.get("/v2/entities/{0}".format("123"), name="/entities/{entity_id}")

    @task
    def get_entities_entity_id_attrs(self):
        self.client.get("/v2/entities/{0}/attrs".format("123"), name="/entities/{entity_id}/attrs")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 3000
    host = "https://localhost:1026"

