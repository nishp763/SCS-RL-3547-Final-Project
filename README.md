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
- `Swig` (v3.0.12) (Anaconda Package) - https://anaconda.org/anaconda/swig
- `pystan` (v2.19.1.1) (Anaconda Package) - https://anaconda.org/conda-forge/pystan
- 
### Windows

### Mac OSX

## Presentation
- [PDF]()
- [PowerPoint]()
- [YouTube Video]()
