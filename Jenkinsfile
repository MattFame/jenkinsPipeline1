pipeline{
    agent none
    stages{
        stage("build"){
            agent{
                docker{
                    image 'python:alpine'
                }
            }
            
            steps{
                echo 'python version command will run...'
                sh 'python --version'
            }

        }
    }
}
