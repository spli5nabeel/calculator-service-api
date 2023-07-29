@Library('build-api-shared-lib') _

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                println "Inside build package..."   
                buildPackage()             
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
