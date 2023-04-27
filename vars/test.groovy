def runMyPython() {
  final pythonContent = libraryResource('com/mkobit/sharedlib/test.py')
  // There are definitely better ways to do this without having to write to the consumer's workspace
  writeFile(file: 'test.py', text: pythonContent)
  sh('chmod +x test.py && ./test.py')
}