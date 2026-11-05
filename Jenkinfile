pipeline {
    agent any

    // Defines the parameters users will fill out before building
    parameters {
        string(name: 'NUM1', defaultValue: '0', description: 'Enter the first number')
        string(name: 'NUM2', defaultValue: '0', description: 'Enter the second number')
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls the code (including find_largest.py) from your repository
                checkout scm
            }
        }

        stage('Run Python Program') {
            steps {
                // Jenkins automatically passes NUM1 and NUM2 as environment variables
sh 'python find_largest.py'
            }
        }
    }
}
