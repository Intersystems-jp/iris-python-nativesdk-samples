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

adbk =  irispy.classMethodObject(className,"%OpenId",1)
name = adbk.get("Name")
telno = adbk.get("Telno")
prefecture = adbk.get("Prefecture")
zipcode = adbk.get("Zipcode")
print('Name = ' + name)
print('Telno = ' + telno)
print('Prefecture = ' + prefecture)
print('Zipcode = ' + str(zipcode))
conn.close()
