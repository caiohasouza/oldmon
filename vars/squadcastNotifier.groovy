#!/usr/bin/env groovy
def call() {
  env.BUILD_STATUS = currentBuild.currentResult
  env.BUILD_STATUS2 = currentBuild.currentResult
  echo "$BUILD_STATUS2"
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