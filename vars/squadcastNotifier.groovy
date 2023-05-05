#!/usr/bin/env groovy

def call() {
  echo "test"
  sh "curl https://raw.githubusercontent.com/caiohasouza/test-oldmonk/master/jenkins-squadcast-notifications.py | echo python3 -"
}