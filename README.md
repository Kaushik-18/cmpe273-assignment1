# cmpe273-assignment1
Flask application using github API

The purpose is to build a simple Flask application which reads its configration data from a Github repo.Also includes a DOCKERFILE for creating a docker container

# How to run :

To start container :-

docker run -d -p 5000:5000 assignment1-flask-app [ URL of repository]

To view output :- 

curl -i [IP_Address of container]:5000/v1/[file name] 



