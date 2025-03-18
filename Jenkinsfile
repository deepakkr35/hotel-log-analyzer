pipeline {
    agent any

    environment {
        KUBECONFIG = "/root/.kube/config"
        DOCKER_IMAGE = "deepakkr35/hotel-log-analyzer"
        VERSION = "v1.0"
        DOCKER_REGISTRY = "index.docker.io"
    }

    stages {
        stage('Checkout code') {
            steps {
                git branch: 'main', url: 'https://github.com/deepakkr35/hotel-log-analyzer.git'
      }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${VERSION} ."
            }
        }

        stage('Run Tests') {
            steps {
                sh "docker run --rm ${DOCKER_IMAGE}:${VERSION} pytest tests/"
            }
        }

        stage('Push Docker Image') {
    steps {
        script {
            docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
                docker.image("${DOCKER_IMAGE}:${VERSION}").push()
            }
        }
    }
}

        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl apply -f k8s/namespace.yaml"
                sh "kubectl apply -f k8s/deployment.yaml"
                sh "kubectl apply -f k8s/service.yaml"
            }
        }
    }
}
