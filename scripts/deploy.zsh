#!/bin/zsh

az group create --name azurearmfunctiondocker --location uksouth

az deployment group create \
--name 'azurearmfunctiondocker' \
--resource-group azurearmfunctiondocker \
--template-file 'deployment_template.json' \
--parameters 'parameters.json'