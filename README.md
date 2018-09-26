# Postfiles
This is very simplified version of my lsshipper 
I have two goals in this project:
* make everything simple as possible
* change destination to logstash as http but not tcp socket as before


# What is this
this python module will upload files that pass regex test line by line to logstash http endpoint. 

# Why not filebeat
filebeat is great but I have application that writes logs in a littlebit strange format. This app allocates 
about 100Kb at the end of text file and then fills it after that it will allocate new 100Kb and again fill it with data. 
I think this is done for prevent fragmentation on windows servers. 

# How does this will work
I will do all the job by process pool and I will try to make whole project without dependencies. So you will need to download zip file and run it with python -m postfiles 
Info about processed files will be saved in json file at the moment when file is finished or program was terminated. 

# Todo:
* ~~function to get line by line from files according to main goal(remember 100Kb?)~~
* ~~function that will return all files that fit to passed regex~~
* ~~save and load file data to know what files already aploaded~~
* ~~catch ctrl+c if someone will stop program~~
* connection to http endpoint using certificates
* put everything together
* make zip module that can be used without install on windows/linux environment
