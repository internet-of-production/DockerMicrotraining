## The internal presentation for the IoP can be found here: https://git-ce.rwth-aachen.de/iop/infrastructure/dockerandk8smicrotraining/-/tree/master

## How to use

## Server
Server for serving 3 Routes. /getID, /saveJson and /getJson.

getID can be used without a Database. It will return a random number picked on server startup

saveJson and getJson need a Mongodb. You can set the connection values for this by providing the envvariable MONGOHOST and MONGOPORT.
Default is 127.0.0.1:27017

## Scripts
add_data.sh will send a PUT request to localhost:27017/saveJson with a jsonmessage. This JSON should be saved in the database.
get_data.sh will send a GET request to localhost:27017/getJson. This should return all JSONS in the database
