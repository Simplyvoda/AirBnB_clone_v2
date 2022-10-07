#!/usr/bin/env bash
# this bash script sets up the web server for deployment of web_static

#-- install nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

#-- creating folders
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

#-- HTML page with content
sudo echo 'Welcome to vodinaefem.tech!' | sudo tee /data/web_static/releases/test/index.html

#-- create symbolic link (check if exists and deletes to recreate)
if [ -d "/data/web_static/current" ];
then
    sudo rm -rf /data/web_static/current;
fi;
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#-- change ownership of /data/ folder
sudo chown -hR ubuntu:ubuntu /data/

#-- update nginx configuration
sudo sed -i '47i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx start
