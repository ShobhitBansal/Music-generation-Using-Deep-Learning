# Music Generation Using Deep Learning 

The Music Generation Model is based on Long short-term memory (LSTM), a recurrent neural network (RNN) architecture, that can efficiently learn via gradient descent.

The model is able to generate good quality instrumental music.

WEBSITE LINK: https://music-generation-using-ml.herokuapp.com/

## Installation Documentation

    $ sudo apt install git
    
![](Screenshots/1.png)

    $ git clone https://github.com/ShobhitBansal/Music-generation-Using-Deep-Learning.git
    
![](Screenshots/2.png)
  
    $ cd Music-generation-Using-Deep-Learning

    $ sudo apt-get install virtualenv
    
![](Screenshots/3.png)

    $ virtualenv env

    $ source env/bin/activate
    
![](Screenshots/4.png)
    
    $ sudo apt-get install python3.7
    
    $ sudo apt-get install python3-pip
    
![](Screenshots/5.png)

    $ pip3 install -r requirements.txt
    
![](Screenshots/6.png)
    
    $ cd home/model/
    
    $ wget https://www.dropbox.com/s/nn9975383dee3i6/piano_model.hdf5?dl=0 -O piano_model.hdf5
    
![](Screenshots/7.png)
    
get back to main directory by executing next command 2 times

	  $ cd ..

	  $ cd ..
	  
![](Screenshots/8.png)
    
to launch server execute the following

	  $ python3 app.py
	  
![](Screenshots/9.png)
    
go to Google Chrome and type http://127.0.0.1:5000

![](Screenshots/10.png)
 
## Website Demo
 
Click on the Generate Music button to generate instrumental piano music. The output file will get downloaded as Output.mid. Use any music player to play the music.

![](Screenshots/11.png)
