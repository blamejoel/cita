# Cat in the Act
![cat in the act twitter](https://github.com/jgome043/cita/blob/images/images/cita_twitter.png?raw=true "Cat in the Act Twitter")  

## What it is
Cat in the act is a pet disciplinary aid that aims to keep your pets off of 
your counters or other places they're not supposed to be!

## Why we made it
We came up with this project as a 
[submission for Hack Poly 2016](https://devpost.com/software/cat-in-the-act). 
The idea was conceived and completed entirely within a span of 12 hours, on 
location at Hack Poly 2016.  
  
We wanted to create something useful, and one of us had new cat that had a 
habit of jumping onto counters that he wasn't allowed on for his own safety.

## How it works
Cat in the act uses a PIR sensor to activate a web cam that is connected to an 
UDOO Neo (an embedded Linux board). Once activated, the camera takes an image 
of the environment within the view area and uses the 
[Clarifai image recognition API](https://developer.clarifai.com/) to determine 
if there is a cat within the frame. If a cat is detected, a high-frequency tone 
within the audible range of cats, but outside of the audible range for humans 
is emitted to deter the pet away from the area. Additionally, a tweet is posted 
from the official 
[Cat_in_the_act Twitter account](https://twitter.com/cat_in_the_act) to 
broadcast the violation.

## How we made it
We used an UDOO Neo board as our CPU. A PIR sensor and piezo is wired to the 
Cortex-M4 Core and communicted over an internal serial bus to the Cortex-A9 
Core. We created a Python script to control the webcam, interface with the 
Clarifai API, and post a tweet using a custom [IFTTT](https://ifttt.com) recipe.
  
## Known issues
We were able to complete a basic "proof of concept", but alas there were still
some areas left in need of improvement by the end of the hackathon.
Particularly:  
  
* Better camera solution for fast-moving subjects
  
