import numpy as np


def stochastic_gradient_descent(model, eta, bacth_size, max_iterations=1e4, epsilon=1e-5, weights_start=None):
    """
    Mini-Batch (Stochastic) Gradient Descent
    ==============================================================================
    Parameters::
    ``````````````````````````````````````````````````````````````````````````````
    + model           :   optimization model object
                          model contains two objects
                            1. Data
                            2. Gradient Function to be applied (loss function)
    + eta             :   learning rate
    + max_iterations  :   maximum number of gradient iterations
    + epsilon         :   tolerance for stopping condition
    + batch_size      :   mini-batch size (if equal to one, it is Stochastic gradient descent)
    + weights_start   :   where to start (otherwise random)

    Output::
    ``````````````````````````````````````````````````````````````````````````````
    + trained_weights    :   final weights value
    + weights_history    :   weight values from each iteration

    References:
    ``````````````````````````````````````````````````````````````````````````````
    Code reference           :    https://github.com/idc9/optimization_algos/blob/master/opt_algos/gradient_descent.py
    Numpy Linalg Norm        :    https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.linalg.norm.html
    GD stopping Condition    :    https://stats.stackexchange.com/questions/33136/how-to-define-the-termination-condition-for-gradient-descent
    """

    # Get data and Gradient function from the model
    # Example: For Least Squares loss function, gradient_of_loss_function is = np.dot(self.X.T, np.dot(self.X, beta) - self.y)
    gradient_of_loss_function = model.gradient_of_loss_function
    n = model.n  # number of data points
    d = model.d  # number of varaibles

    # Check if initial weights are given, otherwise generate random weights
    if weights_start:
        weights_current = weights_start
    else:
        weights_current = np.random.normal(loc=0, scale=1, size=data)

    # Keep track of how weights are changing over iterations
    weights_history = []

    for iterator in range(int(max_iterations)):

        weights_history.append(weights_current)

        # Generate batch_size random numbers between 0 to number of samples to be used as indexes
        indexes=np.random.choice(n, bacth_size)

        # Calculate gradient value using the randomly choosen weight elements
        batch_grad=np.mean([grad_f(weights_current, i) for i in indexes], axis=0)

        # Update the gradient as per the formula or gradient descent
        weights_next=weights_current - eta * batch_grad

        # If relative error is smaller than the epsilon then break the iterations
        # Stop when the improvement drops below the tolerance threshold
        # We have taken Frobenius norm here (Default for np.linalg.norm)
        if np.linalg.norm(wieghts_next - weights_current) <= epsilon * np.linalg.norm(weights_current):
            break;

        weights_next=weights_current

    print('Stochastic Gradient Descent finished after' + str(iterator) + 'iterations')

    return {
        'trained_weights': weights_current,
        'weights_history': weights_history
    }
