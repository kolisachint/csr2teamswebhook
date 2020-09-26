import json
import os
import pandas as pd
from datetime import datetime
from pytz import timezone

csr_pubsub_file=os.path.join(os.path.dirname(__file__),'../schema/csr_pubsub.json')

with open(csr_pubsub_file) as csr_pubsub_json:
    csr_pubsub_data=json.load(csr_pubsub_json)
    GCPProject=csr_pubsub_data['name'].split('/')[1]
    CSR=csr_pubsub_data['name'].split('/')[3]
    MergeDateUTC=datetime.strptime(csr_pubsub_data['eventTime'], '%Y-%m-%dT%H:%M:%S.%f%z')
    MergeDate=MergeDateUTC.astimezone(timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S %Z%z")
    CommitID=csr_pubsub_data['refUpdateEvent']['refUpdates']["refs/heads/master"]['newId']
    Author=csr_pubsub_data['refUpdateEvent']['email']
    print(MergeDate)
    print(Author)
    print(CommitID)




