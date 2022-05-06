pipeline{
    agent any
    stages{
        stage("Git Clone"){
            steps{
                echo "========Git Clone========"
                git branch: 'main', credentialsId: 'GitHub_Credentials', url: 'https://github.com/itsbharatsaini/Selenium.git'
            }
            
        }

        stage("Check Git Repo"){
            steps{
                echo "========Git Repo========"
                powershell 'dir'
            }
            
        }

        stage("K8s Deploy"){
            steps{
                echo "========Deploy to K8s========"
                script {
                    withCredentials([kubeconfigFile(credentialsId: 'K8S_Credential', variable: 'KUBECONFIG')])
                    {
                        powershell 'kubectl apply -f k8s\\selenium-hub-deployment.yaml'
                        powershell 'kubectl apply -f k8s\\selenium-node-chrome-deployment.yaml'
                        powershell 'kubectl apply -f k8s\\selenium-node-firefox-deployment.yaml'
                    }
                }
            }
            
        }
    }
}