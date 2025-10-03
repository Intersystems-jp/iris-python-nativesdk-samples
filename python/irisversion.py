import iris

# Open a connection to the server
args = {'hostname':'127.0.0.1', 'port':1972,
    'namespace':'USER', 'username':'_SYSTEM', 'password':'SYS'
}
conn = iris.connect(**args)
# Create an iris object
irispy = iris.createIRIS(conn)
className =  '%SYSTEM.Version'
stringVal = irispy.classMethodString(className,'GetVersion')
print('IRIS Version = ' + stringVal)
