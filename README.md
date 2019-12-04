# Safe Landings In Deep Space

### Disclaimer
This project was conducted for University of Toronto - School of Continuing Studies (SCS) as part of the Intelligent Agents & Reinforcement Learning - 3547 Course.

Submitted By:
- Adnan Lanewala
- Nareshkumar Patel
- Nisarg Patel

## Introduction
### Background
Landing pad is always at coordinates (0,0). Coordinates are the first two numbers in state vector. Reward for moving from the top of the screen to landing pad and zero speed is about 100..140 points. If lander moves away from landing pad it loses reward back. Episode finishes if the lander crashes or comes to rest, receiving additional -100 or +100 points. Each leg ground contact is +10. Firing main engine is -0.3 points each frame. Solved is 200 points. Landing outside landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on its first attempt. Four discrete actions available: do nothing, fire left orientation engine, fire main engine, fire right orientation engine.</br>

### Goal
Navigate a lander to its landing pad safely and have a safe touch down.

## Setup
Libraries Used:
- `Open AI Gym` (v0.15.4) - https://github.com/openai/gym
- `Open AI Box2D-py` (v2.3.8) (Comes with gym) - https://github.com/openai/box2d-py
Anaconda Packages:
- `Swig` (v3.0.12) (Anaconda Package) - https://anaconda.org/anaconda/swig
- `pystan` (v2.19.1.1) (Anaconda Package) - https://anaconda.org/conda-forge/pystan
- `pyglet` (v1.4.8) (Anaconda Package) - https://anaconda.org/conda-forge/pyglet

### Windows Instructions
Install & Setup Microsoft Visual C++ Build Tools for Visual Studio 2019
***
1. Go to https://visualstudio.microsoft.com/downloads/
2. Scroll down to the bottom of the page and click on `Tools for Visual Studio 2019`.
3. Then browse to `Build Tools for Visual Studio 2019` and click on the Download button to download the file.
</br>
Install & Setup SWIG
***
1. Go to http://www.swig.org/download.html to get the latest version of the `SWIG` library or go to https://sourceforge.net/projects/swig/files/swigwin/swigwin-4.0.1/swigwin-4.0.1.zip/download?use_mirror=iweb to download v4.0.1 directly.
2. Make sure to download `swigwin-x.x.x` for windows as indicated by the `win` in the file name. Please note `x` indicates the version number.
3. Open & Extract the `swigwin-4.0.1.zip` folder.
4. Then go to the extracted `swigwin-4.0.1` folder.
5. Make sure there is `swig.exe` file inside the `swigwin-4.0.1` folder.
6. 

## Presentation
- [PDF]()
- [PowerPoint]()
- [YouTube Video]()
