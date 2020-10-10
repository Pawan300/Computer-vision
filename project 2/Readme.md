### Problem statement is: <br>
- I need to create a mask for an car and change background into black.

<br>
I used Masked RCNN for this task becuase it helps us to consider localization and also create segmentation of an image which help us to get mask from the data points.

* Results I get using this approach is : <br>
  
   * For Muliple cars :<br>
     <img src="/project%202/results/mulitple%20cars.png" alt="different angle" width=500px height=100px/>
   
   * For cars with different colors :<br>
     <img src="/project%202/results/different%20color.png" alt="different angle" width=500px height=400px/>
   
   * For different angle of cars :<br><br>
     <img src="/project%202/results/different%20angle.png" alt="different angle" width=500px height=400px/>
      
* Now other objective is to find out car which we want to use instead of all of the cars which is in the frame :<br>
  Example : <br><br>
  <img src="/project%202/results/input.jpeg" alt="input" width=500px height=400px/>
  <br>
  Here we want to show only black car and we need to hide all of the remaining cars.
  
  So Masked RCNN output conatins :
  ```
    result[0].keys()
    >>> dict_keys(['rois', 'class_ids', 'scores', 'masks'])
  ```
  
  * I tried :
    - To fetch the object which is car and have maximum ROI's area in the image.
    - To fetch the object which is car and have maximum sum of the masks.
    
  * Result I get is :<br>
    <img src="/project%202/results/highlighted%20car.jpeg" alt="input" width=500px height=400px/>
