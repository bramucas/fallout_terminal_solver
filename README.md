# Fallout Terminal solver

This simple tool is intended to help the user find the terminal solution in the Fallout videogame series. This is not a mod for the game, it is an external software written in python.

You can use it manually adding words in the list or you can use text recognition with ocr technology to get words directly from an screenshot. 

**Recognition utility is under development and may not work properly**.

### Dependencies

**For using simple utility**:
 * [Python GTK+ 3](https://python-gtk-3-tutorial.readthedocs.io/en/latest/)

**For using OCR utility**:
 * [Tesseract ocr](https://github.com/tesseract-ocr/tesseract) in the path
 * [Pillow](https://pillow.readthedocs.io/en/latest/) - ```easy_installation Pillow```
 * [pyocr](https://github.com/openpaperwork/pyocr) - ```pip3 install pyocr```


### Running

```bash
python run.py
```

### How to use

**Manual use**: [video](https://youtu.be/jEZdpVqFKcI)

 * First add all the words you see in the terminal.
 * Select a word on the terminal and see what happens.
 * Select the word on the program list, write number of matches and click on 'Comprobar'.
 * Repeat until you succed.
 * Remember to clean the list before you start with the next terminal.

**Text recognition**: [video](https://www.youtube.com/watch?v=K-eglpT50m8)

 * Select 'Clean and get words from an image'
 * Select an screenshot for scan
 * Wait a moment.
 * A dialog may appear showing words that weren't recognized properly
 * Solve the terminal

 ### Future work

  * Fix recognition problems
  
- - -
[![twitter][1.1]][1]     [![github][2.2]][2]

[1]:https://twitter.com/b_munizcastro
[1.1]:https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/twitter-24.png

[2]:https://github.com/bramucas
[2.2]:https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-24.png
