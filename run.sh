python manage.py migrate
python manage.py collectstatic --noinput

/usr/sbin/nginx

rm /run/gift_shop.sock
rm /run/gift_shop.sock.lock

exec gunicorn --workers 5 --max-requests 10 --threads 5 wsgi:application -b unix:///run/gift_shop.sock
