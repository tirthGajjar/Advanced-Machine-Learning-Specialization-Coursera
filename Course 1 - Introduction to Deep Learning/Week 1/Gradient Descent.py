import numpy as np


def batch_gradient_descent(model, eta, max_iterations=1e4, epsilon=1e-5, weights_start=None):
    """
    Batch Gradient Descent
    ============================================================
    Parameters::
    ````````````````````````````````````````````````````````````
    + model           :   optimization model object
                          model contains two objects
                            1. Data
                            2. Gradient Function to be applied (loss function)
    + eta             :   learning rate
    + max_iterations  :   maximum number of gradient iterations
    + epsilon         :   tolerance for stopping condition
    + weights_start   :   where to start (otherwise random)

    Output::
    ````````````````````````````````````````````````````````````
    + trained_weights	:   final weights value
    + weights_history   :   weight values from each iteration
    
    References:
    ````````````````````````````````````````````````````````````
    Code reference		:	https://github.com/idc9/optimization_algos/blob/master/opt_algos/gradient_descent.py
    Numpy Linalg Norm		:	https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.linalg.norm.html
    GD stopping Condition	:	https://stats.stackexchange.com/questions/33136/how-to-define-the-termination-condition-for-gradient-descent
    """

	# Get data and Gradient function from the model
	# Example: For Least Squares loss function, gradient_of_loss_function is = np.dot(self.X.T, np.dot(self.X, beta) - self.y)
	gradient_of_loss_function = model.gradient_of_loss_function
	data = model.data
	# Check if initial weights are given, otherwise generate random weights
	if weights_start:
		weights_current = weights_start
	else:
		weights_current = np.random.normal(loc=0, scale=1, size=data)

	# Keep track of how weights are changing over iterations
	weights_history = []

	for iterator in range(int(max_iterations):

		weights_history.append(weights_current)

		# Update the gradient as per the formula or gradient descent
		weights_next = weights_current - eta * gradient_of_loss_function(weights_current)

		# If relative error is smaller than the epsilon then break the iterations
		# Stop when the improvement drops below the tolerance threshold
		# We have taken Frobenius norm here
		if np.linalg.norm(wieghts_next - weights_current) <= epsilon * np.linalg.norm(weights_current):
			break;

		weights_next=weights_current

	print('Gradient Descent finished after' + str(iterator) + 'iterations')

	return {
		'trained_weights': weights_current,
		'weights_history': weights_history
	}
