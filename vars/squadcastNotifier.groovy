#!/usr/bin/env groovy

def call() {
  echo "antes"
  def BUILD_STATUS = currentBuild.currentResult
  echo "${BUILD_STATUS}"
  sh "curl https://raw.githubusercontent.com/caiohasouza/test-oldmonk/test/jenkins-squadcast-notifications.py | python3 -"
}