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
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                    sh 'python -m py_compile src/*.py'
                    stash(name: 'compiled-results', includes: 'src/*.py*')
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
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    //sh 'pip install --user -r requirements.txt'
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
