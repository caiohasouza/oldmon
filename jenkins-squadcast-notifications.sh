#!/bin/bash
echo "echo current: $CURRENT_BUILD_RESULT"
echo "previous: $PREVIOUS_BUILD_RESULT"
curl https://raw.githubusercontent.com/caiohasouza/test-oldmonk/master/jenkins-squadcast-notifications.py | python3 - jenkins-squadcast-notifications.py