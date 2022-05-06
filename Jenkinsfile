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
       
<<<<<<< HEAD
=======
        stage ('Test') {
			steps {  
				sh 'ls'
			}
>>>>>>> a9831361f3ac108a4aafefeefaf19255c521a0c8
		}
  
    }  