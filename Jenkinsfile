pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7.9'
                }
            }
            steps {
                sh 'python manage.py test'
            }
        }
    }
}


