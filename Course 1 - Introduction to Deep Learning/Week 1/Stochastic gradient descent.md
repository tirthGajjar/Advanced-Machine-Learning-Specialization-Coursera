# Gradient Descent

Watch below videos to learn about Gradient Descent and Cost functions with intuition

>[Lecture 2.2 — Linear Regression With One Variable | CostFunction](https://www.youtube.com/watch?v=yuH4iRcggMw)  
>[Lecture 2.3 — Linear Regression With One Variable | Cost Function Intuition #1](https://www.youtube.com/watch?v=yR2ipCoFvNo)  
>[Lecture 2.4 — Linear Regression With One Variable | Cost Function Intuition #2](https://www.youtube.com/watch?v=0kns1gXLYg4&index=7&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)  
>[Lecture 2.5 — Linear Regression With One Variable | Gradient Descent](https://www.youtube.com/watch?v=F6GSRDoB-Cg&index=8&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)  
>[Lecture 2.6 — Linear Regression With One Variable | Gradient Descent Intuition](https://www.youtube.com/watch?v=YovTqTY-PYY&index=9&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)  
>[Lecture 2.7 — Linear Regression With One Variable | Gradient Descent For Linear Regression](https://www.youtube.com/watch?v=GtSf2T6Co80&index=10&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)  

Notes created by me for the same topic can be found [here](https://github.com/tirthGajjar/Advanced-Machine-Learning-Specialization-Coursera/blob/Course-1-Week-1/Course%201%20-%20Introduction%20to%20Deep%20Learning/Week%201/Gradient%20Descent%20and%20Cost%20function.pdf).  

## loss functions
1. Cross-Entropy  
2. Hinge
3. Huber
4. Kullback-Leibler
5. MAE (L1)
6. MSE (L2)


# Stochastic gradient descent

In gradient descent, a batch is the total number of examples you use to calculate the gradient in a single iteration. So far, we've assumed that the batch has been the entire data set. When working at Google scale, data sets often contain billions or even hundreds of billions of examples. Furthermore, Google data sets often contain huge numbers of features. Consequently, a batch can be enormous. A very large batch may cause even a single iteration to take a very long time to compute.

A large data set with randomly sampled examples probably contains redundant data. In fact, redundancy becomes more likely as the batch size grows. Some redundancy can be useful to smooth out noisy gradients, but enormous batches tend not to carry much more predictive value than large batches.

What if we could get the right gradient on average for much less computation? By choosing examples at random from our data set, we could estimate (albeit, noisily) a big average from a much smaller one. Stochastic gradient descent (SGD) takes this idea to the extreme--it uses only a single example (a batch size of 1) per iteration. Given enough iterations, SGD works but is very noisy. The term "stochastic" indicates that the one example comprising each batch is chosen at random.

Mini-batch stochastic gradient descent (mini-batch SGD) is a compromise between full-batch iteration and SGD. A mini-batch is typically between 10 and 1,000 examples, chosen at random. Mini-batch SGD reduces the amount of noise in SGD but is still more efficient than full-batch.

To simplify the explanation, we focused on gradient descent for a single feature. Rest assured that gradient descent also works on feature sets that contain multiple features.


# An Overview of Gradient Descent Optimization Algorithms
### Gradient descent optimization algorithms  
 1. Momentum
 2. Nesterov’s Accelerated Gradient
 3. Adagrad
 4. RMSprop
 5. Adadelta
 6. Adam
 7. Adamax
 8. Nadam
 

## References 
- [Reducing Loss: Stochastic Gradient Descent](https://developers.google.com/machine-learning/crash-course/reducing-loss/stochastic-gradient-descent)
- [Stochastic Gradient Descent with momentum](https://towardsdatascience.com/stochastic-gradient-descent-with-momentum-a84097641a5d)


# TO-DO
Read below articles  
https://distill.pub/2017/momentum/  
http://ruder.io/deep-learning-optimization-2017/index.html  
http://cs231n.github.io/neural-networks-3/  
https://www.youtube.com/playlist?list=PLtmWHNX-gukIc92m1K0P6bIOnZb-mg0hY  
https://pdfs.semanticscholar.org/e2dc/8810671f76927d862e63faa29c401bdec5da.pdf  