# Install kibana 4.4
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add -

# Add the kibana repo to the list
echo "deb http://packages.elastic.co/kibana/4.4/debian stable main" | tee -a /etc/apt/sources.list

# Update and install the cabin
apt-get update && apt-get install kibana

# Add the kibana to startup service
update-rc.d kibana defaults 95 10

# Start the kibana service by running below command
service kibana start

