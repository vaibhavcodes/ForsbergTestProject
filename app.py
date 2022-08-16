from flask import Flask, render_template
import pymysql

app = Flask(__name__)

class Database:
    def __init__(self):
        #host = "127.0.0.1"
        #user = "root"
        #password = "root"
        #db = "testdb"
        host = "forsbergserver.database.windows.net"
        user = "vaibhav"
        password = "password23@"
        db = "forsbergDB"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def list_products(self, table_name, columns_reqd):
        #query = "select " + columns_reqd + " from " + table_name
        query = "select top 5 " + columns_reqd + " from " + "forsbergDB.[dbo]." + table_name
        self.cur.execute(query)
        result = self.cur.fetchall()
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
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
