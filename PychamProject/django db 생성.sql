create database django_db default character set utf8mb4;

create user 'django'@'%' identified by '1234'; -- any host
create user 'django'@'localhost' identified by '1234'; -- local host

grant all privileges on django_db.* to 'django'@'%';
grant all privileges on django_db.* to 'django'@'localhost';

flush privileges;