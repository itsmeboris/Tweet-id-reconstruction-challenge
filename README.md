# Tweet-id-reconstruction-challenge
## Tweet id reconstruction challenge
### Data challenge
In this challange I will try to  reconstruct and acquire information from twitter only using tweet ids. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.  

### Prerequisites
* Python 3

## Deployment
* Configure config.py
> I have used 4 files, you can use as many as you like  
> If you want to use other machine ids than the ones I used, change them in the file also
* To Run on the application: 
> python parse_input.py

## output  
This will output several files:  
### output.json
* Will have an entry per file, each entry will contain the total percentage per machine and sequence id  
filtered by the machine_ids specified in config.py
### seq-busiest_filename.json
* This will have absolute percentage per file of all the sequence ids
### machine-busiest_filename.json
* This will have absolute percentage per file of all the machine ids

## Authors

* **Boris Sobol**
