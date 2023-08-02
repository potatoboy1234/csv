# Column to Row Transposer 3000
This script will transpose columns to row values, while keeping the same row ID. 

For example:

|   ID   | Column Value 1 | Column Value 2 | Column Value 3 | Column Value 4 |
|:------:|:--------------:|:--------------:|:--------------:|:--------------:|
|  ABCD  |       1        |       2        |       3        |       4        |
|  EFGH  |       5        |       7        |       8        |       9        |
|  IJKL  |      10        |      11        |      12        |      13        |


will become

|   ID   | Column Value |
|:------:|:------------:|
|  ABCD  |      1       |
|  ABCD  |      2       |
|  ABCD  |      3       |
|  ABCD  |      4       |
|  EFGH  |      5       |
|  EFGH  |      7       |
|  EFGH  |      8       |
|  EFGH  |      9       |
|  IJKL  |     10       |
|  IJKL  |     11       |
|  IJKL  |     12       |
|  IJKL  |     13       |
≠

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- I created this script to enable a CSV importer that couldn't handle multiple columns correctly. Using the script made it possible to import the necessary data faster.
- This script transforms column values into new rows, while keeping the same ID.


## Technologies Used
- Python, imported pandas


## Features
List the ready features here:
- Takes a CSV and transforms columns to new rows according to the column names, sorts by ID.

## Setup
Install python and import pandas.

## Usage
- Set the filepath to your CSV file.
- Set the ID column name.
- Set the column names that you'd liek to transform.
- Run script and it will create a new CSV file with the output.


## Project Status
Project is: complete.


## Room for Improvement

Room for improvement:
- Add UI to select files
- Add UI to select columns
- Add UI settings to control sorting

## Contact
Created by Oleksii Savchuk - feel free to contact me!