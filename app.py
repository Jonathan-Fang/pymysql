import pymysql

def mysqlconnect():
    # connect to the MySQL database
    connect = pymysql.connect(
        host='localhost',
        user='root',
        password='Tgbmysqlr!',
        db='sept_database',
    )

    cur = connect.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    print(output) #debug

    with connect:
        with connect.cursor() as cursor:
            # read all records from both tables
            sql = 'SELECT * FROM sept_table_alpha'
            cursor.execute(sql)
            result = cursor.fetchall()
            desc = 'selected from sept_table_alpha'
            print(result)
            print(desc)

            sql = 'SELECT * FROM sept_table_beta'
            cursor.execute(sql)
            result = cursor.fetchall()
            desc = 'selected from sept_table_beta'
            print(result)
            print(desc)
        
        with connect.cursor() as cursor:
            # add a row
            sql = """INSERT INTO sept_table_alpha(username, password, element, age) VALUES('buriedintheearth', 'help345', 'earth', 18)"""
            cursor.execute(sql)
            sql = 'SELECT * FROM sept_table_alpha'
            cursor.execute(sql)
            result = cursor.fetchall()
            desc = 'added a row'
            print(result)
            print(desc)

            # delete a row
            sql = """DELETE FROM sept_table_alpha WHERE sept_table_alpha.PrimaryID = 1"""
            cursor.execute(sql)
            sql = 'SELECT * FROM sept_table_alpha'
            cursor.execute(sql)
            result = cursor.fetchall()
            desc = 'removed a row'
            print(result)
            print(desc)

    # close the connection
    # connect.close()

# Driver code
if __name__ == "__main__" :
    mysqlconnect()