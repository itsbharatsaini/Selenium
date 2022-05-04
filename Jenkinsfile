pipeline {
     agent any
    stages {

        stage ('checkout') {
            steps {
            checkout([$class: 'GitSCM', branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/itsbharatsaini/Selenium.git']]])
            }
        }
       
        stage ('kubernetes Deploy') {
			steps {
				script {
					kubernetesDeploy(
						configs: 'selenium-pod.yaml',
						kubeconfigId: 'K8S'
						)           
				   
				}
			}
		}
  
    }  
}