# learnex

#Goal
AI assisted learning app for students.

#Backend: 
The backend is a simple python Flask application that provides a REST API interface for students to learn about a particular subject and also provides a wrapper over an AI based agent for learning through conversation with an LLM.

#FrontEnd:
Frontend is implemented in Next.js. A simple and intuitive UI for students to learn a particular subject with all learning resources in one place. It proves an easy way to get assistance from AI to clear doubts and have conversations with AI to learn a subject deep and understand the concepts clearly.

## DockerSetup

* Build the image using docker build command `docker build -t <image_name> .`.
* Create a file .env where all the values or secrets are mentioned.
* Run the container using `docker run --env-file <path_to_env_file> -p 8501:8501 <image_name>`