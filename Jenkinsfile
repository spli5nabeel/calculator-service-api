@Library('build-api-shared-lib')

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                println "Inside build package..."                
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
