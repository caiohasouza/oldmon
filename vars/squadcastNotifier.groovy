#!/usr/bin/env groovy
def start() {
  env.BUILD_STATUS = "STARTED"
  def priority = "${env.PRIORITY}"
  def additionalArgs
  if(priority != null) {
    additionalArgs = "--priority ${env.PRIORITY}"
  } else {
    additionalArgs = "--priority P5"
  }
  final file = libraryResource('jenkins-squadcast-notifications.py')
  writeFile(file: 'jenkins-squadcast-notifications.py', text: file)
  sh "python3 jenkins-squadcast-notifications.py"
}

def result() {
  env.BUILD_STATUS = currentBuild.currentResult
  def priority = "${env.PRIORITY}"
  def additionalArgs
  if(priority != null) {
    additionalArgs = "--priority ${env.PRIORITY}"
  } else {
    additionalArgs = "--priority P3"
  }
  final file = libraryResource('jenkins-squadcast-notifications.py')
  writeFile(file: 'jenkins-squadcast-notifications.py', text: file)
  sh "python3 jenkins-squadcast-notifications.py"
}