#!/usr/bin/env groovy

def call() {
  echo "test"
  sh "curl https://raw.githubusercontent.com/caiohasouza/test-oldmonk/test/jenkins-squadcast-notifications.py | python3 -"
}