sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "CREATE DATABASE IF NOT EXISTS base;"
#sudo mysql -uroot -e "SELECT User, Host FROM mysql.user;"
#sudo mysql -uroot -e "SET PASSWORD FOR root@localhost=PASSWORD('');"
#sudo mysql -uroot -e "DROP USER 'django'@'localhost';"
#sudo mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'pass123';"
#sudo mysql -uroot -e "GRANT ALL ON base.* TO 'django'@'localhost';"
#sudo mysql -uroot -e "FLUSH PRIVILEGES;"
#sudo chmod -R 777 .
#sudo mysql -uroot -e "SELECT * FROM base.qa_question order by added_at DESC;"
