pipeline {
	environment {
		registry = "linea/andromeda"
		registryCredential = 'Dockerhub'
		dockerImage = ''
		deployment = 'andromeda'
		namespace = 'condor-monitor'
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
            -d '{\"argString\": \"-namespace $namespace -image $registry:$GIT_COMMIT -deployment $deployment\"}' \
            https://run.linea.gov.br/api/1/job/c1cd3d02-d1d7-47f1-b503-4d97a4755df6/executions
          """
        }
      }
    }
  }
}
