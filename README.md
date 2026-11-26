# File Handling
- Read and write from and into files on local filesystem.  
- Must open first, then close when done
    - OS needs to allocate resources
    - Exclusive lock on the file
    - Track position in the file - read sequentially

## Demo: Terminal App
- An app that manages and analyzes Euro cup match data. And its going to have a number of features:
Load match data from a json file
    - Display all match data
    - Add a new match 
    - Calculate and display total goals
    - Filter and display high-scoring matches
    - Save match data to a json file 
    - Error handling for user input and file ops
