pipeline {
    agent any
    stages{
    stage('Deploy om K8s'){
        steps{
            powershell 'kubectl apply -f selenium-pod.yml'
        }
    }
}
}