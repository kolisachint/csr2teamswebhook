What is the purpose of this Channel ?
As part of DevOps activities, we do code review and deploy code to production environment for different applications.
This channel is created for quick glance at deployment notifications. 
 
Team can do following activities using this channel ->
Monitor Code deployments of multiple projects.
Code Review of code changes
Deploy code to production environment.
Monitor production batch status
Monitor production job failures
Discuss and assign support activities to the team members
How to add your project git changes to this channel?
gcloud source repos update AdobeCampaignInterimLayer    --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
gcloud source repos update AdobeCampaignMart            --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
gcloud source repos update AdobeCampaignMart_VM_Config  --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
gcloud source repos update airflow_dags                 --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
gcloud source repos update nSegment                     --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
Steps followed to develope MS Teams webhook

  
Create pubsub topic 
gcloud pubsub topics create projects/syw-cdw-ti-prod/topics/csr2teamswebhook
 
How to add your project git changes to this channel?
gcloud source repos update AdobeCampaignInterimLayer    --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
gcloud source repos update AdobeCampaignMart            --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
gcloud source repos update AdobeCampaignMart_VM_Config  --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
gcloud source repos update airflow_dags                 --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
gcloud source repos update nSegment                     --add-topic=csr2teamswebhook --message-format=json
               --service-account=edwetlpd-prod@syw-cdw-ti-prod.iam.gserviceaccount.com
 
Create a cloud function on pusub topic
    link python code csr2teamswebhook.py
 
