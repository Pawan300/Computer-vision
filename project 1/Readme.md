### This project is basically provide two functions :
  - Invisibilty of a human face from the webcam frames.
  - Social distancing tracking of humans using webcam.

This project using the algorithm implemnted by https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/ for face recognition.

### Problem solve :<br>

### Invisible human :
```
python3 object_tracker.py -p object_detection/deploy.prototxt -m object_detection/model.caffemodel
```

### Social distancing :
```
python3 social_distancing.py -p object_detection/deploy.prototxt -m object_detection/model.caffemodel 
```
