import iris
import os
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
className =  '%SYSTEM.OBJ'
dir = os.getcwd()
# 実行ディレクトリ名に/pythonが一個だけ含まれる前提
fileName = dir.split('/python')[0] + '/src/Samples/ADBK.cls'
status = irispy.classMethodObject(className,'Import',fileName,'ck')
# error = irispy.classMethodString('%SYSTEM.Status','GetOneErrorText',status)
# print('Error = ' + error)
