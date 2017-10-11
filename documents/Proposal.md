# CS6220 Fall 2017 Section 1
# Project Proposal Group 6
## Group member: 
### Aashish Vikram Singh, Saurabh Singh, Luxi Zeng, Kaichen Zhang
## Dataset to be analyzed
In our project, we will implement a simpler version of Facebook friends' recommendation system by using the unsupervised learning method. 

We have 2 datasets, containing different types of info to begin with:
1) Dataset1:   

         | 1 | 2 | \N|
         | 1 | 3 | \N|
         | 1 | 4 | \N|
         | 2 | 5 | \N|
         | 2 | 3 | \N|
        
Each line contains two anonymized user identifiers, showing the second user is accepted by the first as a friend. Finally, the third column is a UNIX timestamp with the time of link establishment (if it could be determined, otherwise it is '\N').

There are two main purposes for this relatively small size of dataset: 
* We will use this dataset to see if there is a strong connection between friends by using the Graph class, and also to determine if the level that we currently reached is far enough. 
* It will be used as a test to see how good our algorithm works before trying on the real one
        
2) Dataset2:  To begin building the dataset, we will use the Facebook Graph API, it is the primary way to get data out of, and put data into, Facebook's platform. It's a low-level HTTP-based API which allows us to get the list of friends along with their features (birthday, education, likes, events user went to, etc.) and then convert the response into json format for future working. 

Due to the rate limitation of Graph API calls, according to the Facebook Graph API documentation: 
> Your app can make 200 calls per hour per user in aggregate. This limit is calculated based on the number of calls made in the previous hour. When your app is rate limited, all calls for the app are limited, not just ones for a specific user.

Here is our preliminary way of approach: for each of our group member, we will randomly pick 15 of friends from our friend list, we call it level 1 friends. And then, for each level 1 friend that we chose, we will extract 25 friends from the list, and we call them level 2 friends. After that, we will do the same thing for each friend on level 2, getting 25 friends out of the list. After that, for each member in our group, we will 9375 various levels of friends to be analyzed. And here is a flowchart to illustrate the idea: 

![friends_node](Friends_node.png)

For each of the friend, we will get the following aspect of information: 
* Birthday (for determine the age range)
* Education history including: name, type, year of attendance and major
* Events interested including: name, location, status(interested/going), start time, end time and description
* Hometown
* Current location
* Employment including: name, location, job title
* Likes: including Facebook pages followed, posts liked/commented, books(read/like), music, athletes
* Photo tags
* Friends that show likes/comments under this friend's post

And for those two datasets, we have created a ipython notebook for data extraction, and we will include more detailed information in the next update. 

## Questions to answer
    
1) a) Recommend friends by number of common friends.
   b) Recommend friends by number of common friends and common features that we have previously extracted
            
       Question to answer: We will compare the result from these two algorithms, to see if the 
       recommendation make a difference
       
2) Exploratory Data Analysis:
       a) How different groups tend to cluster? e.g. In a Karatte-club group, explore the cluster that is formed by the users’ interconnection. How does it look? Are there any obvious grouping between different members?
       b) What are the features that makes a particular user with large number of followers popular?

3) How to validate the recommendation system? 
        We will start with two friends F1 and F2 which we previously know they are friends with each other. Then, we remove friend link between them. Run the recommendation program for User F1 and get rank of F2. Now run the recommendation program for F2 and get rank of F1. An ideal algorithm should suggest F1 to F2 and vice-versa with similar confidence.
        

## Algorithms to apply
1) To Recommend a friend to a user, we can start with FP-growth algorithm from market basket analysis. Transactions here are a list of friends for particular users. We use FP-growth to determine the associations between users and Recommend friends based on that.
2) Recommendation based on number of common friends

## Group work division
1) We will divide the task of building of recommendation system by using different algorithms. 
    This way each of us get to learn the inside out of a particular algorithm and can then share their respective 
    findings with advantages and disadvantages.
    
2) Divide the work of exploratory data analysis. The dataset with this much richness in itself possess a lot of potential for exploratory data analysis. We propose to use NetworkX library of python to do that for starter.
    
3) We propose to use ''GitHub issue resolving feature' to monitor and fix the errors in the code. And we will assign developer the issue online and then the developer would be tasked to fix the same.
