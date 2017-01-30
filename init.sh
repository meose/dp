sudo pkill -9 python
sudo pkill -9 nginx
sudo pkill -9 gunicorn

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

cd /home/box/web/
gunicorn -w 4 hello:app -b 0.0.0.0:8080
cd ..