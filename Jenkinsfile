pipeline {
    agent any
        stages {
            stage('Git Clone') {
                steps {
                    git 'https://github.com/chakradhar06/Jenkins.git'
                }
            }
            stage('Build Code') {
                steps {
                    sh "/usr/bin/python3 fibonacci.py"
                }
            }
            stage('Test Code') {
                steps {
                    sh "/usr/bin/python3 test.py"
                }
            }
            stage('Monitoring') {
                steps{
                    echo "This is a monitoring step"
                }
            }
        }
}