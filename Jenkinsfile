pipeline{
    agent any
    stages{
        stage("build"){
            agent{
                docker{
                    image 'python:alpine'
                }
            }
            steps{
                echo 'building...'
                echo "$HOME"
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install -r requirements.txt'
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
                sh "echo $HOME"
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    //sh 'pip install -r requirements.txt'
                    echo "echoing... $HOME"
                    sh "echo $HOME"
                    sh "printenv"
                    sh 'python -m pytest -v --junit-xml test_results.xml src/appTest.py'
                }
            }
            
            post {
                always {
                    junit 'test_results.xml'
                }
            }
        }
    }
}
