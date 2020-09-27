import os
import json
import requests
from datetime import datetime
from pytz import timezone

DeployURL="http://35.225.237.40/trigger?dag_id=Git_Deployment_In_Production"

csr_pubsub_file=os.path.join(os.path.dirname(__file__),'../schema/csr_pubsub.json')

with open(csr_pubsub_file) as csr_pubsub_json:
    csr_pubsub_data=json.load(csr_pubsub_json)
    GCPProject=csr_pubsub_data['name'].split('/')[1]
    CSR=csr_pubsub_data['name'].split('/')[3]
    MergeDateUTC=datetime.strptime(csr_pubsub_data['eventTime'], '%Y-%m-%dT%H:%M:%S.%f%z')
    MergeDate=MergeDateUTC.astimezone(timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S %Z%z")
    CommitID=csr_pubsub_data['refUpdateEvent']['refUpdates']["refs/heads/master"]['newId']
    Author=csr_pubsub_data['refUpdateEvent']['email']

csr_msteams_file=os.path.join(os.path.dirname(__file__),'../schema/csr_msteams_template.json')

with open(csr_msteams_file) as csr_msteams_json:
    csr_msteams_data=csr_msteams_json.read()
    msteams_data= csr_msteams_data.replace("<GCPProject>",GCPProject)\
                                                .replace("<CSR>",CSR)\
                                                    .replace("<MergeDate>",MergeDate)\
                                                        .replace("<CommitID>",CommitID)\
                                                            .replace("<Author>",Author)\
                                                                .replace("<DeployURL>",DeployURL)

webhook_url="https://outlook.office.com/webhook/f9b88694-aede-4ef1-9a34-25f17836b709@27e4c168-0323-4463-acad-7e124b566726/IncomingWebhook/481da1e377e24e5b8216e18b8f3296c1/0a244876-c3c5-4ff9-bd20-2414764ab9dc"
post_data=requests.post(webhook_url,data=msteams_data)






