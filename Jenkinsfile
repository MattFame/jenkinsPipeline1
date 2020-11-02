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
                sh 'sudo pip install -r requirements.txt'
                sh 'python -m py_compile src/*.py'
                stash(name: 'compiled-results', includes: 'src/*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:alpine'
                }
            }
            steps {
                sh 'python -m pytest -v --junit-xml test_results.xml src/appTest.py'
            }
            // post {
            //     always {
            //         junit 'test-reports/results.xml'
            //     }
            // }
        }
    }
}
