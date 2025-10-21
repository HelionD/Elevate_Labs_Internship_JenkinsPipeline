pipeline {
    agent any

    environment {
        IMAGE_NAME = "foo"
        IMAGE_TAG  = "bar"
        CONTAINER_NAME = "foo-container"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building the Docker image..."
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Test') {
            steps {
                echo "Checking if Docker image exists..."
                sh """
                if ! docker images | grep -q ${IMAGE_NAME}; then
                    echo "❌ Image not found!"
                    exit 1
                fi
                echo "✅ Image built successfully."
                """
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying the application locally..."
                sh """
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
                docker run -d -p 8080:8080 --name ${CONTAINER_NAME} ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
