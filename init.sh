sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
#gunicorn -c /home/box/web/etc/ask.py wsgi --daemon
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart
