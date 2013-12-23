PyCss
=====

## Introduction
PyCss (or Pythonic Cascading Style Sheet) is a project to write css file in pythonic way. As we all know, the structure of css file is extremely simple. Furthermore, Python’s syntax is expressive and needs less to write. So why don’t we write css file in pythonic syntax for not only conveniene but also readability? That’s why PyCss comes out.

So I invent a brandnew file type, pcss, which is quite similary with css. However, it’s much simpler, more readable and pythonic. All selectors should occupy one single line and their attributes should be written below with representative tab, just like how Python does. Moreover, there is no colon after the selector because we don’t need it, neither does semicolon after attributes.

After we write the pcss file, we can simpliy convert it into css file with the same file name tool, pycss.py. Here is the source code of pycss1.0. It’s written in Python and you can use it under GNU Publish Lisence.

Finally, I gonna to show you the difference between ordinary css file and the new pcss file. It’s quite simple, isn’t it?

## Implement 
* detect whether input parameter is pcss file or not
* convert into css file with the same file name in the same directory
* translate Python comment into Css comment
* replace all braces with representative tab
* remove all semicolon at the end of each line
* add close brace in a new line even if EOF is the last line of attribute
* keep all the empty lines
* produce css file with readable tab as well

## Screenshot
![css_pcss screenshot](https://raw.github.com/tobegit3hub/PyCss/master/screenshot/css_pcss.png)
