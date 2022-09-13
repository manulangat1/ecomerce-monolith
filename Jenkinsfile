#! env/bin/groovy 
def version 
// def newVersion
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
                    docker system prune -a -f 
                    docker-compose -f docker-compose.yaml down
                    docker-compose -f docker-compose.yaml up --build   -d
                    docker-compose -f docker-compose.yaml  exec -T web bump2version minor
                    '''
                    // sh "docker ps"
                    // sh "docker-compose -f docker-compose.yaml  exec web python3 manage.py migrate"
                    // sh "docker-compose -f docker-compose.yaml  logs -f"
                    // docker-compose -f docker-compose.yaml  logs -f
                }
            }
        }
        stage('Deploy the version and tag'){
            steps {
                script {
                    
                    echo" build number ${BUILD_NUMBER}"
                    def matchers = readFile("__init__.py") =~  "version = (.+)"
                    echo "${matchers[0][1]}"
                    // def newVersion = matchers[0][1]
                    // echo "${newVersion}"
                    // sh "docker-compose -f docker-compose.yaml down"

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
// post{ 
//     always { 
//         sh '''
//         docker system prune -a -f 
//         docker-compose -f docker-compose.yaml down
//         '''
//     }
// }