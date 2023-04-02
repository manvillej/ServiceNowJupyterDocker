# ServiceNowJupyterDocker
 A containerized JupyterLab application for analyzing ServiceNow data 

## Some Useful Commands
    docker-compose up -d --build
    docker-compose down -v
    docker-compose exec web <insert command>


## Set up your .env file
make sure to set up your .env file before building your docker image

    SERVICENOW_INSTANCE=yourinstancename
    SERVICENOW_USERNAME=yourusername
    SERVICENOW_PASSWORD=yourpassword
    JUPYTER_TOKEN=yourjupytertoken

The instance name is in the URL of your instance. for example: https://yourinstancename.service-now.com is "yourinstancename"

