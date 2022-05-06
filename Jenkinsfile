pipeline {
     agent any
    stages {

        stage ('Git  Clone') {
            steps {
                git branch: 'main', credentialsId: 'GitHub_Credentials', url: 'https://github.com/itsbharatsaini/Selenium.git'
            }
        }
        
        stage ('Check GitHub Repo') {
            steps {
               powershell 'dir'
                
            }
        }
       
		}
  
    }  