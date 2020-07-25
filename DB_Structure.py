#DATABASE created using orm (Object-relational mapping) with PEEWEE
#connected via MySQL Server
#excute ONE TIME ONLY!!! so write it correctly and finished

from peewee import *
import datetime             #used for current date field to set current datetime

db = MySQLDatabase(
        'studio_app_2',                 #Database schema
        user='root',                  #MySQL Username
        password='macrun96',          #MySQL password
        host='localhost',             #MySQL localhost
        port=3306                     #MySQL port
)


#DB Tables
#####Table Columns
#####Meta relate to database schema


class Packages(Model):
    Name = CharField(20, unique=True)
    Price = IntegerField(default=0)
    Banners = IntegerField(default=0)
    Frames = IntegerField(default=0)
    Photos = IntegerField(default=0)
    Albums = IntegerField(default=0)
    Description = TextField(null=True)

    class Meta:
        database = db


class Photographers(Model):
    Name = CharField(45, unique=True)
    Studio = CharField(45, null=True)
    Phone = CharField(15)
    Email = CharField(null=True , unique=True)
    Description = TextField(null=True)    #for photographer equipment

    class Meta:
        database = db


class Employees(Model):
    Name = CharField(40)
    Phone = CharField(15, null=True)
    Email = CharField(null=True , unique=True)
    join_Date = CharField(null=True)
    National_ID = IntegerField(null=True, unique=True)
    Priority = IntegerField(null=True)
    Password = CharField(20)

    class Meta:
        database = db


#################################
##CHOICES for spicfied column
EVENT_TYPE = (
    (1, 'wedding'),
    (2, 'casual'),
    (3, 'Engagement'),
    (4, 'other'),
)
#################################

class Orders(Model):
    Groom_Name = CharField()                                                #SIMPLE TEXT
    Bride_Name = CharField()                                                #SIMPLE TEXT
    Phone_Number = CharField(15)                                              #edit it later to be phone format
    Phone_Number_2 = CharField(15, null=True)                                   #OPTIONAL
    Event_Type = CharField(choices=EVENT_TYPE)                              #(WEDDING, CASUAL, Engagement, OTHER)
    Event_Date = DateField()
    Package = ForeignKeyField(Packages, backref='Package')                  #RELATION WITH PACKAGES
    Price = IntegerField()                                                  #must call the package price
    Down_Payment = IntegerField()                                           #3ARBON
    Remaining_Payment = IntegerField()                                      #operation = Price - Down payment 
    Photographer = ForeignKeyField(Photographers, backref='Photographer')
    Locations = TextField(null=True)                                        #LOCATION IN/OUT MANSOURA
    Comments = TextField(null=True)
    Employee = ForeignKeyField(Employees, backref='Employee')               #EMPLOYEE REGISTERED
    Current_Date = CharField()

    class Meta:
        database = db


ACTION = (
    (1,'login'),
    (2,'logout'),
    (3,'add'),
    (4,'edit'),
    (5,'remove'),
    (6,'import'),
    (7,'export'),
    (8,'print')
)

TABLE = (
    (1,'orders'),
    (2,'photographers'),
    (3,'packages'),
)


class History(Model):
    Username = ForeignKeyField(Employees, backref='History_Username')
    Action = CharField(choices=ACTION)             #CHOICES
    Table = CharField(choices=TABLE)               #CHOICES
    Date_Time = DateTimeField(default=datetime.datetime.now)     #Timestamp

    #Changed_Field = what column did the user interacted with

    class Meta:
        database = db


#connect to database
db.connect()

#create tables
#consider the order in creating tables to excute the forgien keys right

db.create_tables(
    [
        Packages,
        Photographers,
        Employees,
        Orders,
        History
    ]
)
