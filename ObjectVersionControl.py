import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import MySQLdb

# options and image read/cast credit https://github.com/markjay4k/YOLO-series/blob/master/part2%20-%20Processing%20Images%20with%20YOLO%20and%20openCV.ipynb


options = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolo.weights',
    'threshold': 0.3,
    'gpu': 1.0
}

tfnet = TFNet(options)


# read the color image and covert to RGB

img = cv2.imread('Samplesetup2.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# use YOLO to predict the image
results = tfnet.return_predict(img)

img.shape
# pull out some info from the results

for result in results:
    tl = (result['topleft']['x'], result['topleft']['y'])
    br = (result['bottomright']['x'], result['bottomright']['y'])
    label = result['label']
    print(result['label'] + " confidence: " + str(result['confidence']))

    # add the box and label and display it
    img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
    img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

plt.imshow(img)
plt.show()