pipeline {
    environment {
        registry = "linea/centaurus"
        registryCredential = 'Dockerhub'
        dockerImage = ''
        deployment = 'centaurus'
        namespace = 'centaurus'
    }
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Test'
            }
        }
        stage('Building and push image') {
            when {
                allOf {
                    expression {
                        env.TAG_NAME == null
                    }
                    expression {
                        env.BRANCH_NAME.toString().equals('master')
                    }
                }
            }
            steps {
                script {
                sh 'docker build -t $registry:$GIT_COMMIT .'
                docker.withRegistry( '', registryCredential ) {
                    sh 'docker push $registry:$GIT_COMMIT'
                    sh 'docker rmi $registry:$GIT_COMMIT'
                }
                sh """
                  curl -D - -X \"POST\" \
                    -H \"content-type: application/json\" \
                    -H \"X-Rundeck-Auth-Token: $RD_AUTH_TOKEN\" \
                    -d '{\"argString\": \"-namespace $namespace -image $registry:$GIT_COMMIT -deployment $deployment\"}' \
                    https://run.linea.gov.br/api/1/job/793311e5-4f81-4ff2-9dd5-1ca58da79e14/executions
                  """
            }
        }
    }
        stage('Building and Push Image Release') {
            when {
                expression {
                    env.TAG_NAME != null
                }
            }
            steps {
                script {
                sh 'docker build -t $registry:$TAG_NAME .'
                docker.withRegistry( '', registryCredential ) {
                    sh 'docker push $registry:$TAG_NAME'
                    sh 'docker rmi $registry:$TAG_NAME'
                }
                sh """
                  curl -D - -X \"POST\" \
                    -H \"content-type: application/json\" \
                    -H \"X-Rundeck-Auth-Token: $RD_AUTH_TOKEN\" \
                    -d '{\"argString\": \"-namespace $namespace_prod -image $registry:$TAG_NAME -deployment $deployment\"}' \
                    https://run.linea.gov.br/api/1/job/793311e5-4f81-4ff2-9dd5-1ca58da79e14/executions
                  """
            }
        }
    }
  }
}
