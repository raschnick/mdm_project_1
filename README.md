# mdm_project_1

### Deploy this app to an azure app service
TODO: add rg, region and adapt sku
```
$ az webapp up --runtime PYTHON:3.11 --sku F1 --logs
```

### Delete the azure app service
TODO: adapt rg name
```
$ az group delete --name raschnic_rg_3893 --yes --no-wait
```