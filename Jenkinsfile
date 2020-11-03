pipeline{
    agent any
    environment {
        MYSQL_DATABASE_HOST = "database-42.cbanmzptkrzf.us-east-1.rds.amazonaws.com"
        MYSQL_DATABASE_PASSWORD = "Clarusway"
        MYSQL_DATABASE_USER = "admin"
        MYSQL_DATABASE_DB = "phonebook"
        MYSQL_DATABASE_PORT = 3306
        PATH="/usr/local/bin/:${env.PATH}"
    }
    stages{
        stage("compile"){
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
                    stash(name: 'compilation_result', includes: 'src/*.py*')
                }   
            }
        }

        stage('test') {
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

        // stage('deliver') {
        //     agent any
        //     environment {
        //         VOLUME = '$(pwd)/src:/src'
        //         IMAGE = 'cdrx/pyinstaller-linux:python3'
        //     }
        //     steps {
        //         dir(path: env.BUILD_ID) {     
        //             unstash(name: 'compilation_result')   
        //             sh "pwd"
        //             sh "ls"
        //             sh "docker run -rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F app.py'"  
        //         }
        //     }

        //     post {
        //         success {
        //             sh "ls"
        //             sh "pwd"
        //             archiveArtifacts "${env.BUILD_ID}/src/dist/app"     
        //             sh "docker run -rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
        //         }
        //     }
        // }

        stage('build'){
            agent any
            steps{
                sh "docker build -t matt/handson-jenkins ."
                sh "docker tag matt/handson-jenkins:latest 046402772087.dkr.ecr.us-east-1.amazonaws.com/matt/handson-jenkins:latest"
            }
        }
        stage('push'){
            agent any
            steps{
                sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 046402772087.dkr.ecr.us-east-1.amazonaws.com"
                sh "docker push 046402772087.dkr.ecr.us-east-1.amazonaws.com/matt/handson-jenkins:latest"
            }
        }

        stage('compose'){
            agent any
            steps{
                sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 046402772087.dkr.ecr.us-east-1.amazonaws.com"
                sh "docker-compose up"
            }
        }
    }
}
