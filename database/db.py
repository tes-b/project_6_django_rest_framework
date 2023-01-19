import pymysql

'''if you close db by using method .close(), have to reconnect db

dont you, then error occurs -> InterfaceError: (0, ""). please, connect and close'''


hostname = 'localhost'
username = 'root'
userpassword = 'root'
enc_type = 'utf8mb4'

conn_db = pymysql.connect(host = hostname,
                          user = username, 
                          password = userpassword, 
                          charset = enc_type)

cur = conn_db.cursor()

create_db_query = '''
create database bbs
'''

create_user_table_query = '''
create table BBS.Users(
    member_number int not null auto_increment primary key,
    id varchar(100) not null unique,
    password varchar(100) not null,
    name varchar(100) not null,
    age integer,
    gender char(10),
    email varchar(50),
    registration_date date,
    latest_login date
)
'''

create_board_table_query = '''
create table BBS.Board(
    post_number int not null auto_increment primary key,
    id varchar(100),
    contents varchar(1000),
    foreign key (id) references BBS.Users (id) on update cascade
)
'''

cur.execute(create_db_query)
cur.execute(create_user_table_query)
cur.execute(create_board_table_query)


conn_db.commit()
conn_db.close()