from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# mysql configurations

app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin123'
app.config['MYSQL_DATABASE_DB'] = 'covid19'
app.config['MYSQL_DATABASE_HOST'] = 'demo-database.ckjrhaypvifd.us-east-1.rds.amazonaws.com'
mysql.init_app(app)
