#Install Logstash

wget https://download.elastic.co/logstash/logstash/packages/debian/logstash_2.2.0-1_all.deb
sudo dpkg -i logstash_2.2.0-1_all.deb

cp /vagrant/conf/logstash.conf /etc/logstash/conf.d/logstash.conf

/opt/logstash/bin/logstash --configtest --config /etc/logstash/conf.d/logstash.conf
sudo service logstash start

sudo update-rc.d logstash defaults 95 10




