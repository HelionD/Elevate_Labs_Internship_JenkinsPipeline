🚀 Jenkins CI/CD Pipeline Project
🧩 Overview

A Jenkins pipeline that automatically builds, tests, and deploys a Python application using Docker.
The entire process is triggered automatically via GitHub Webhooks.

⚙️ Infrastructure Setup

AWS EC2 Instance — Deployed Jenkins server

GitHub Webhook — Configured for automatic pipeline triggers on code push

Docker — Installed on EC2 instance for containerized deployment

🛠️ What I Did
1️⃣ Created a Dockerfile

Containerized a Python application

Used the Python slim base image for lightweight efficiency

Installed dependencies and executed the app

2️⃣ Built a Jenkins Pipeline

The pipeline consists of three stages:

🧱 Build Stage

Builds a Docker image tagged as foo:bar

🧪 Test Stage

Verifies the image was created successfully

Fails automatically if the image does not exist

🚀 Deploy Stage

Stops any existing running container

Runs a new container on port 8085

Container name: foo-container

3️⃣ Automated the Workflow

GitHub Webhook triggers the pipeline automatically on every push

Jenkins runs the build → test → deploy sequence

Fully automated — no manual intervention needed ✅

💡 Technologies Used
Tool	Purpose
AWS EC2	Hosts Jenkins
Jenkins	CI/CD automation
Docker	Containerization
Python	Application runtime
GitHub Webhooks	Automated pipeline triggers

🖼️ Pipeline Output

The pipeline response and visual result are available in:
📂 */docs/image.png*