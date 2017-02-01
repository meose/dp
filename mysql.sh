sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE IF NOT EXISTS base;"
#sudo mysql -uroot -e "SELECT User, Host FROM mysql.user;"
#sudo mysql -uroot -e "SET PASSWORD FOR root@localhost=PASSWORD('');"
sudo mysql -uroot -e "DROP USER 'sven'@'localhost';"
sudo mysql -uroot -e "CREATE USER 'sven'@'localhost' IDENTIFIED BY 'qrs797';"
sudo mysql -uroot -e "GRANT ALL ON base.* TO 'sven'@'localhost';"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"

#sudo mysql -uroot -e "SELECT * FROM base.qa_question order by added_at DESC;"
