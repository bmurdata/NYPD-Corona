import pyodbc 
computer="computer host"
computer="localhost"#input("Enter Local Host for SQLExpress")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+str(computer)+'\SQLEXPRESS;'
                      'Database=twitterScraper;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('SELECT @@version')
for row in cursor:
    print(row)
cursor.execute("SELECT TABLE_NAME FROM twitterScraper.INFORMATION_SCHEMA.TABLES  WHERE TABLE_TYPE = 'BASE TABLE'")

for row in cursor:
    print(row)

