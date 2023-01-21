#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Hello from web_static" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/root \/var\/www\/html;/a \\tlocation /web_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
nginx -s reload
