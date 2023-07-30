@Library('build-api-shared-lib') _

pipeline {
    agent any

    stages {
        stage('Prepare Build Package') {
            steps {
                println "Inside build package..."   
                buildPackage()             
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Preparing Docker image'
            }
        }
        stage('Deploying Image to K8 Cluster') {
            steps {
                echo 'Preparing Docker image'
            }
        }
        stage('Upload Image to Nexus') {
            steps {
                echo 'Uploading Docker Image to Nexus'
            }
        }
    }
}
