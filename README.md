# Rembil - Linux Executable Management Tool
## Overview
 [`Rembil`](https://github.com/HBlackGhost/Rembil.git) is a utility designed for managing executable files on linux systems, offering streamlined installation
and removal processes. By simplifying file copying, permission setting, and symbolic link creation, it enhances
system organization and workflow efficiency. With its intuitive interface, users can seamlessly integrate or
uninstall tools, optimizing their computing environment.
## Features
- Build:  You can build your tool and after building you can run in terminal.
- Remove: Uninstall executable files by removing their directories and associated symbolic links.
- User-friendly interface: Simple command-line interface with clear instructions for building or removing executable files.
## Options 
  -h, --help            show this help message and exit
  
  -m {b,r}              build or remove
  
  -p PATH               The Path Of Tool To Be Builded [For Build]
  
  -d DIRECTORY          The Directory Name of Tool To Be Build [For Build]
  
  -f FILE               The Tool Name File in The Directory [For Build]
  
  -c CALL               The Name Wanted To Call Tool In Terminal [For Build]
  
  -RD REMOVE_DIRECTORY  The Directory Name of Tool To Be Remove [For Remove]
  
  -RF REMOVE_FILE       The Tool File Name in The Directory [For Remove]
  
  -RC REMOVE_CALL       The Call Of Tool Wanted To Remove [For Remove]
## Installation and Running
```bash
 git clone https://github.com/HBlackGhost/Rembil.git
 cd /Downloads/Rembil
 pip3 install -r requirements.txt
 sudo python3 rembil.py [For UI]
```
## Usage And Screenshots
- To build any tool: sudo python3 rembil.py -m b -p [PATH] -d [DIRECTORY] -f [FILE] -c [CALL]
- To remove an tool : sudo python3 rembil.py -m r -RD [REMOVE_DIRECTORY]-RF [REMOVE_FILE] -RC [REMOVE_CALL]
- ### Hint : must be your tool file started with [#!/usr/bin/python3]

 ------------------------------------------------------------------------------------------------------------

  Building Tool To can Run it In Terminal (using one line ):
  
  ![Building Tool To can Run it In Terminal](https://imgur.com/GVZsYQ4.gif)

   Building Tool To can Run it In Terminal (using UI ):

  ![Building Tool To can Run it In Terminal](https://imgur.com/2KJJNZo.gif)

  -----------------------------------------------------------------------------------------------------------
  

  Removing Tool Form Linux And Terminal Too (using one line) :
  
  ![Removing Tool Form Linux And Terminal Too](https://imgur.com/w2An5PT.gif)

  Removing Tool Form Linux And Terminal Too (using UI) :
  
  ![Removing Tool Form Linux And Terminal Too](https://imgur.com/FPtlX7u.gif)

 
  
  
