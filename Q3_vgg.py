from tensorflow.keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
import numpy as np
model = VGG16()

print(model.summary())

image = load_img('C:\\Users\\Mahsa\\Downloads\\sandali.jpg', target_size=(224, 224))
image = img_to_array(image)  #output Numpy-array

image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

image = preprocess_input(image)
yhat = model.predict(image)

label = decode_predictions(yhat, top=200)
label = label[0][:]
for i in range(199):
    print( (label[i][1]))

print('%s (%.2f%%)' % (label[0][1], label[0][2]*100))
print('%s (%.2f%%)' % (label[1][1], label[1][2]*100))
print('%s (%.2f%%)' % (label[2][1], label[2][2]*100))



