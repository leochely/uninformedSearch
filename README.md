# uninformedSearch
CSCI 404 Project 1  
(This file is saved as .txt to comply with the project requirements but is written in Markdown. It can be previewed with https://markdownlivepreview.com/ for an easier lecture)

## 1. Names and CWID
Leo Chely, 10818125  
David An, 10727498

## 2. Programming Language
Python 3

## 3. OS
Code was written on Mac and Windows 10, but should be OS-independent (it just requires Pyhton 3.x to be installed). Since it is a Python program, it does not need to be compiled.

## 4. Code Structure
First, the program reads the input file and stores the data in a dictionary of dictionaries: the keys of the dictonary are cities' names, and tthe inner dictionaries are other city names and the indexes/values 
are the associated distances between them. That way, the distance between any city can be retried with `graph[city1][city2]` (or `graph[city2][city1]`, both are equivalent). The program then performs a 
uniformed search while recording the origin city of all the visited city. When the destination city is reached, the program back tracks the cities that led to the destination. These cities are then stored 
in a list that is reversed before being printed.

## 5. How to run
The program does not need to be compiled. Cd into the directory and run the following command:

`python3 main.py input_file origin_city destination_city`

On the school computers or on Windows machine in general when using git bash, `python3` has to be replaced by `python`  




