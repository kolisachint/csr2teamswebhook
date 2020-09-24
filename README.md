# csr2teamswebhook-
Cloud Source Repository to Microsoft Teams webhook
You can receive notifications of changes to your Google Cloud repositories by using Pub/Sub 

Configuring Pub/Sub notifications (google.com) 

 

CSR git push json message 

{ "name": "projects/syw-cdw-ti-prod/repos/AdobeCampaignMart", "url": "https://source.developers.google.com/p/syw-cdw-ti-prod/r/AdobeCampaignMart", "eventTime": "2020-09-24T15:05:07.107599Z", "refUpdateEvent": { "email": "sachin.koli@transformco.com", "refUpdates": { "refs/heads/master": { "refName": "refs/heads/master", "updateType": "UPDATE_FAST_FORWARD", "oldId": "973f4d41fc15cadfb715516de549b2ac2636d7d1", "newId": "835922d0b32304b918fe2592dde621352ba7b5ec" } } } } 

 

Create cloud function to trigger python webhook job, once pub sub receives a message 

 


 

 

 

MS Teams webhook information 

POST->https://outlook.office.com/webhook/f9b88694-aede-4ef1-9a34-25f17836b709@27e4c168-0323-4463-acad-7e124b566726/IncomingWebhook/481da1e377e24e5b8216e18b8f3296c1/0a244876-c3c5-4ff9-bd20-2414764ab9dc 

 

JSON-> 

{ 

  "@context": "https://schema.org/extensions", 

  "@type": "MessageCard", 

  "themeColor": "0072C6", 

  "title": "Visit the Outlook Dev Portal", 

  "text": "Click **Learn More** to learn more about Actionable Messages!", 

  "potentialAction": [ 

    { 

      "@type": "ActionCard", 

      "name": "Send Feedback", 

      "inputs": [ 

        { 

          "@type": "TextInput", 

          "id": "feedback", 

          "isMultiline": true, 

          "title": "Let us know what you think about Actionable Messages" 

        } 

      ], 

      "actions": [ 

        { 

          "@type": "HttpPOST", 

          "name": "Send Feedback", 

          "isPrimary": true, 

          "target": "http://..." 

        } 

      ] 

    }, 

    { 

      "@type": "OpenUri", 

      "name": "Learn More", 

      "targets": [ 

        { "os": "default", "uri": "https://docs.microsoft.com/outlook/actionable-messages" } 

      ] 

    } 

  ] 

} 
