# Fullstack CRUD application template

## Description

The application is built using the following technologies:

- Flask: for the backend API and working with the database
- VueJS: for the frontend
- PostgreSQL
- Nginx: for serving the frontend

Everything is wrapped up into the Docker, using the docker-compose and has two separate configurations - for local development and for production.

Project is built the way it could be deployed on the Virtual Machine from the cloud provider of your preference (AWS, Google Cloud, Azure, Heroku etc). I used AWS EC2 instance to deploy the project, that's why my configurations mention credentials specific for it.

The application itself is something like micropost platform - it allows you to add messages, delete and edit them. Messages are kept in the database.

## Installation

To install everything on your local machine you'd need to have Docker and docker-compose installed locally. If you need to tweak the project configuration, e.g. Python or JS dependencies - you need to have Python and/or node.js installed locally.

## Configuration

The project is configured via environment variables, for convenience they could be placed into the `.env` file (e.g. `config.env`):

```
export EC2_INSTANCE_PUBLIC_DOMAIN="ec2_public_domain_name"
# default value for EC2_USER:
export EC2_USER="ec2-user"
```

## Development

The first thing to do is to configure the project by setting the environment variables, if you have them in the `config.env` file the following command sequence will work:

```
source config.env
docker-compose up -d
```

Backend API is running on http://localhost:5000 
Frontend is running on http://localhost:8080
Database is running on http://localhost:5432

Also you need to create a database in PostgreSQL, the project is configured to work with /messages database:
```
➜ psql -h localhost -p 5432 -U tester
Password for user tester:
psql (10.14 (Ubuntu 10.14-0ubuntu0.18.04.1), server 11.2 (Debian 11.2-1.pgdg90+1))
WARNING: psql major version 10, server major version 11.
         Some psql features might not work.
Type "help" for help.

tester=# create database messages;
```

## Deploy

The easiest way to deploy this project to a Virtual Machine is to install the following tools inside the VM:
- `git`
- `docker`
- `docker-compose`

Pull the code to the instance:
```
git clone https://github.com/al-serebrov/vue-flask-template
```

Build and push the built frontend to the server:
```
source config.env &&
export VUE_APP_API_ENDPOINT=$EC2_INSTANCE_PUBLIC_DOMAIN &&
cd frontend &&
npm run build &&
scp -r -i /path/to/the/private/key.pem "$EC2_USER@$EC2_INSTANCE_PUBLIC_DOMAIN":/home/ec2-user/app-python-auto-ria/frontend/
```

On the sever run:
```
docker-compose -f docker-compose.prod.yml
```

Also, if needed, configure traffic rules and security groups on the AWS: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html

The application is accessible on your public EC2 domain!
