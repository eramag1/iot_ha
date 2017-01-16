#
# Author: Espe
#

# Setting up Fiware Repo
sudo cp /vagrant/repos/fiware.repo /etc/yum.repos.d

# Install contextBroker
sudo yum -y install contextBroker

# Change BROKER_DATABASE_HOST
sed -c -i "s/\(BROKER_DATABASE_HOST *= *\).*/\1172.28.33.10/" /etc/sysconfig/contextBroker

# Start contextBroker
sudo service contextBroker start

# Start automatically during boot
sudo chkconfig contextBroker on

# Setting up Elastic Filebeat Repo
sudo cp /vagrant/repos/elasticbeat.repo /etc/yum.repos.d

# Install Elastic Filebeat agent
sudo yum -y install filebeat

# Start automatically during boot
sudo chkconfig filebeat on

# Change Filebeat config
sudo cp /vagrant/conf/filebeat.yml /etc/filebeat/

# Restart Filebeat
sudo service filebeat restart
