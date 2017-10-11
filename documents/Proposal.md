# CS6220 Fall 2017 Section 1
# Project Proposal Group 6
## Group member: 
### Aashish Vikram Singh, Saurabh Singh, Luxi Zeng, Kaichen Zhang
## Dataset to be analyzed
In our project, we will implement a simpler version of Facebook friends' recommendation system by using the unsupervised learning method. 

To begin building the dataset, we will use the Facebook Graph API, it is the primary way to get data out of, and put data into, Facebook's platform. It's a low-level HTTP-based API which allows us to get the list of friends along with their features and then convert the response into json format for future working. 

Due to the rate limitation of Graph API calls, according to the Facebook Graph API documentation: 
> Your app can make 200 calls per hour per user in aggregate. This limit is calculated based on the number of calls made in the previous hour. When your app is rate limited, all calls for the app are limited, not just ones for a specific user.

Here is our preliminary way of approach: for each of our group member (as level 0 friends),  we will randomly pick 15 of friends from our friend list, we call it level 1 friends. And then, for each level 1 friend that we chose, we will extract 25 friennds from the list, and we call them level 2 friends. After that, we will do the same thing for each friend on level 2, getting 25 freinds out of the list. After that, for each member in our group, we will 9375 various levels of friends to be analyzed, which gives us in total of 37500 friends in the dataset. The following flow chart help illustrate the procedure: 

![friends_node](Friends_node.png)

Furthermore, for each of friend stored in the dataset, we will extract the following aspect of information:
* Education history (school/institute/college/university they went to, major and year of attendence)
* Employment history
* Age range
* Common friends 
## Questions to answer

## Algorithms to apply

## Group work division
