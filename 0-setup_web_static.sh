#!/usr/bin/env bash
# this bash script sets up the web server for deployment of web_static

#-- install nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTPS'

#-- creating folders
sudo mkdir /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/releases/test/ /data/web_static/shared/

#-- HTML page with content
echo -e '<html>\n<body>\n<h1>Welcome to my page!</h1>\n<p>currently building vodinaefem.tech</p>\n</body>\n</html>' > /data/web_static/releases/test/index.html

#-- create symbolic link (check if exists and deletes to recreate)
if [ -d "/data/web_static/current" ];
then
    sudo rm -rf /data/web_static/current;
fi;
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#-- change ownership of /data/ folder
sudo chown -hR ubuntu:ubuntu /data/

#-- update nginx configuration
sudo chown 755 /etc/nginx/sites-available/default
sudo sed -i '/server_name _/a\		location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

sudo service nginx restart
