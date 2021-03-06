
# CrickFev  

> A command line tool to see cricket updates.   

![demo](https://user-images.githubusercontent.com/23627932/33074597-bbee674e-ceec-11e7-9a65-eeb610668d71.gif)  


Why?
----

Mr.X loves to do stuffs in terminal and he is die-hard fan of Cricket.  

Some times due to work, he can not see full live match on screen, so whenever he wants to see score he has to open browser.  

What about a CLI app which will give you update of matches.  


Features
--------

* See live and upcoming events of cricket  
* See scores of all live match  
* See full score-card of a particular match  

How to use?
-----------

To use, it is recommended to make `virtualenv` and then install all required packages:

* Installing virtualenv:  
```
$ sudo pip install virtualenv
```  
* Making virtualenv:  
```
$ virtualenv venv
```  
* Go to your CrickFev dir and activate it:   
```
$ . venv/bin/activate
```  
* To install all required packages:  
 ```
 $ pip install --editable .
 or
 $ sudo pip install --editable .
```

**Note** `$` means commands should be entered in **Terminal**  



Usage
-----

   | Commands |  Description |
   | --- | --- |
   | levent | See live and upcoming events of cricket |
   | lscore | See scores of all live matches |
   | lscore --ch=[OPTION] | See scores of particular event related live match ( [OPTION]  stands for event number ) |
   | lscorecard --em [OPT1] [OPT2] | See full score-card of a particular match ( [OPT1] for event number and [OPT2] for match number ) |  
   
  



      
      
      
    
    





