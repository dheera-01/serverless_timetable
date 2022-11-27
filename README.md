# serverless_timetable
Contains the openfaas functions for building timetable generating application.

## Serverless
Before deploying the functions, we have to do port-forwarding and extract secret for gateway.
These instruction are provided on *https://docs.openfaas.com/deployment/kubernetes/* section.

Forward the gateway to your machine.\
`kubectl rollout status -n openfaas deploy/gateway`\
`kubectl port-forward -n openfaas svc/gateway 8080:8080 &`\

If basic auth is enabled, you can now log into your gateway.\
`PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)`\
`echo -n $PASSWORD | faas-cli login --username admin --password-stdin`\

Credentials extraction for open-faas portal.\
Username: "admin"\
Password: It can be extracted from the PASSWORD variable using echo $PASSWORD\

Serverless folder contains the code for functions deployed. 
Following are the instructions for building and deploying the function on OpenFaaS setup.

Build: `faas-cli build -f function_name.yml`\
Push: `faas-cli push -f function_name.yml`\
Deploy: `faas-cli deploy -f function_name.yml`\
Combined command: `faas-cli up -f function_name.yml`\

The parameters for the functions can be changed using the following syntax(were used during load testing.)\
`faas-cli up -f function_name.yml --label com.openfaas.scale.max=10 --label com.openfaas.scale.target=5 --label com.openfaas.scale.type=rps --label com.openfaas.scale.target-proportion=1.0 --label com.openfaas.scale.zero=true --label com.openfaas.scale.zero-duration=5m`


### Script Instructions
The *ServerlessScript.py* is the script for using the deployed functions.\
Command for running: `python3 ServerlessScript.py`\
The timetable is downloaded as *timetable.html*.\

## Server
Server folder contains the code for building the server on local machine. The `index.py` contains the same code which is used for creating server in the container given in the python3-flask template of OpenFaaS store. Function folder contains the complete for logic and csv files.\

Command for creating server on local machine: `python3 index.py`\
Command for running script: `python3 ServerScript.py`\
