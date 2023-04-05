# install and configure Nginx server

exec { 'nginx configuration':
    provider => shell,
    command  => 'sudo apt-get update; sudo apt-get install -y nginx; sudo echo "Hello World!" | sudo tee /var/www/html/index.html;
	     sudo sed -i "/server_name _;/a location /redirect_me {\\n\\treturn 301 https://test.com;\\n\\t}" /etc/nginx/sites-available/default; 
	     sudo service nginx restart'
}
