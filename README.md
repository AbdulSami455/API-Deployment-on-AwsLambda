𝑨𝑷𝑰 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒎𝒆𝒏𝒕 𝒐𝒏 𝑨𝒘𝒔 𝑳𝒂𝒎𝒃𝒅𝒂

This Repo is about Deploying FastAPi on Aws Lambda

𝑾𝒉𝒂𝒕 𝒊𝒔 𝑨𝒘𝒔 𝑳𝒂𝒎𝒃𝒅𝒂?

AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you.


![sam-layers-diag](https://github.com/AbdulSami455/API-Deployment-on-AwsLambda/assets/111019622/132b9f19-70a4-4617-b5c2-0b7838d02362)


We use Mangum so that Lambda can find the handler and call the correct endpoints.

𝑹𝒖𝒏 𝒕𝒉𝒆𝒔𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝒇𝒓𝒐𝒎 𝒕𝒉𝒆 𝒑𝒓𝒐𝒋𝒆𝒄𝒕 𝒅𝒊𝒓𝒆𝒄𝒕𝒐𝒓𝒚 𝒊𝒏 𝒕𝒆𝒓𝒎𝒊𝒏𝒂𝒍
𝙈𝙖𝙠𝙚 𝙨𝙪𝙧𝙚 𝙩𝙝𝙖𝙩 𝙩𝙝𝙚 𝙇𝙖𝙢𝙗𝙙𝙖 𝙛𝙪𝙣𝙘𝙩𝙞𝙤𝙣 𝙝𝙖𝙨 𝙖 𝙁𝙪𝙣𝙘𝙩𝙞𝙤𝙣 𝙐𝙧𝙡 - 𝙨𝙚𝙩 𝙞𝙩 𝙩𝙤 𝙉𝙊𝙉𝙀 𝙛𝙤𝙧 𝙖𝙪𝙩𝙝𝙉 𝙛𝙤𝙧 𝙩𝙚𝙨𝙩𝙞𝙣𝙜
𝙀𝙙𝙞𝙩 𝙩𝙝𝙚 𝙝𝙖𝙣𝙙𝙡𝙚𝙧 𝙞𝙣 𝙡𝙖𝙢𝙗𝙙𝙖 𝙩𝙤 𝙢𝙖𝙞𝙣.𝙝𝙖𝙣𝙙𝙡𝙚𝙧 - 𝙘𝙝𝙚𝙘𝙠 𝙩𝙝𝙚 𝘾𝙡𝙤𝙪𝙙𝙒𝙖𝙩𝙘𝙝 𝙇𝙤𝙜𝙨 𝙩𝙤 𝙨𝙚𝙚 𝙬𝙝𝙮 𝙞𝙩 𝙛𝙖𝙞𝙡𝙨.
![awsdeploy](https://github.com/AbdulSami455/API-Deployment-on-AwsLambda/assets/111019622/19bd8ab1-c2dc-467e-96f5-8453fe3d8272)

1. pip3 install -t dep -r requirements.txt
2. (cd dep; zip ../lambda_artifact.zip -r .)
3. zip lambda_artifact.zip -u main.py


𝙐𝙥𝙡𝙤𝙖𝙙 𝙩𝙝𝙚 .𝙯𝙞𝙥 𝙛𝙞𝙡𝙚 𝙩𝙤 𝙇𝙖𝙢𝙗𝙙𝙖 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝘼𝙬𝙨 𝘾𝙤𝙣𝙨𝙤𝙡𝙚 𝙩𝙤 𝙖 𝙇𝙖𝙢𝙗𝙙𝙖 𝙁𝙪𝙣𝙘𝙩𝙞𝙤𝙣.

