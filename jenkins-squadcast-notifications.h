#!/bin/bash
BUILD_RESULT=`echo $currentBuild.currentResult`
curl https://raw.githubusercontent.com/caiohasouza/test-oldmonk/master/jenkins-squadcast-notifications.py | python3 - jenkins-squadcast-notifications.py