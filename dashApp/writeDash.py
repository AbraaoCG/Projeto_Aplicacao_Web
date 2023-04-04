from convertDash import writeLayout
import subprocess

InputFilename = '../assets/index.html'
OutPutFilename = '../assets/dashCode.py'
writeLayout(InputFilename= InputFilename, OutPutFilename= OutPutFilename)

subprocess.call(f'black {OutPutFilename}')
