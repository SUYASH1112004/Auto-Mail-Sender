'''Creating the log file which contains the processess running on the 
Computer and the auto mail sender will send the mail ..'''

import os
import psutil
import time
import urllib.request as urllib2 
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def Is_connected():
    try:
        urllib2.urlopen('https://www.google.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False
    
def Mailsender(filename,time):
    try:
        fromaddr="suyashpatil1817@gmail.com"
        toaddr="sakshipatil2302@gmail.com"
        msg=MIMEMultipart()
        msg['From']=fromaddr
        msg['To']=toaddr
        body="""
        Hello %s.
        Please find the  attached document which conatin
        log of running process.
        Log file is created at: %s

        This is auto Generated Mail.

        Thanks & Regards,
        Suyash Patil
        """%(toaddr,time)
        
        Subject="""Procees Log Generated at : %s"""%(time)

        msg['Subject']=Subject
        msg.attach(MIMEText(body,'plain'))
        attachment=open(filename,'rb')
        p=MIMEBase('application','octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',"attachment; filename=%s"%filename)
        msg.attach(p)
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(fromaddr,"oqss trtc zlqg mlbl")
        text=msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        s.quit()

        print("Log File Successfully Sent Through Mail")
    except Exception as E:
        print("Unable to send mail",E)

def ProcessLog(log_dir="Process_File"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir) 
        except:
            pass
    
    seperator= "-" * 80
    log_path=os.path.join(log_dir,"Logfile.log")
    f=open(log_path,'w')
    f.write(seperator+"\n")
    f.write("Process Logger :"+time.ctime()+"\n")
    f.write(seperator+"\n")
    # f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            vms=proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for elem in listprocess:
        f.write("%s\n"%elem)

    print("Log file is being created successfully.")

    connected=Is_connected()

    if connected:
        starttime=time.time()
        Mailsender(log_path,time.ctime())
        endtime=time.time()

        print("Took %s seconds to send mail "%(endtime-starttime))
    else:
        print("There is no internet connection ")


def main():
    print("Application name :"+ argv[0])

    if(len(argv)!=2):
        print("Error:Invalid Input ")
    
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This Script is used to llog record of running process")
        exit()

    if(argv[1]=="-u"or argv[1]=="-U"):
        print("Usage : ApplicationName Absolutepath_directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while(True):
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error : Invalid Data type of input")

    except Exception as E:
        print("Error:Invalid Input ",E)

if __name__=="__main__":
    main()





        
        

