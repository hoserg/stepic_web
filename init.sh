sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE dbstep CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -uroot -e "CREATE USER 'hoserg'@'localhost' IDENTIFIED BY 'hoserg';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'hoserg'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart

python /home/box/web/ask/manage.py syncdb
