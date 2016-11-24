
echo; read -p "Enter login for MySQL for root access : " root_login
echo; read -p "Enter password for MySQL for root access : " root_pass
ir_pass='pass'
mysql -u ${root_login} -p${root_pass} -e "CREATE USER 'f2014017'@'localhost' IDENTIFIED BY '${ir_pass}' ; GRANT ALL PRIVILEGES ON *.* TO 'f2014017'@'localhost'; FLUSH PRIVILEGES;"
mysql -u f2014017 -p${ir_pass} -e "CREATE DATABASE IR_assign_14017; USE IR_assign_14017;"
