#!/bin/bash
CURRENT_BUILD_RESULT=`echo $currentBuild.currentResult`
PREVIOUS_BUILD_RESULT=`echo $currentBuild.previousBuild`
echo "Current: $CURRENT_BUILD_RESULT"
echo "PRevious: $PREVIOUS_BUILD_RESULT"
curl https://raw.githubusercontent.com/caiohasouza/test-oldmonk/master/jenkins-squadcast-notifications.py | python3 - jenkins-squadcast-notifications.py