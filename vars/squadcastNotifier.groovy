#!/usr/bin/env groovy

def call() {
  echo "antes"
  def BUILD_STATUS = currentBuild.currentResult
  //def PRIORITY
  //def ADDITIONAL_ARGS
  //if (PRIORITY == null) {
  //  def ADDITIONAL_ARGS = "--priority P3"
  //} else {
  //  def ADDITIONAL_ARGS = "P5"
  //}
  //sh "echo ${ADDITIONAL_ARGS}"
  def serviceNameVar
  def dockerPath
  def imageTagVar
  def serviceName


  // for backward compatibility
  if(serviceName != null) {
      serviceNameVar = "serviceName"
      dockerPath = "dockerRepo"
      imageTagVar = "imageTag"
  } else {
      serviceNameVar = "2"
      dockerPath = "env.dockerPath"
      imageTagVar = "env.imageTag"
  }
  sh "echo $serviceNameVar"
  final file = libraryResource('jenkins-squadcast-notifications.py')
  writeFile(file: 'jenkins-squadcast-notifications.py', text: file)
  //sh('chmod +x my_file.py && ./my_file.py')
  sh "python3 jenkins-squadcast-notifications.py --url ${env.SQUADCAST_URL} --build-number  ${env.BUILD_NUMBER} --job-name ${env.JOB_NAME} --build-url ${env.BUILD_URL} --job-url ${env.JOB_URL} --build-status ${BUILD_STATUS}"

  //sh "find / -name jenkins-squadcast-notifications.py"
  //sh "curl https://raw.githubusercontent.com/caiohasouza/test-oldmonk/test/jenkins-squadcast-notifications.py | python3 - --url ${env.//SQUADCAST_URL} --build-number  ${env.BUILD_NUMBER} --job-name ${env.JOB_NAME} --build-url ${env.BUILD_URL} --job-url ${env.JOB_URL} //--build-status ${BUILD_STATUS}"
}