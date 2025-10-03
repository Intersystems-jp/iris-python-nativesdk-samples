import iris

# Open a connection to the server
args = {'hostname':'127.0.0.1', 'port':1972,
    'namespace':'USER', 'username':'_SYSTEM', 'password':'SYS'
}
conn = iris.connect(**args)
# Create an iris object
irispy = iris.createIRIS(conn)

className =  'Samples.ADBK'
irispy.classMethodString(className,'Init')

adbkrecord = irispy.getIRISList('Samples.ADBKD',1)
name = adbkrecord.get(2)
telno = adbkrecord.get(4)
prefecture = adbkrecord.get(5)
zipcode = adbkrecord.get(3)
print('Name = ' + name)
print('Telno = ' + telno)
print('Prefecture = ' + prefecture)
print('Zipcode = ' + str(zipcode))
conn.close()
