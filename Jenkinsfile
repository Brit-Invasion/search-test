pipeline {
    agent any
    
    stages {

        stage('Set Build Name') {
            steps {
                script {
                    currentBuild.displayName = "Build №${BUILD_NUMBER}" 
                }
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
