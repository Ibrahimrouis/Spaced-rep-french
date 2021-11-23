import smtplib
from email.message import EmailMessage
from datetime import date, timedelta
from password import password


def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    logs = pickle.load(open('planning.pkl', 'rb'))
    today=date.today()
    result=''
    for key,value in logs.items():
        for k,v in logs[key].items():
            if v==today:
                result=result+'\t'+key+'\t: '+k+'\n'
    if result!='':
        msg = EmailMessage()
        msg.set_content('Pages list for today, '+today+' : \n'+result)
        me = 'ibrahim.rouis@yahoo.com'
        you = 'ibrahim.rouis@yahoo.com'
        msg['Subject'] = f'Spaced Rep French'
        msg['From'] = me
        msg['To'] = you
        login, password = 'ibrahim.rouis@yahoo.com',password

        # Send the message via our own SMTP server.
        s = smtplib.SMTP_SSL(host='smtp.mail.yahoo.com')
        # s.set_debuglevel(1)
        s.login(login, password)
        s.sendmail(me, you, msg.as_string())
        s.quit()
