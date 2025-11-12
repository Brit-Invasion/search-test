pipeline {
    agent any

    options {
        buildName "Build №${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Brit-Invasion/search-test' 
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python packages...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'pytest --junitxml=report.xml || true'
            }
        }
    }

    post {
        always {
            echo 'Archiving test results...'
            junit 'report.xml'
        }
    }
}
