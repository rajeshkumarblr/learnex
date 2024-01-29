# Learnex

## Goal
Learnex is an AI-assisted learning app for students (specfically for CBSE XII students for now, will be extended in future to other classes also). This is a non-profit, open source, free learning app for assisting students in their studies and learning.

## Project Status
The project is under development and planned to be completed in 3 months time.

## Planned Features

1) Provide all standard CBSE lessons in one place in a customised UI, where the students can interact with AI for clearing their doubts and use it for learning.
2) Organise freely availeble resources and arrange them along with lessons, so that the students can refer to them easily.
3) Provide an AI based evaluation mechanism to students to check their understanding on a subject.
4) Provide a calender interface to students, to track their learnings and plan for exams effectively.

## Backend
The backend is a simple Python Flask application that provides a REST API interface for students to learn about a particular subject. It also provides a wrapper over an AI-based agent for learning through conversation with a Language Model (LLM).

## Frontend
The frontend is implemented in Next.js. It provides a simple and intuitive UI for students to learn a particular subject with all learning resources in one place. It offers an easy way to get assistance from AI to clear doubts and have conversations with AI to deeply learn a subject and understand the concepts clearly.
## DockerSetup

* Build the image using docker build command `docker build -t <image_name> .`.
* Create a file .env where all the values or secrets are mentioned.
* Run the container using `docker run --env-file <path_to_env_file> -p 8501:8501 <image_name>`