"""

Name: Gisel Rodriguez
Date: 10/01/2022
Assignment: Module 4: Basic Flask Website
Due Date: 10/05/2022
About this project: reates a table setup for newBidder.py
Assumptions:The program will compile with 0 error and will produce the correct output
Sources : Dr.Works Module 6
All work below was performed by Gisel Rodriguez

"""
import sqlite3
import  string,base64
import Encryption

'Encryption.py'
# create a new database
conn = sqlite3.connect('NewDb.db')

# create a cursor to execute queries
cur = conn.cursor()

# drop table from database
try:
    conn.execute('''Drop table bidder''')
    # save changes
    conn.commit()
    print('Bidder table dropped')
except:
    print('Bidder table did not exist')


# commit and save changes to database
conn.commit()

# create table in database
cur.execute('''CREATE TABLE BIDDER(
BidderId INTEGER PRIMARY KEY NOT NULL,
BidderName TEXT NOT NULL,
PhoneNumber TEXT NOT NULL,
PrequalifiedUpperLimit TEXT NOT NULL,
AppRoleLevel TEXT NOT NULL,
LoginPassword TEXT NOT NULL);
''')

# commit and save changes to database
conn.commit()
print("Bidder table dropped.")


print('Bidder Table created.')
# Insert multiple values into table at once
nm = str(Encryption.cipher.encrypt(b'James Bond').decode("utf-8"))
num = str(Encryption.cipher.encrypt(b'111-222-0007').decode("utf-8"))
Pwd = str(Encryption.cipher.encrypt(b'test123').decode("utf-8"))
cur.execute("Insert Into BIDDER (BidderName,PhoneNumber,PrequalifiedUpperLimit,AppRoleLevel,LoginPassword) Values (?, ?, ?,3,?)",(nm, num, 300000,Pwd))
conn.commit()

nm = str(Encryption.cipher.encrypt(b'Tina Whitefield').decode("utf-8"))
num = str(Encryption.cipher.encrypt(b'333-444-5555').decode("utf-8"))
Pwd = str(Encryption.cipher.encrypt(b'test456').decode("utf-8"))
cur.execute("Insert Into BIDDER (BidderName,PhoneNumber,PrequalifiedUpperLimit,AppRoleLevel,LoginPassword) Values (?, ?, ?,2,?)",(nm, num, 2500000,Pwd))
conn.commit()

nm = str(Encryption.cipher.encrypt(b'Tim Jones').decode("utf-8"))
num = str(Encryption.cipher.encrypt(b'777-888-9999').decode("utf-8"))
Pwd = str(Encryption.cipher.encrypt(b'test789').decode("utf-8"))
cur.execute("Insert Into BIDDER (BidderName,PhoneNumber,PrequalifiedUpperLimit,AppRoleLevel,LoginPassword) Values (?, ?, ?,1,?)",(nm, num, 125000,Pwd))
conn.commit()

nm = str(Encryption.cipher.encrypt(b'Jenny Smith').decode("utf-8"))
num = str(Encryption.cipher.encrypt(b'3333-222-1111').decode("utf-8"))
Pwd = str(Encryption.cipher.encrypt(b'test321').decode("utf-8"))
cur.execute("Insert Into BIDDER (BidderName,PhoneNumber,PrequalifiedUpperLimit,AppRoleLevel,LoginPassword) Values (?, ?, ?,2,?)",(nm, num, 10000,Pwd))
conn.commit()

nm = str(Encryption.cipher.encrypt(b'Mike Hatfield').decode("utf-8"))
num = str(Encryption.cipher.encrypt(b'555-444-3333').decode("utf-8"))
Pwd = str(Encryption.cipher.encrypt(b'test654').decode("utf-8"))
cur.execute("Insert Into BIDDER (BidderName,PhoneNumber,PrequalifiedUpperLimit,AppRoleLevel,LoginPassword) Values (?, ?, ?,1,?)",(nm, num, 2500,Pwd))
conn.commit()
"""
cur.execute('''Insert Into BIDDER ('BidderName','PhoneNumber','PrequalifiedUpperLimit','AppRoleLevel','LoginPassword') 
Values ('James Bond', '111-222-0007', 300000, 3, Pwd);''')
conn.commit()
cur.execute('''Insert Into BIDDER ('BidderName','PhoneNumber','PrequalifiedUpperLimit','AppRoleLevel','LoginPassword') 
Values  ( 'Tina Whitefield', '333-444-5555', 2500000, 2, 'test456');''')
conn.commit()
cur.execute('''Insert Into BIDDER ('BidderName','PhoneNumber','PrequalifiedUpperLimit','AppRoleLevel','LoginPassword') 
Values ('Tim Jones', '777-888-9999', 125000, 1, 'test789');''')
conn.commit()
cur.execute('''Insert Into BIDDER ('BidderName','PhoneNumber','PrequalifiedUpperLimit','AppRoleLevel','LoginPassword') 
Values ('Jenny Smith', '3333-222-1111', 10000, 2, 'test321');''')
conn.commit()
cur.execute('''Insert Into BIDDER ('BidderName','PhoneNumber','PrequalifiedUpperLimit','AppRoleLevel','LoginPassword') 
Values  ( 'Mike Hatfield', '555-444-3333', 2500, 1, 'test654');''')
conn.commit()
"""
""""
 Use Cursor results from a Select statement to display the information
 from all the rows in the table
"""


# iterate over the rows
for row in cur.execute('SELECT * FROM BIDDER;'):
    print(row)


# close database connection
conn.close()
print('Connection closed.')


