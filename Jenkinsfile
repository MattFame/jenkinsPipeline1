pipeline{
    agent any
    environment {
        MYSQL_DATABASE_HOST = "database-42.cbanmzptkrzf.us-east-1.rds.amazonaws.com"
        MYSQL_DATABASE_PASSWORD = "Clarusway"
        MYSQL_DATABASE_USER = "admin"
        MYSQL_DATABASE_DB = "phonebook"
        MYSQL_DATABASE_PORT = 3306
    }
    stages{
        stage("build"){
            agent{
                docker{
                    image 'python:alpine'
                }
            }
            steps{
                // echo 'building...'
                // echo "$HOME"
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    //sh 'pip install -r requirements.txt'
                    sh 'python -m py_compile src/*.py'
                    stash(name: 'compiled', includes: 'src/*.py*')
                }   
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:alpine'
                }
            }

            steps {
                // sh "echo $HOME"
                // sh "echo ${HOME}"
                // echo "$HOME"
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    //sh 'pip install -r requirements.txt'
                    // echo "echoing... $HOME" //both are the same
                    // sh "echo ${HOME}"
                    // sh "printenv"
                    sh 'python -m pytest -v --junit-xml results.xml src/appTest.py'
                }
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
    }
}
