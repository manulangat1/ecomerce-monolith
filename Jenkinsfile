#! env/bin/groovy 
def version 
def newVersion
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
                    def matcher = readFile("__init__.py") =~  "version = (.+)"
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
                    // sh "docker-compose -f docker-compose.yaml up -d "
                    sh ''' 
                    docker-compose -f docker-compose.yaml up -d
                    // docker-compose -f docker-compose.yaml  exec web python3 manage.py migrate
                    docker-compose -f docker-compose.yaml  logs -f
                    '''
                    // sh "docker ps"
                    // sh "docker-compose -f docker-compose.yaml  exec web python3 manage.py migrate"
                    // sh "docker-compose -f docker-compose.yaml  logs -f"
                }
            }
        }
        stage('Deploy the version and tag'){
            steps {
                script {
                    
                    echo" build number ${BUILD_NUMBER}"
                    def matchers = readFile("__init__.py") =~  "version = (.+)"
                    echo "${matchers[0][1]}"
                    newVersion = matchers[0][1]
                    // sh "docker-compose -f docker-compose.yaml  exec web python3 manage.py migrate  "
                    // sh "bump2version minor"

                    // withCredentials([usernamePassword(credentialsId:"github-credentials", usernameVariable:'USER', passwordVariable:'PASS')]) { 
                    //     sh   "git config --global user.name jenkins"
                    //     sh "git config --global user.email jenkins@jobs.com"
                    //     sh "git status"
                    // }
                }
            }
        }
    }
}