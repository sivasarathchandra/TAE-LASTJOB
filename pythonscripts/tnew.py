import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
import codecs
import testnew
import csv
import pprint

adnearObj = testnew.Adnear("pramod@adnear.com", "ka09ez9177")
print("entering the all camapigns")
adnearObj.getAllCampaigns()
print("entering all reports")
adnearObj.getAllReports()
#adnearObj.getReport('5a2f38ae7e4fb76114000041')
print("all campaign details")
adnearObj.getAllCampaignDetails()
#adnearObj.getCampaignDetails('5a2f38ae7e4fb76114000041')
with codecs.open("Daily_Report.csv", "w", "utf-8") as output:
	writer = csv.writer(output)
	writer.writerow(['CampaignID', 'Campaign_Name', 'Country', 'Yesterday_Impressions', 'Yesterday_Clicks', 'CTR','ACcount Name','Daily_Cap', 'Totoal_Goal', 'Start_Date', 'End_date'])
	for k, v in adnearObj.campaignDict.items():
		tempDict = {}
		tempDict["CampaignID"] = k
		tempDict.update(v)
		writer.writerow(tempDict.values())
		print(tempDict)
server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
server.ehlo()
server.starttls()
gmail_user = 'shiva@near.co'
gmail_pwd = 'hitman22'
server.login(gmail_user, gmail_pwd)
msg = MIMEMultipart()
to = ['shiva@near.co'] #Multiple Email Address
Subject = "Daily Report"
 
# Message can be a simple text message or HTML
TEXT = "Hello everyone,\n"
TEXT = TEXT + "\n"
TEXT = TEXT + "Hope you are doing fine today. This report is said to run from my python script\n"
TEXT = TEXT + "Please review the attached report and let me know if it looks fine.\n"
TEXT = TEXT + "Please let me know if any changes are required to it.\n"
TEXT = TEXT + "Regards,\n"
TEXT = TEXT + "Shiva Sarath Chandra"
 
		
msg['From'] = 'shiva@near.co'
msg['To'] = ", ".join(to) #Join them as we have multiple recipients
msg['Subject'] = Subject
 msg.attach(MIMEText(TEXT))
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('Daily_Report.csv', 'rb').read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename('test_report.csv'))
msg.attach(part)	
server.sendmail(gmail_user, to, msg.as_string())
print("Email Sent to the Id's Mentioned")
server.close()
