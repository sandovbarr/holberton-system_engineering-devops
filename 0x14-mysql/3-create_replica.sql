CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
