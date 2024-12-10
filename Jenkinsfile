pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the repository...'
                git url: 'https://github.com/iamdipali/Testjen.git', branch: 'main'
            }
        }
        stage('Run Hello World Script') {
            steps {
                echo 'Running the Hello World Python script...'
                bat 'python hello.py'  // Use `python` or `python3` as appropriate based on your setup
            }
        }
    }
}
