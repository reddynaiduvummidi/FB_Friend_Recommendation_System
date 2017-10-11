# CS6220 Fall 2017 Section 1
# Project Proposal Group 6
## Group member: 
### Aashish Vikram Singh, Saurabh Singh, Luxi Zeng, Kaichen Zhang
## Dataset to be analyzed
In our project, we will implement a simpler version of Facebook friends' recommendation system by using the unsupervised learning method. 

We have 2 datasets, containing different type of info to begin with:
1) Dataset1:   

         | 1 | 2 | \N|
         | 1 | 3 | \N|
         | 1 | 4 | \N|
         | 2 | 5 | \N|
         | 2 | 3 | \N|
        
        Each line contains two anonymized user identifiers, meaning the second user appeared in the first user's friend list. Finally, the third column is a UNIX timestamp with the time of link establishment (if it could be determined, otherwise it is '\N').
        
2) Dataset2:  To begin building the dataset, we will use the Facebook Graph API, it is the primary way to get data out of, and put data into, Facebook's platform. It's a low-level HTTP-based API which allows us to get the list of friends along with their features (birthday, education, likes, events user went to, etc) and then convert the response into json format for future working. 

Due to the rate limitation of Graph API calls, according to the Facebook Graph API documentation: 
> Your app can make 200 calls per hour per user in aggregate. This limit is calculated based on the number of calls made in the previous hour. When your app is rate limited, all calls for the app are limited, not just ones for a specific user.

Here is our preliminary way of approach: for each of our group member, we will randomly pick 15 of friends from our friend list, we call it level 1 friends. And then, for each level 1 friend that we chose, we will extract 25 friennds from the list, and we call them level 2 friends. After that, we will do the same thing for each friend on level 2, getting 25 freinds out of the list. After that, for each member in our group, we will 9375 various levels of friends to be analyzed. For each of friend, we will get the following aspect of information

![friends_node](Friends_node.png)
## Questions to answer

    1) a) Recommend friend by no. of common friends.
       b) Recommend friend by no. of common friends and common feautres (likes, events)
       
       Question to ask: Does the algorithm makes a difference?
       
    2) Exploratory Data Analysis:
       a) How different groups tend to cluster? e.g In a Karatte-club group, explore the cluster that is formed by the users interconnection. How does it look? Are there any obvious grouping between different members?
       b) What are the features that makes a particular user with large number of followers popular?

    3) How good is my Recommendation? 
        To solve this problem, start with two friends F1 and F2. Remove friend link between them. Run the recommendation program for User F1 and get rank of F2. Now run the recommendation program for F2 and get rank of F1. Does these make sense? An ideal algorithm should suggest F1 to F2 and vice-versa with equal confidence.
        

## Algorithms to apply

    1) To Recommend a friend to a user, we can start with FP-growth algorithm from market basket analysis. Transactions here are a list of friends for particular users. We use FP-growth to determine the associations between users and Recommend friends based on that.
    2) Recommendation based on no. of common friends

## Group work division
    1) Divide the task of building of recommendation system using different algorithms. 
    This way each of us get to learn the inside out of a particular algorithm and can then share thier respective 
    findings with advantages and disadvantages.
    
    2) Divide the work of exploratory data analysis. The dataset with this much richness in itself possess a 
    lot of potential for exploratory data analysis. We propose to use NetworkX library of python to do that for starter.
    
    3) We propose to use 'github issue resolving feature' to monitor and fix the errors in the code. 
    Assign developer the issue online and then the developer would be tasked to fix the same.
