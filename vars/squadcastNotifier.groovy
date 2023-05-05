#!/usr/bin/env groovy

def call() {
  echo "antes"
  def current = currentBuild.currentResult
  def previous = currentBuild.previousBuild?.currentResult
  echo "${current}"
  echo "${previous}"
  echo "depois"
  sh "curl https://raw.githubusercontent.com/caiohasouza/test-oldmonk/test/jenkins-squadcast-notifications.py | python3 -"
}