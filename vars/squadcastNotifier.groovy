#!/usr/bin/env groovy

def call() {
  echo "antes"
  def BUILD_STATUS = currentBuild.currentResult
  sh "ls -la"
  final file = libraryResource('jenkins-squadcast-notifications.py')
  writeFile(file: 'jenkins-squadcast-notifications.py', text: pythonContent)
  //sh('chmod +x my_file.py && ./my_file.py')

  sh "find / -name jenkins-squadcast-notifications.py"
  sh "curl https://raw.githubusercontent.com/caiohasouza/test-oldmonk/test/jenkins-squadcast-notifications.py | python3 - --url ${env.SQUADCAST_URL} --build-number  ${env.BUILD_NUMBER} --job-name ${env.JOB_NAME} --build-url ${env.BUILD_URL} --job-url ${env.JOB_URL} --build-status ${BUILD_STATUS}"
}