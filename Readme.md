### Technologies & tools

- Python
- Django
- Docker


## Instructions

1. Install docker
2. Run `docker-compose up` in the root directory
3. Run `file_upload_project` by running `python manage.py runserver 0.0.0.0:8080` in the root directory
4. Open `http://localhost:8001/services` in your browser to see all the services
5. Use services on `http://localhost:8001/path`


## Folder Structure: `server`

- `file_upload_project`: Contains the file upload simulation service
- `docker-compose.yml`: Contains the docker-compose configuration
- `kong.yml`: Contains the Kong configuration
- `Readme.md`: This file

