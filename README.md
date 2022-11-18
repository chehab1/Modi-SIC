# MODI-SIC ASSEMBLER

The Modi-SIC assembler has the same set of instructions (Format 3) and concept of memory variable reserve as the SIC. Additionally, it supports Format 1 instructions as well as Immediate Instructions (Format 3), which deal with an immediate value given as an integer.


## Project Idea 
It reads an assembly program written in Modi-Sic as input in the form of a text file (in.txt). 
[InputFile](https://github.com/chehab1/Modi-SIC/blob/main/rsc/inputs/in.txt)

It generates five files, and set them in the folder "generated files".
    
    intermediate.txt (Parsed input without code lines and comments) 
    location_counter.txt
    symbol tabkle.txt
    out pass2.txt
    HTE.txt

## Project Criteria
The only thing you need to do when writing your inputs is to use a tab separator between one column from another.

## How to run the project?
1.  you need to install pyhton
2.  Install pandas by running this command
    
        pip install pandas
3.  put your input in this file [InputFile](https://github.com/chehab1/Modi-SIC/blob/main/rsc/inputs/in.txt)
4.  run the project by running this command 
        
        python main.py
        
## License
####  MIT License        
