##
# signature
# https://github.com/leosartaj/signature.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##
import shutil, os

"""
Helper functions for performing tests
"""

def newFile(fName):
    """
    Touch a new file
    """
    with open(fName, 'a'):
        pass

def testArea(obj):
    obj.testArea = os.path.join(obj.dire, 'testArea')
    os.mkdir(obj.testArea)
    obj.unsigned1 = os.path.join(obj.dire, 'testArea/test_unsignedfile1.py')
    newFile(obj.unsigned1)
    obj.signed1 = os.path.join(obj.dire, 'testArea/test_signedfile1.py')
    shutil.copy(obj.signfile, obj.signed1)
    obj.testArea2 = os.path.join(obj.dire, 'testArea/testArea2')
    os.mkdir(obj.testArea2)
    obj.unsigned2 = os.path.join(obj.dire, 'testArea/testArea2/test_unsignedfile2.py')
    newFile(obj.unsigned2)
    obj.signed2 = os.path.join(obj.dire, 'testArea/testArea2/test_signedfile2.py')
    shutil.copy(obj.signfile, obj.signed2)