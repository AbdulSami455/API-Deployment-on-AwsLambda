𝑨𝑷𝑰 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒎𝒆𝒏𝒕 𝒐𝒏 𝑨𝒘𝒔 𝑳𝒂𝒎𝒃𝒅𝒂

This Repo is about Deploying FastAPi on Aws Lambda

𝑾𝒉𝒂𝒕 𝒊𝒔 𝑨𝒘𝒔 𝑳𝒂𝒎𝒃𝒅𝒂?

AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you.


![sam-layers-diag](https://github.com/AbdulSami455/API-Deployment-on-AwsLambda/assets/111019622/132b9f19-70a4-4617-b5c2-0b7838d02362)


We use Mangum so that Lambda can find the handler and call the correct endpoints.

𝑹𝒖𝒏 𝒕𝒉𝒆𝒔𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝒇𝒓𝒐𝒎 𝒕𝒉𝒆 𝒑𝒓𝒐𝒋𝒆𝒄𝒕 𝒅𝒊𝒓𝒆𝒄𝒕𝒐𝒓𝒚 𝒊𝒏 𝒕𝒆𝒓𝒎𝒊𝒏𝒂𝒍

1. pip3 install -t dep -r requirements.txt
2. (cd dep; zip ../lambda_artifact.zip -r .)
3. zip lambda_artifact.zip -u main.py
