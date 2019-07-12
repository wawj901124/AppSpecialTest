def writeFile(FileName, content):
    FName = open(FileName, 'a')
    FName.write(content)
    FName.close()

def findException(tfile,sstr):
    try:
        lines=open(tfile,'r').readlines()
        flen=len(lines)-1
        acount = 0
        fileException = "%s_Exception" % tfile
        tfileException = "%s.txt" % fileException
        
        writeFile(tfileException,"%s keywords:\n" % fileException)
        for i in range(flen):
            if sstr in lines[i]:
                lineException = '\t%s\n'% lines[i]

                writeFile(tfileException,lineException)
                acount+= 1

        writeFile(tfileException,"%s  frequency:%s" % (fileException,acount))
        print 'Please check Exception keywords in the "%s"\n' % tfileException
    except Exception,e:
        print e


findException("ManualExitMonkeyTest_20170817165837_monkey.log","Exception")
