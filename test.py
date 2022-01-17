import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math
from tensorflow.python.keras.backend import variable
import random

def calculate_RMSE(input_tensor, comparison_array):
    input_array = np.array(input_tensor[0])   
    diff_array1 = (int(input_array[0]) - int(comparison_array[0]))**2 
    diff_array2 = (int(input_array[1]) - int(comparison_array[1]))**2 
    diff_array3 = (int(input_array[2]) - int(comparison_array[2]))**2      
    diff_array = diff_array1 + diff_array2 + diff_array3 
    diff_array = math.sqrt(diff_array)
    return diff_array

def replace_pixel(input_tensor, test_variable):

    output_array = np.zeros(shape=(len(test_variable),1))
    for key in range(len(test_variable)):
        output_array[key] = calculate_RMSE(input_tensor, test_variable[key])
    result = np.where(output_array == np.amin(output_array))
    return test_variable.pop(result[0][0])

input_tensor = tf.constant([[[100, 110, 120]]], dtype=np.uint8)
test_variable = np.array([[[81, 23, 22], [255, 201, 200]], [[124, 66, 65], [155, 97, 96]]], dtype=np.uint8)
test_variable = test_variable.reshape(len(test_variable) + len(test_variable[0]) ,3)
test_variable = test_variable.tolist()
result_Array = np.zeros((len(test_variable),len(test_variable[0]),3), dtype=np.uint8)

#result_Array[0][0] = replace_pixel(input_tensor, test_variable)

tmp2 = replace_pixel(input_tensor[0], test_variable)
print(f"the result of replace pixel is: {tmp2}")

#mask = np.ones((len(test_variable),len(test_variable[0]),1), dtype=np.bool_)


#input_tensor_length = tf.Tensor.get_shape(input_tensor).as_list()
#print(length_filter_image)
#for x_direction in range(length_filter_image[0]):
#    for y_direction in range(length_filter_image[1]):
        #print(x_direction, y_direction)
#        result = replace_pixel(input_tensor, test_variable)
        #print(f"result is {result}")
        #mask[result[0]][result[1]] = False
#        result_Array[x_direction][y_direction] = test_variable[result[0]][result[1]]

