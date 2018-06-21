import os
os.environ["KERAS_BACKEND"] = "theano"

from keras.models import Sequential
from keras.layers import Conv2D # pracowanie na obrazach 2D
from keras.layers import MaxPooling2D # maksymalna wartosc piksela z obrazu
from keras.layers import Flatten # przerabianie obrazu na 1D
from keras.layers import Dense


def cnn(file_name):
# Sequential - siec warstw
#model = Sequential()

# Splot, 32 filtry, kazdy 3x3, macierz filtru mnozy sie przez wycinek obrazu, wynik to srodek wycinka, relu - rectified linear unit, zwraca max(0,x)
#model.add(Conv2D(32, (3, 3), input_shape = (70, 70, 3), activation = 'relu'))

# Warstwa zmieniajaca rozdzielczosc obrazka, z wycinka brana najwieksza wartosc
#model.add(MaxPooling2D(pool_size = (2, 2)))

# Dodatkowe warstwy
#model.add(Conv2D(25, (3, 3), activation = 'relu'))
#model.add(MaxPooling2D(pool_size = (2, 2)))

#model.add(Conv2D(15, (3, 3), activation = 'relu'))
#model.add(MaxPooling2D(pool_size = (2, 2)))

#model.add(Conv2D(5, (3, 3), activation = 'relu'))
#model.add(MaxPooling2D(pool_size = (2, 2)))

# Przeksztalca macierze na wektory
#model.add(Flatten())

# units - liczba wejsc w warstwie, polaczenie warstw, funkcja sigmoid - ksztalt 'S'
#model.add(Dense(units = 32, activation = 'relu'))
#model.add(Dense(units = 1, activation = 'sigmoid'))

# kompilacja, binarny wynik
#model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    from keras.preprocessing.image import ImageDataGenerator
    from keras.models import load_model

    model = load_model('uczenie.h5')
#przeksztalcanie obrazu, scinanie, zoom, obrot
    train_data = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
    test_data = ImageDataGenerator(rescale = 1./255)
# batch - rozmiar partii danyc
    training_set = train_data.flow_from_directory('dataset/train_set', target_size = (70, 70), batch_size = 32, class_mode = 'binary')
    test_set = test_data.flow_from_directory('dataset/test_set',
target_size = (70, 70), batch_size = 32, class_mode = 'binary')
#steps_per_epoch - liczba zdjec w treningu, epoch - kroki, val_steps - liczba zdjec w tescie
    model.fit_generator(training_set, steps_per_epoch = 350, epochs = 3, validation_data = test_set, validation_steps = 231)
#model.save('uczenie.h5')


#przykladowe wejscia
    import numpy as np
    from keras.preprocessing import image

    test1 = image.load_img('file_name', target_size = (70, 70))
    test1 = image.img_to_array(test1)
    test1 = np.expand_dims(test1, axis = 0)
    result = model.predict(test1)
    training_set.class_indices
    if result[0][0] == 1:
        prediction = 'bomb'
        print (prediction)
        return prediction
    else:
        prediction = 'not bomb'
        print (prediction)
        return prediction
