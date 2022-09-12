#! env/bin/groovy 
def version 
pipeline {
    agent any 

    stages { 
        stage("Init the application") {
            steps { 
                script {
                    echo "Hello there, ${BRANCH_NAME}"
                }
            }
        }
        stage("Read the current version of the application") { 
            steps { 
                script { 
                    echo" build number ${BUILD_NUMBER}"
                    def matcher = readFile("__init__.py") =~  "__version__=(.+)"
                    echo "${matcher[0][1]}"
                    version = matcher[0][1]
                }
            }
        }
        stage("Test stage") { 
            steps { 
                script{
                    echo "now what"
                    // sh "pytest"
                }
            }
        }
        stage("Build") { 
            steps { 
                script{
                    echo "now what"
                }
            }
        }
        stage('Deploy the version and tag'){
            steps {
                scripts {
                    sh "npx semantic-release"
                }
            }
        }
    }
}