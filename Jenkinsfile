pipeline {
    environment {
        registry = "linea/centaurus"
        registryCredential = 'Dockerhub'
        dockerImage = ''
    }
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'echo test'
            }
        }
        stage('Building and push image') {
            when {
                expression {
                   env.BRANCH_NAME.toString().equals('master')
                }
            }
            steps {
                script {
                dockerImage = docker.build registry + ":$GIT_COMMIT"
                docker.withRegistry( '', registryCredential ) {
                dockerImage.push()
                }
                sh "docker rmi $registry:$GIT_COMMIT"
                // sh 'curl -D - -X "POST" -H "Accept: application/json" \
                //     -H "Content-Type: application/json" \
                //     -H "X-Rundeck-Auth-Token: $RD_AUTH_TOKEN" \
                //     http://fox.linea.gov.br:4440/api/16/job/0430ff97-56fb-4bb4-b323-6f870bf3af94/executions'
            }
        }
    }
  }
}
