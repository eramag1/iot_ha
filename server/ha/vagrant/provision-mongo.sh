#
# Author: Espe
#

# Setting up EPEL Repo
#wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
#sudo rpm -ivh epel-release-6-8.noarch.rpm

# Setting up EPEL Repo
sudo cp /vagrant/repos/epel.repo /etc/yum.repos.d

# Install required packages
sudo yum -y install mongodb-server mongodb-org

# Change bind_ip paramfrom 127.0.0.1 to 0.0.0.0
sed -c -i "s/\(bind_ip *= *\).*/\10.0.0.0/" /etc/mongodb.conf

# Start MongoDB
sudo service mongod start
sudo chkconfig mongod on