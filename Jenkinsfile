// pipeline {
//     agent any
//     environment {
//         PYTHONPATH = "C:/Users/hp/PycharmProjects/pythonFINAL"
//         TEST_REPORTS='test-reports'
//     }
//     stages {
//         stage('Build') {
//             steps {
//                 echo 'Building..'
//                 bat 'pip install -r requirements.txt' // Install dependencies if needed
//             }
//         }
//         stage('Test') {
//             steps {
//                 echo 'Testing..'
//                 // Run your tests here
//                 bat 'python report_unit_pytest.py'
//             }
//         }
// //         stage('Run API Tests with Pytest') {
// //             steps {
// //                 echo 'Running API Tests with Pytest...'
// //                 script {
// //                     try {
// //                         // Run pytest with pytest-html plugin to generate HTML report
// //                         bat "C:/Users/hp/anaconda3/Scripts/pytest.exe report_unit_pytest.py --html=test-reports/report.html"
// //                     } catch (Exception e) {
// //                         echo "Tests failed, but the build continues."
// //                     }
// //                 }
// //             }
// //         }
//         stage('Deploy') {
//             steps {
//                 echo 'Deploying..'
//                 // Add deployment steps here if needed
//             }
//                      }
//            }
// }

pipeline {
    agent any
    environment {
        // Define the Python virtual environment directory
        VENV_DIR = 'venv'
        // Define the project's root directory
        PROJECT_ROOT = "C:\\Users\\hp\\PycharmProjects\\pythonFINAL"
        // Define the path to the Python executable
        PYTHON_PATH = "C:\\Python310\\python.exe"
        // Define the directory where HTML reports will be generated
        HTML_REPORT_DIR = "reports"
    }
    stages {
        stage('Preparation') {
            steps {
                echo 'Checking out SCM'
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    // Navigate to project's root directory
                    bat "cd ${PROJECT_ROOT}"
                    // Set up virtual environment if it doesn't exist
                    bat "if not exist ${VENV_DIR} call \"%PYTHON_PATH%\" -m venv ${VENV_DIR}"
                    // Activate virtual environment
                    bat "call ${VENV_DIR}\\Scripts\\activate"
                    // Upgrade pip to the latest version
                    bat "call ${VENV_DIR}\\Scripts\\python.exe -m pip install --upgrade pip"
                    // Install requirements
                    bat "call ${VENV_DIR}\\Scripts\\pip install -r requirements.txt"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Combining the commands into a single 'bat' invocation
                    bat 'python report_unit_pytest.py'
                }
            }
        }
        stage('List Report') {
            steps {
                script {
                    bat "dir ${PROJECT_ROOT}\\${HTML_REPORT_DIR}"
                }
            }
        }
        stage('Verify Report') {
            steps {
                script {
                    bat "type ${PROJECT_ROOT}\\${HTML_REPORT_DIR}\\report.html"
                }
            }
        }
        stage('Publish Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${PROJECT_ROOT}\\${HTML_REPORT_DIR}",
                    reportFiles: 'report.html',
                    reportName: "HTML Report"
                ])
            }
        }
        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: "${HTML_REPORT_DIR}/*", allowEmptyArchive: true
            }
        }
    }
}