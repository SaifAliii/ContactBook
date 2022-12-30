import pymysql
class dbHandle:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def is_contact_exist(self, name):
        mydb = None
        mycursor = None
        status = True
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "select * from contacts where name = %s"
            args = (name)
            mycursor.execute(query, args)
            records = mycursor.fetchall()
            print("The length of records fetched from DB: ")
            print(len(records))
            if len(records) > 0:
                status = True
            else:
                status = False
        except Exception as e:
            print(str(e))
        finally:
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None
            return status

    def insert_contact(self, contact):
        mydb = None
        mycursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mycursor = mydb.cursor();
            query = "insert into contacts (name, mobileno, city, profession, userid) values (%s, %s, %s, %s, %s)"
            args = (contact.name, contact.mobileno, contact.city, contact.profession, contact.userid)
            mycursor.execute(query, args)
        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None

    def get_contacts(self, userid):
        mydb = None
        mycursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "select * from contacts where userid=%s"
            args = (userid)
            mycursor.execute(query, args)
            records = mycursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None
            return records

    def search_contact(self, name):
        mydb = None
        mycursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "select * from contacts where name=%s"
            args = (name)
            mycursor.execute(query, args)
            result = mycursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None
            return result

    def validate_email(self, email):
        mydb = None
        mycursor = None
        status = False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "Select * from users where email = %s"
            args = (email)
            mycursor.execute(query, args)
            if len(mycursor.fetchall()) != 0:
                status = True
        except Exception as e:
            print(str(e))
        finally:
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None
            return status

    def register_user(self, user):
        mydb = None
        mycursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "insert into users (email, password) values (%s, %s)"
            args = (user.email, user.password)
            mycursor.execute(query, args)
        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydb != None:
                mydb = None
            if mycursor != None:
                mycursor = None

    def get_user_id(self, email):
        mydb = None
        mycursor = None
        user_id = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "select userid from users where email = %s"
            args = (email)
            mycursor.execute(query, args)
            user_id = mycursor.fetchall()
            user_id = user_id[0][0]
            print("user id from db is: ", user_id)

        except Exception as e:
            print(str(e))
        finally:
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None
            return user_id

    def matchpassword(self, email):
        mydb = None
        mycursor = None
        password = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "select password from users where email = %s"
            args = (email)
            mycursor.execute(query, args)
            password = mycursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None
            return password

    def delete_contact(self, index):
        mydb = None
        mycursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "delete from contacts where contactid = %s"
            args = (index)
            mycursor.execute(query, args)
        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None