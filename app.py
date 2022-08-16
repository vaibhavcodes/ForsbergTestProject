from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

class Database:
    def __init__(self):
        #host = "127.0.0.1"
        #user = "root"
        #password = "root"
        #db = "testdb"
        server = "forsbergserver.database.windows.net"
        username = "vaibhav"
        password = "password23@"
        database = "forsbergDB"
        port = 1433
        driver = '{ODBC Driver 13 for SQL Server}'
        conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=port;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.cursor = conn.cursor()

    def list_products(self, table_name, columns_reqd):
        #query = "select " + columns_reqd + " from " + table_name
        query = "select top 2 " + columns_reqd + " from " + "[dbo]." + table_name
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/trackstat')
def trackstat():
    def db_query():
        db = Database()
        table_name = "trackstata"
        columns = "Sync_Message, Port, TimeStatus, Week, Seconds, C_No"
        products = db.list_products(table_name, columns)
        return products

    res = db_query()
    return render_template("trackstat.html", result=res)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#az webapp config set -g ForsbergRG -n forsbergwebapp --startup-file startup.txt