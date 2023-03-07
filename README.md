# mdm_project_1

### Deploy this app to an azure app service
```
$ az webapp up --name rani-flask-demo --resource-group mdm --location switzerlandnorth --runtime PYTHON:3.11 --sku F1 --logs
```

### Delete the azure app service
```
$ az group delete --name mdm --yes --no-wait
```