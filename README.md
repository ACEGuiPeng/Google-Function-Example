# Google-Function-Example
## Local Dev
```bash
cd ./src
functions-framework-python --target api_proxy
```
## Deploy
```bash
gcloud functions deploy python-http-function \
--gen2 \
--runtime=python311 \
--region=REGION \
--source=./src \
--entry-point=api_proxy \
--trigger-http \
--allow-unauthenticated
```