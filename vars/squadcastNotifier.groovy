#!/usr/bin/env groovy
def call(String action) {
  if(action == "start") {
    env.BUILD_STATUS = "STARTED"
    env.PRIORITY = "P5"
  } else {
    env.BUILD_STATUS = currentBuild.currentResult
  }
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