#!/usr/bin/env groovy
def call(String action) {
  def additionalArgs
  def priority
  if(action == "start") {
    env.BUILD_STATUS = "STARTED"
    priority = "P5"
  } else {
    env.BUILD_STATUS = currentBuild.currentResult
    priority = "${env.PRIORITY}"
  }
  if(priority == "null") {
    additionalArgs = "--priority P3"
  } else {
    additionalArgs = "--priority ${env.PRIORITY}"
  }
  final file = libraryResource('jenkins-squadcast-notifications.py')
  writeFile(file: 'jenkins-squadcast-notifications.py', text: file)
  sh "python3 jenkins-squadcast-notifications.py $additionalArgs"
}