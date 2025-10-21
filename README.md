# 🚀 Jenkins CI/CD Pipeline Project

## 🧩 Overview
A **Jenkins pipeline** that automatically **builds**, **tests**, and **deploys** a **Python application** using **Docker**.  
The entire process is triggered automatically through **GitHub Webhooks**.

---

## ⚙️ Infrastructure Setup

- 🖥️ **AWS EC2 Instance** — Deployed Jenkins server  
- 🔗 **GitHub Webhook** — Configured for automatic pipeline triggers on code push  
- 🐳 **Docker** — Installed on the EC2 instance for containerized deployment  

---

## 🛠️ What I Did

### 🧱 1. Created a Dockerfile
- Containerized a **Python application**
- Used the **Python Slim** base image for efficiency  
- Installed dependencies and ran the application

---

### ⚡ 2. Built a Jenkins Pipeline

The pipeline consists of **three stages**:

#### 🔨 Build Stage
- Builds a Docker image tagged as `foo:bar`

#### ✅ Test Stage
- Verifies the Docker image was created successfully  
- Fails automatically if the image does not exist

#### 🚀 Deploy Stage
- Stops any existing running container  
- Runs a new container on **port 8085**  
- Container name: **foo-container**

---

### 🔁 3. Automated the Workflow
- **GitHub Webhook** triggers the pipeline on each push  
- Jenkins automatically runs **Build → Test → Deploy**  
- Fully automated — no manual intervention required 💪  

---

## 💡 Technologies Used

| Technology             | Purpose                     |
|------------------------|-----------------------------|
| 🖥️ **AWS EC2**         | Host Jenkins server         |
| ⚙️ **Jenkins**         | CI/CD automation            |
| 🐳 **Docker**          | Containerization            |
| 🐍 **Python**          | Application runtime         |
| 🔔 **GitHub Webhooks** | Automated pipeline triggers |

---

## 🖼️ Pipeline Visualization

The pipeline execution output and diagram can be found here:  
📂 `docs/image.png`

---

## 📌 Example Command (for Deployment)

```bash
docker run -d -p 8085:8080 --name foo-container foo:bar
