import pymysql

from dbHandel import dbHandle
from contacts import Contacts


class Controller:
    def __init__(self):
        self.dbobject = dbHandle("localhost", "root", "sunnyiam1()X", "lab7")

    def validate_name(self, name):
        status = self.dbobject.is_contact_exist(name)
        if status == True:
            return False
        else:
            return True

    def validate_mobileno(self, mobileno):
        if mobileno[0] != '+':
            return False
        if len(mobileno) != 13:
            return False
        try:
            intmobileno = int(mobileno[1:])
            print(intmobileno)
        except Exception as e:
            return False
        return True

    def register_contact(self, contact):
        self.dbobject.insert_contact(contact)

    def get_contacts(self, userid):
        return self.dbobject.get_contacts(userid)

    def search_contact(self, name):
        return self.dbobject.search_contact(name)

    def validate_email(self, email):
        return self.dbobject.validate_email(email)

    def validate_password(self, password):
        if len(password) >= 8:
            return True
        else:
            return False

    def registeruser(self, user):
        self.dbobject.register_user(user)

    def get_user_id(self, email):
        return self.dbobject.get_user_id(email)

    def matchpassword(self, email, password):
        pswd = self.dbobject.matchpassword(email)
        print("password from data base is: ", pswd[0][0])
        print("Password from form is: ", password)
        if pswd[0][0] == password:
            return True
        else:
            return False

    def delete_contact(self, index):
        self.dbobject.delete_contact(index)


