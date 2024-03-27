pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m venv venv'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        stage(' Running Tests') {
            steps {
                catchError{
                echo 'Testing..'
                bat "venv\\Scripts\\python.exe report_unit_pytest.py"
                }
            }
        }
        stage('Publish Report') {
            steps {
                echo 'Publish Report..'
                bat 'powershell Compress-Archive -Path report.html -DestinationPath report.zip -Force'
                archiveArtifacts artifacts: 'report.zip', onlyIfSuccessful: true
            }
        }
    }
}

