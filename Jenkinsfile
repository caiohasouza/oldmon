#!/usr/bin/env groovy
@Library('jenkins-squadcast-notifications') _ 

pipeline {
  options { 
    timeout(time: 14, unit: 'HOURS')
    skipDefaultCheckout()
  } 

  agent {
    kubernetes { 
      inheritFrom 'jenkins-slave-backup'
      defaultContainer 'k8s-jenkins-toolbox'
    }
  }

  stages {
    stage('Checkout') {
      steps {
        retry(3) {
          script {
            checkout scm
          }
        }
      }
    }

    stage('Test') {
      steps {
        withEnv(["AWS_ROLE_ARN=${AWS_ROLE_ARN}", "AWS_REGION=${AWS_RDS_REGION}"]) {
          sh "echo test"
          sh "exit 1"
        }
      }
    }
  }
  //post {
  //  always {
  //    //jenkins-squadcast-notifications.runMyPython()
  //  }
  //}
}