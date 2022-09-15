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
        stage('SonarQube Analysis') {
                steps {
                    script {
                        def scannerHome = tool 'SonarScanner';
                            withSonarQubeEnv() {
                            sh "${scannerHome}/bin/sonar-scanner"
                            }
                    }
                }
            }
        stage("Create a virtual enviroment") { 
            steps{
                script{
                    echo "Now creating a virtualenv"
                    sh "python3 -m virtualenv venv"
                    sh "chmod +x venv/"
                    sh "ls"
                    sh ". venv/bin/activate"
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
                    
                    withCredentials([usernamePassword(credentialsId:'dockerhub-id', usernameVariable:"USER" , passwordVariable:"PASS")]) { 
                        // sh " echo ${PASS} | docker login -u $USER --stdin-"
                        sh ''' 
                    docker system prune -a -f 
                    docker-compose -f docker-compose.yaml down
                    docker-compose -f docker-compose.yaml up --build   -d
                    echo $PASS | docker login -u $USER --password-stdin
                    docker push manulangat/django-ecomerce-monolith
                    '''
                        // sh "echo $PASS | docker login -u $USER --password-stdin"
                        // sh "docker push manulangat/django-ecomerce-monolith-${BUILD_NUMBER}.${version}"
                    }
                    // docker-compose -f docker-compose.yaml  exec -T web bump2version minor
                }
            }
        }
        
        stage('Commit the version and tag'){
            steps {
                script {
                    
                    echo" build number ${BUILD_NUMBER}"
                    def matchers = readFile("__init__.py") =~  "version = (.+)"
                    echo "${matchers[0][1]}"

                    def vers = matchers[0][1]
                    echo "${vers}"
                    matchers = null
                    // def newVersion = matchers[0][1]
                    // echo "${newVersion}"
                    // sh "docker-compose -f docker-compose.yaml down"
// now
                    withCredentials([usernamePassword(credentialsId:"github-creds-hook", usernameVariable:'USER', passwordVariable:'PASS')]) { 
                        sh '''
                        chmod +x venv/
                        . venv/bin/activate
                        pip install -r requirements.txt
                        
                        git config --global user.name jenkins
                        git config --global user.email jenkins@jobs.com
                        git status
                        git config --list
                        git remote set-url origin https://$USER:$PASS@github.com/manulangat1/ecomerce-monolith.git
                        git push --tags -f
                        git tag | xargs git tag -d
                        chmod +x README.md 
                        chmod +x __init__.py 
                        chmod +x setup.py 
                        chmod +x CHANGELOG.md
                        bump2version  minor --allow-dirty
                        git describe --always
                        git push --tags -f
                        git tag | xargs git tag -d
                        
                        
                        '''
                        echo "Done pushing to github"
                    }
                }
            }
        }
    }
    post{ 
    always { 
        sh '''
        docker system prune -a -f 
        docker-compose -f docker-compose.yaml down
        rm -rf venv
        '''
        emailext body: "$JOB_NAME - Build # $BUILD_NUMBER - :Check console output at $BUILD_URL to view the results.", recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
    }
    failure { 
        echo "oops sth failed"
    }
}
}
