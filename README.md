# **Vamp Escape v2.0**

Video (DEMO): [https://youtu.be/jNQv5P0YVa8](https://youtu.be/jNQv5P0YVa8)

A program made in python that automates the escape process in the game [ROBLOX: Vampire Hunters 3](https://www.roblox.com/games/1240644540/Vampire-Hunters-3). This program only works in the WASD + Space setting and has only been tested on Windows 11 computers with screens with a 1920x1080 resolution.

Table of Contents:
1. Setup
2. Usage
3. Arguments
4. Other Notes


## **Setup:**

### Installing Python
This program requires python version 3.6+ to use. To check your python version, run 
```console 
python --version
``` 
in your terminal/command prompt.

To install python, go to the [download page](https://www.python.org/downloads/) on python.org and download the latest version. Open the application and go through the install process.

To make sure your python installed correctly, run 
```console 
python --version
``` 
 in your terminal/command prompt to check the version. If python is not found follow this [video](https://youtu.be/EU8L9SMH8K0) for intructions.


### Installing the program
To install this program click the green code button and then click `download zip`. Extract the zip contents to wherever you want, just remember the path.

### Installing packages
Before using the program, there are packages that need to be installed. In your terminal/command prompt, navigate to the directory of the program. This could be 
```console
C:\Users\user\Downloads\vampEscapev2
```

Once in the project's directory, run
```console
pip install -r requirements.txt
```
to install all the required packages.

Once this is finished, the install process is complete and ready to use.

## **Usage:**
To use the program, enter the command
```console
python main.py
```
This will lead you to a CLI menu that will first check your monitor size. If you have one monitor, nothing needs to be done, but if you are connected to multiple monitors, you will need to select one (the monitor where you game is). Once that is complete, the program will ask to enable fast mode. By default, regular mode is enabled but is not very efficient and slower than a player. Fast mode is much more efficient but can sometimes have false positives where a button is detected where there is actually none. To enable fast mode, just hit enter when prompted, otherwise input `n` and hit enter to use regular mode.

After the program gives a message to keep the application running in the background, everything is set and the game can be played normally. Whenever the you are escaping from the vampire, the program should automatically do it for you.

## **Arguments:**
When running
```console
python main.py
```
there are arguments that can be given to change the behaviour and look of the program:

1. > --fps or -i

Pass this argument if you want to display the frames per second that the program is rendering. This MUST be used with the `--image` argument.

2. > --image or -i

Pass this argument if you want to display the image that the program is processing. This does not require any other argument. This is for debug purposes and can have impact on the performance.

3. > --verbose or -v

Pass this argument to have the program output some stuff about what button it detects, the FPS or other messages to the console.

4. > --monitor or -m

Pass this argument to choose which display you want to use rather than choosing during when the program is running.
This argument takes **one parameter** which is the *monitor number* that you want to use. Usually this argument would not be used on the first run as you would not know what the monitor numbers are but they are always the same so when the program runs a second time, you can pass this argument to speed up the setup process.


5. > --mode or -fm

Pass this argument to choose whether or not you want to run fast mode. This can also be chosen in the setup menu but this argument is there to speed up the setup process. If you want to use regular mode, that needs to be explicitly said in the setup process.


## **Other Notes:**

This program is still being developed and has only been tested on one screen.

Contact [leekycauldron23@gmail.com](mailto:leekycauldron23@gmail.com) for questions.
