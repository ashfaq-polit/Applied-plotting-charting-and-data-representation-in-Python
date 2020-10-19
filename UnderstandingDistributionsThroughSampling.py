
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[ ]:




# In[ ]:




# In[ ]:

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
get_ipython().magic('matplotlib notebook')

fig = plt.figure()
n = 100
bins = 10
gspec = gridspec.GridSpec(2, 2)

upper_right = plt.subplot(gspec[0, 1])
lower_left = plt.subplot(gspec[1, 0])
lower_right = plt.subplot(gspec[1, 1])
upper_left = plt.subplot(gspec[0, 0])


# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 1000)
x2 = np.random.gamma(2, 1.5, 1000)
x3 = np.random.exponential(2, 1000)
x4 = np.random.uniform(14,20, 1000)

# plot the histograms
#plt.figure(figsize=(9,3))
#upper_right.hist(x1, normed=True, bins=20, alpha=0.5)
#lower_left.hist(x2, normed=True, bins=20, alpha=0.5)
#lower_right.hist(x3, normed=True, bins=20, alpha=0.5)
#upper_left.hist(x4, normed=True, bins=20, alpha=0.5);
#plt.axis([-7,21,0,0.6])

def update(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    if curr == n: 
        a.event_source.stop()
    plt.cla()
    upper_left.hist(x4[:curr], bins=bins)
    upper_right.hist(x1[:curr], bins=bins)
    lower_left.hist(x2[:curr], bins=bins)
    lower_right.hist(x3[:curr], bins=bins)
    #plt.axis([-4,4,0,30])
    plt.annotate('n = {}'.format(curr), [3,27])
    
a = animation.FuncAnimation(fig, update, interval=10)
plt.gca().set_title('Sampling the Normal Distribution')
plt.gca().set_ylabel('Frequency')
plt.gca().set_xlabel('Value')


# In[ ]:



