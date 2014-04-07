#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

''' convert .pcss into .css '''
def parse_pcss_to_css():
  
  pcssFileName = sys.argv[1]
  if not pcssFileName.endswith('.pcss'):
    print("Not a pcss file, exiting...")
    return False

  pcssFile = open(pcssFileName, 'r')
  
  cssFileName = pcssFileName[:-5] + '.css'
  cssFile = open(cssFileName, 'w')

  print("Parse " + pcssFileName + " to " + cssFileName)

  try:
    isInBlock = False
    
    for line in pcssFile:
      
      # empty line
      if not line.split(): 
        newLine = '\n'
	if isInBlock:
          print("End the block and add }")
          newLine = '}' + '\n' + '\n'
	  isInBlock = False
          cssFile.write(newLine)
	
      # comment line
      elif line.startswith('#'):
        print("Parse comment line " + line)
        newLine = '/* ' + line[1:-1] +' */' + '\n'			
	
      # selector line
      elif line.split() and not line.startswith(' '):
        print("Start the block of the selector " + line.strip())
        newLine = line.strip() + '{' + '\n'
        isInBlock = True
        cssFile.write(newLine)
        
      # attribute line
      elif line.startswith(' '):
        print("Parse the attribute " + line.strip())
        newLine = '\t' + line.strip() + ';' + '\n'
        cssFile.write(newLine)
        
    if isInBlock:
      print("Write the block in css file")
      newLine = '}' + '\n'
      cssFile.write(newLine)
      
  except IOError as e:
    print("Error occurs when parse .pcss to .css" + e)
  finally:
    pcssFile.close()
    cssFile.close()
    
if __name__ == '__main__':
  parse_pcss_to_css()
