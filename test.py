import os
import streamlit as st
import numpy as np
import tensorflow as tf
import keras.utils as image
from cv2 import cv2

st.title("Prediksi Gambar")

loaded_model = tf.keras.models.load_model('CCT')

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Pilih Gambar', filenames)
    return os.path.join(folder_path, selected_filename)

if __name__ == '__main__':
    # Select a file
    st.write("Pilih Gambar.")
    if st.checkbox('Klik untuk memilih'):
        folder_path = st.text_input('Folder Gambar', 'img')
        filename = file_selector(folder_path=folder_path)
        img_name = filename[filename.index('/'):]
        st.write('Anda memilih gambar : `%s`' % img_name[1:])
        st.write('Pilih gambar yang berbeda menggunakan dropdown.')

        image = cv2.imread(filepath)
        blur_image=cv2.medianBlur(image,7)

        grey = cv2.cvtColor(blur_image, cv2.COLOR_BGR2GRAY)

        thresh = cv2.adaptiveThreshold(grey,200,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,41,25)

        contours,hierarchy= cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        preprocessed_digits = []

        # initialize the reverse flag and sort index
        # handle if we need to sort in reverse
        boundingBoxes = [cv2.boundingRect(c) for c in contours]
        (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes),
                                        key=lambda b:b[1][0], reverse=False))


        for c in contours:
            x,y,w,h = cv2.boundingRect(c)

            # Creating a rectangle around the digit in the original image (for displaying the digits fetched via contours)
            cv2.rectangle(blur_image, (x,y), (x+w, y+h), color=(255, 0, 0), thickness=2)

            # Cropping out the digit from the image corresponding to the current contours in the for loop
            digit = thresh[y:y+h, x:x+w]

            # Resizing that digit to (18, 18)
            resized_digit = cv2.resize(digit, (18,18))

            # Padding the digit with 5 pixels of black color (zeros) in each side to finally produce the image of (28, 28)
            padded_digit = np.pad(resized_digit, ((5,5),(5,5)), "constant", constant_values=0)

            # Adding the preprocessed digit to the list of preprocessed digits
            preprocessed_digits.append(padded_digit)

        plt.xticks([])
        plt.yticks([])
        plt.title("Contoured Image",color='red')
        plt.imshow(image, cmap="gray")
        plt.show()

        inp = np.array(preprocessed_digits)
        figr=plt.figure(figsize=(len(inp),4))
        i=1
        alphabets=[]
        for digit in preprocessed_digits:
            [prediction] = model.predict(digit.reshape(1, 28, 28, 1)/255.)
            pred=alpha[np.argmax(prediction)]
            alphabets.append(pred)
            figr.add_subplot(1,len(inp),i)
            i+=1
            plt.xticks([])
            plt.yticks([])
            plt.imshow(digit.reshape(28, 28), cmap="gray")
            plt.title(pred,color='green',fontsize=18,fontweight="bold")
            
        st.write("The Recognized Alphabets are : " ,*alphabets)

        # img = image.load_img(filename)
        # x = image.img_to_array(img)
        # x = np.expand_dims(img, axis=0)

        # st.write(x)

        # st.image(img, caption="Gambar Yang Dipilih")
        
        # output = loaded_model.predict(x)
        
        # st.image(img, caption="Selected image")
        # if(output < 0.5):
        #     st.write("It is a cat.")
        # else:
        #     st.write("It is a dog.")