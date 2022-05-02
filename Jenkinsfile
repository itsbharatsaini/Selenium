pipeline {
    agent any
    stage('Deploy om K8s'){
        steps{
            powershell 'kubectl apply -f selenium-pod.yml'
        }
    }
}