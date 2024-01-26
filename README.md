# learnex
AI assisted learning app for students

## DockerSetup

* Build the image using docker build command `docker build -t <image_name> .`.
* Create a file .env where all the values or secrets are mentioned.
* Run the container using `docker run --env-file <path_to_env_file> -p 8501:8501 <image_name>`