#! env/bin/groovy 
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
        stage("Check version and bump it") { 
            steps { 
                script { 
                    echo" build number ${BUILD_NUMBER}"
                }
            }
        }
        stage("Wow here i am") { 
            steps { 
                script{
                    echo "now what"
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
    }
}