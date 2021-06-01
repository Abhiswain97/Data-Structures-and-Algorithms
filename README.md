# Data-Structures-and-Algorithms
Implementations of Data Structures and Algorithms in python for self-learning.

# How to run

## Requirements

1. GNU-make
2. python 3.x 

## Steps

1. Clone the repo: 
  ```
  git clone https://github.com/Abhiswain97/Data-Structures-and-Algorithms.git 
  cd Data-Structures-and-Algorithms
  ```
  
> My python interpreter is anaconda-python3.8. So, the instructions here are specific to it. 


2. In the `Makefile` set:
    - `PYTHON = <your anaconda python path>`, it's mostly like `~/anaconda3/envs/<your-env>/python`
    
> If you have python other than anaconda then just specify the path to it in the `PYTHON` variable. 

3. You're now all set, you can simply say:
  ```
  make run FNAME=<path to file you want to run from the repo>
  ```
  This will run it.
  
## Optional settings

1. Activate your conda environemnt and install the requiremnets using: `pip install -r requirements.txt`

2. You can set other variables in `Makefile`:
    - `BLACK = <path to black inside your conda environment>`, it's mostly like `~/anaconda3/envs/<your-env>/Scripts/black`
    - `MYPY = <path to mypy inside your conda environment>`, it's mostly like `~/anaconda3/envs/<your-env>/Scripts/mypy`

3. Now, you can use formatting and type-checking. Do, `make FNAME=<path to file you want to run from the repo>` and now it formats, type-checks and runs it. 

4. You can do specific things also like:
    - `make format FNAME=<path to file you want to run from the repo>`
    - `make type_check FNAME=<path to file you want to run from the repo>`

> I have not added type-hinting to all the files so, the type-cheking is hit or miss currently. But I will add type-hinting to all the files.




