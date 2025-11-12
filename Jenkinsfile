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
                bat '"C:\\Users\\ybritavskyi\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat '"C:\\Users\\ybritavskyi\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest --junitxml=report.xml || echo "Pytest failed"'
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
