import numpy as np

# a simple neural network based on the tutorial found at https://www.youtube.com/watch?v=kft1AJ9WVDk

# sigmoid function flattens values to [0, 1]
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# derivative of sigmoid function determines how
# drastic of a readjustment is needed
def sigmoid_derivative(x):
    return x*(1-x)

# the problem: given 3 inputs x1, x2, x3, determine the output based on the table:
#                   x1      x2      x3      y
#   input set 1     0       0       1       0
#   input set 2     1       1       1       1
#   input set 3     1       0       1       1
#   input set 4     0       1       1       1
# possible solution: y = ac ; output is only 1 when both a and c are 1
# possible solution: y = a ; output is only 1 when a is 1

# array containing input problem sets - arr[0] = input set 1, arr[n] = input set n+1
training_inputs = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

# array containing solutions to input problem sets - arr[0] = solution to input set 1, arr[n] = solution to input set n+1
# .t = transpose of array -> the following statement is equivalent to
# training_outputs = np.array([[0], [1], [1], [0]])
# (used to ease creation of array)
training_outputs = np.array([[0,1,1,0]]).T

# used to obtain the same random numbers each time program is run - not strictly necessary
np.random.seed(1)

# initialize synaptic weights to a value in (-1, 1) - multiply by two to get values in (0, 2) and then subtract one to get values in (-1, 1)
# NOTE: initial range values don't necessarily matter - a range of values in (-10, 10) would yield comparable results
# since we have 3x1 inputs, need 3x1 random values
# general form for values in (a, b): (b-a)(random value) + a
synaptic_weights = 2 * np.random.random((3, 1)) - 1

# print starting synaptic weights
print('Random starting synaptic weights: ')
print(synaptic_weights)

# wish to 'train' over 10000 iterations
for i in range(10000):

    # receive input layer variables from training input sets
    input_layer = training_inputs

    # get weighted sum of inputs and process through sigmoid function
    # for this problem, input set 1 = {0, 0, 1} with synaptics_weights = {-0.16, 0.44, -0.99}:
    # output for input set 1 = (0 * -0.16) + (0 * 0.44) + (1 * -0.99)
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    print("Outputs: ")
    print(outputs)

    # error is the trained outputs - example outputs
    error = training_outputs - outputs
    print("Errors: ")
    print(error)

    # want adjustments to be proportional to error - a near 0 error
    # implies an almost perfect solution, therefore no need to change
    adjustments = error * sigmoid_derivative(outputs)

    # the new weights are the inputs multiplied by their adjustments added to the old weights
    synaptic_weights += np.dot(input_layer.T, adjustments)

# final weights after iterations
print('Synaptic weights after training: ')
print(synaptic_weights)

# final outputs after iterations
print('Outputs after training: ')
print(outputs)
