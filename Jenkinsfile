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

        stage('deliver') {
            agent any
            environment {
                VOLUME = '$(pwd):/src'
                IMAGE = 'cdrx/pyinstaller-linux:python3'
            }
            steps {
                dir(path: env.BUILD_ID) {     
                    unstash(name: 'compilation_result')       
                    sh "docker run -v ${VOLUME} ${IMAGE} 'pyinstaller -F src/app.py'"  
                }
            }

            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/src/dist/linux/app"     
                    sh "docker run -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}
