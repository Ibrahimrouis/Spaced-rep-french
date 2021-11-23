import smtplib
from email.message import EmailMessage
from datetime import date, timedelta
from psw import password
import pickle

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    logs = pickle.load(open('./planning.pkl', 'rb'),encoding='latin1')
    today=date.today()
    result=''
    for key,value in logs.items():
        for k,v in logs[key].items():
            if v==today:
                result=result+'\t'+str(key)+'\t: '+str(k)+'\n'
    print(result)
    if result!='':
        msg = EmailMessage()
        msg.set_content('Pages list for today, '+str(today)+' : \n'+result)
        me = 'ibrahim.rouis@yahoo.com'
        you = 'ibrahim.rouis@yahoo.com'
        msg['Subject'] = f'Spaced Rep French'
        msg['From'] = me
        msg['To'] = you
        login, pswd = 'ibrahim.rouis@yahoo.com',password

        # Send the message via our own SMTP server.
        s = smtplib.SMTP_SSL(host='smtp.mail.yahoo.com')
        # s.set_debuglevel(1)
        s.login(login, pswd)
        s.sendmail(me, you, msg.as_string())
        s.quit()
