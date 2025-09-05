# WindowsTerminalReflector
Reflects your 2nd monitor (can be set with -m) to the windows CMD


## How do I use this?

- Have latest python version (https://www.python.org/)
- Using VSCode or running in the CMD
- Running Main.exe in the CMD

### Running in the VSCode terminal:

- Click the triangle near the top right corner of the screen.
* Done!

### Running with the EXE:

- Open the windows CMD (Win+R, type "cmd")
- Type "cd C:\Your\Path\Here" - (For example, downloads would be: C:\Users\Admin\Downloads\
                                                                            ^ this would be changed if you have a dif username for ur PC

- Next, type "main.exe"
* Done!


## Help! It wont work!

- Do you have a second monitor?
  No) Run "main.exe -m 1" << Im using the VSCode terminal! -- Click the up arrow key and type " -m 1"
  Yes) ↓↓↓
- Did you install pillow and mss?
  No) Run "pip install mss pillow"
  Yes) Make an issue request and I will gladly help!



# Extra commands:
- "-m" will set the monitor that you want to use to mirror (**DEFAULT IS SET AS THE SECOND MONITOR!**)
- "-i" will set how fast the program grabs the screen (**DEFAULT IS SET AS ONE SECOND!**)
