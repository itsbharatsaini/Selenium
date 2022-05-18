pipeline{
    agent any
    stages{
        stage("Git Clone"){
            steps{
                echo "========Git Clone========"
                git branch: 'main', credentialsId: 'GitHub_Credentials', url: 'https://github.com/itsbharatsaini/Selenium.git'
                powershell 'dir'
            }   
        }

        stage("K8s Deploy"){
            steps{
                echo "========Deploy to K8s========"
                script {
                    withCredentials([kubeconfigFile(credentialsId: 'K8S_Credential', variable: 'KUBECONFIG')])
                    {
                        powershell 'kubectl apply -f Kubernetes\\selenium-hub-deployment.yaml'
                        powershell 'kubectl apply -f Kubernetes\\selenium-node-chrome-deployment.yaml'
                        
                        // powershell 'kubectl apply -f Kubernetes\\selenium-node-firefox-deployment.yaml'
                        // powershell 'kubectl apply -f Kubernetes\\selenium-node-edge-deployment.yaml'
                    }
                }
            }
        }
    }
}
