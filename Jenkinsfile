pipeline {
     agent any

     stage ('Git  Clone') {
            steps {
                git branch: 'main', credentialsId: 'GitHub_Credentials', url: 'https://github.com/itsbharatsaini/Selenium.git'
                echo 'Test'
            }
        }
        
        stage ('Check GitHub Repo') {
            steps {
               powershell 'dir'
                
            }
        }
       
		}
  
    }  
