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
                echo 'building...'
                sh 'python -m py_compile src/*.py'
                stash(name: 'compiled-results', includes: 'src/*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml src/appTest.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
