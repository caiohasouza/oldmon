def runMyPython() {
  final pythonContent = libraryResource('com/mkobit/sharedlib/jenkins-squadcast-notifications.py')
  // There are definitely better ways to do this without having to write to the consumer's workspace
  writeFile(file: 'jenkins-squadcast-notifications.py', text: pythonContent)
  sh('chmod +x jenkins-squadcast-notifications.py && ./jenkins-squadcast-notifications.py')
}