pipeline {
	environment {
		registry = "linea/centaurus"
		registryCredential = 'Dockerhub'
		dockerImage = ''
		deployment = 'centaurus'
		namespace = 'condor-monitor'
		commit = ''
	}
  agent any
  stages {
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
            -d '{\"argString\": \"-namespace $namespace -commit $GIT_COMMIT -image $registry:$GIT_COMMIT -deployment $deployment\"}' \
            https://run.linea.gov.br/api/1/job/0b1c0a88-4137-43f5-aa11-4bf6f3382db0/executions
          """
        }
      }
    }
  }
}
