import networkx as nx
import matplotlib.pyplot as plt
import operator
import random

# Create a practice graph
practice_graph = nx.Graph()

# add the node in the practice graph
practice_graph.add_node("A")
practice_graph.add_node("B")
practice_graph.add_node("C")
practice_graph.add_node("D")
practice_graph.add_node("E")
practice_graph.add_node("F")

# add the edge in the practice graph
practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "E")
practice_graph.add_edge("D", "F")

def draw_practice_graph():
    """Draw practice_graph to the screen."""
    nx.draw(practice_graph)
    plt.show()

# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
# draw_practice_graph()

# Create the Romeo-Juliet graph
rj = nx.Graph()

# add the node in the Romeo-Juliet graph
rj.add_node("Nurse")
rj.add_node("Juliet")
rj.add_node("Capulet")
rj.add_node("Tybalt")
rj.add_node("Romeo")
rj.add_node("Friar Laurence")
rj.add_node("Benvolio")
rj.add_node("Montague")
rj.add_node("Escalus")
rj.add_node("Mercutio")
rj.add_node("Paris")

# add the edge in the Romeo-Juliet graph
rj.add_edge("Nurse", "Juliet")
rj.add_edge("Juliet", "Tybalt")
rj.add_edge("Juliet", "Friar Laurence")
rj.add_edge("Juliet", "Romeo")
rj.add_edge("Juliet", "Capulet")
rj.add_edge("Capulet", "Tybalt")
rj.add_edge("Capulet", "Escalus")
rj.add_edge("Capulet", "Paris")
rj.add_edge("Paris", "Escalus")
rj.add_edge("Paris", "Mercutio")
rj.add_edge("Escalus", "Mercutio")
rj.add_edge("Escalus", "Montague")
rj.add_edge("Mercutio", "Romeo")
rj.add_edge("Romeo", "Montague")
rj.add_edge("Montague", "Benvolio")
rj.add_edge("Romeo", "Benvolio")
rj.add_edge("Romeo", "Friar Laurence")

def draw_rj():
    """Draw the rj graph to the screen and to a file."""
    nx.draw(rj)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
# draw_rj()

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    The parameter 'user' is the string name of a person in the graph.
    """
    return set(graph.neighbors(user))

def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given graph.
    The result does not include the given user nor any of that user's friends.
    """
    f_list = set()

    friend_list = friends(graph,user)

    for friend in friend_list:
        f_list.update(set(friends(graph,friend)))

    for friend in friend_list:
        f_list.discard(friend)

    f_list.remove(user)

    return f_list

def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common."""
    friend_set_1 = friends(graph,user1)
    friend_set_2 = friends(graph,user2)

    return (friend_set_1 & friend_set_2)

def number_of_common_friends_map(graph, user):
    """Returns a map from each user U to the number of friends U has in common with the given user.
    The map keys are the users who have at least one friend in common with the
    given user, and are neither the given user nor one of the given user's friends.
    Take a graph G for example:
        - A and B have two friends in common
        - A and C have one friend in common
        - A and D have one friend in common
        - A and E have no friends in common
        - A is friends with D
    number_of_common_friends_map(G, "A")  =>   { 'B':2, 'C':1 }
    """
    number_common = dict()

    friend_list = friends_of_friends(graph,user)

    for friend in friend_list:
        number_common[str(friend)] = len(common_friends(graph,str(friend),user))

    return number_common

def number_map_to_sorted_list(map):
    """Given a map whose values are numbers, return a list of the keys.
    The keys are sorted by the number they map to, from greatest to least.
    When two keys map to the same number, the keys are sorted by their
    natural sort order, from least to greatest."""
    number = []
    res = sorted(map.items(), key=lambda x: (-x[1], x[0]))
    for item in res:
        number.append(item[0])

    return number

def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names of people in the graph
    who are not yet a friend of the given user.
    The order of the list is determined by the number of common friends.
    """
    common_friends = number_of_common_friends_map(graph,user)
    return number_map_to_sorted_list(common_friends)

def influence_map(graph, user):
    """Returns a map from each user U to the friend influence, with respect to the given user.
    The map only contains users who have at least one friend in common with U,
    and are neither U nor one of U's friends.
    See the assignment for the definition of friend influence.
    """
    fre_of_fre = friends_of_friends(graph,user)

    com_fre = dict()
    influence = dict()

    for friend in fre_of_fre:
        com_fre[str(friend)] = common_friends(graph,friend,user)

    for friend,common_friend in com_fre.items():
        count = 0 
        for item in common_friend: 
            count = count + 1/len(friends(graph,item))
        influence[str(friend)] = count

    return influence

def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names of people in the graph
    who are not yet a friend of the given user.
    The order of the list is determined by the influence measurement.
    """
    friends_influence = influence_map(graph,user)
    res = number_map_to_sorted_list(friends_influence)

    return res

unchanged = []
changed = []

for friend in rj.nodes():
    res_influence = recommend_by_influence(rj, friend)
    res_number = recommend_by_number_of_common_friends(rj,friend)

    if (res_influence == res_number):
        unchanged.append(friend)
    else:
        changed.append(friend)

def evaluate_recommendation(graph):
    number_index = []
    influence_index = []

    for i in range(100):
        # 1. Randomly choose a real friend connection; call the two friends F1 and F2.
        friendship_chosen = random.choice(graph.edges())
        friend1 = friendship_chosen[0]
        friend2 = friendship_chosen[1]

        # 2. Remove their friendship from the graph.
        graph.remove_edge(friend1,friend2)

        '''
        3. Compute friend recommendations for F1 and F2.
        4. Determine the rank of F1 in F2's list of recommended friends.
            Determine the rank of F2 in F1's list of recommended friends.
            If either of these does not exist (e.g., F1 is not recommended as one of F2's friends), discard the F1-F2 pair from your experiment.
            Otherwise, average these two numbers.
            The "rank" is also known as the "index" or "position". It starts counting at 1, not 0.
        '''
        if ((len(graph.neighbors(friend1)) == 0) or (len(graph.neighbors(friend2)) == 0)):
            pass
        else:
            f1_rec_number = recommend_by_number_of_common_friends(graph,friend1)

            f2_rec_number = recommend_by_number_of_common_friends(graph,friend2)
        
            f1_rec_influence = recommend_by_influence(graph,friend1)

            f2_rec_influence = recommend_by_influence(graph,friend2)

            if ((friend2 not in f1_rec_number) or (friend1 not in f2_rec_number) or (friend2 not in f1_rec_influence) or (friend1 not in f2_rec_influence)):
                pass
            else:
                # recommend friend by the number of common friends
                index_number_f1= f1_rec_number.index(friend2) + 1
                number_index.append(index_number_f1)

                index_number_f2= f2_rec_number.index(friend1) + 1
                number_index.append(index_number_f2)
               
                # recommend friend by friends' influence
                index_influence_f1 = f1_rec_influence.index(friend2) + 1
                influence_index.append(index_influence_f1)

                index_influence_f2 = f2_rec_influence.index(friend1) + 1
                influence_index.append(index_influence_f2)

        #5. Put their friendship back in the graph.
        graph.add_edge(friend1,friend2)
            
    sum_influence_index = 0
    for i in range(len(influence_index)):
        sum_influence_index += influence_index[i]
    avg_influence = sum_influence_index / len(influence_index)
    print("Average rank of influence method:", avg_influence)

    # calculate the average of number of common friends
    sum_number_index = 0
    for i in range(len(number_index)):
        sum_number_index += number_index[i]
    avg_number = sum_number_index/len(number_index)  
    print ("Average rank of number of friends in common method:", avg_number)

    # compare two methods
    if (avg_influence < avg_number):
        print ("recommend by influence is better")
    else:
        print ("recommend by number of friends in common method is better")

evaluate_recommendation(rj)

'''Create a graph named facebook from the Facebook data in file facebook-links.txt. 
As above, use the Graph class.'''

facebook = nx.Graph()

'''File facebook-links.txt contains a list of all of the user-to-user links from the Facebook New Orleans networks. 
These links are undirected on Facebook.

Format: Each line contains two numeric user identifiers, 
meaning the second user appeared in the first user's friend list, 
and the first user appeared in the second user's friend list. 
Finally, the third column is a UNIX timestamp with the time of link establishment 
(if it could be determined, otherwise it is unavailable).'''

with open ("facebook-links.txt","r") as file:
    content = file.readlines()
for i in range(len(content)):
    point1 = content[i].split("\t")[0]
    if point1 not in facebook:
        facebook.add_node(point1)

    point2 = content[i].split("\t")[1]
    if point2 not in facebook:
        facebook.add_node(point2)
    facebook.add_edge(point1,point2)

def draw_facebook_graph():
    '''Draw facebook to the screen.'''
    nx.draw(facebook)
    plt.show()

# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
# draw_facebook_graph()

'''
For every Facebook user with an id that is a multiple of 1000, 
print a list containing the first 10 friend recommendations, 
as determined by number of common friends. 
If there are fewer than 10 recommendations, 
print all the recommendations.
'''
rec_num_of_friends = []
for i in range(len(facebook.nodes())):
    if ((i%1000 == 0) and (str(i) in facebook)):
        rec_num_of_friends.append(recommend_by_number_of_common_friends(facebook,str(i))[:10])

'''
For every Facebook user with an id that is a multiple of 1000, 
print a list containing the first 10 friend recommendations, 
as determined by influence score. 
If there are fewer than 10 recommendations, 
print all the recommendations.
'''
rec_influence = []
for i in range(len(facebook.nodes())):
    if ((i%1000 == 0) and (str(i) in facebook)):
        rec_influence.append(recommend_by_influence(facebook,str(i))[:10])

'''
Considering only those 63 Facebook users with an id that is a multiple of 1000, 
compute and print the number of Facebook users who have the same first 10 friend recommendations,
and the number of Facebook users who have different first 10 friend recommendations under the two recommendations
'''
unchanged = 0
changed = 0
for i in range(len(rec_influence)):
    if (rec_num_of_friends[i] == rec_influence[i]):
        unchanged += 1
    else:
        changed += 1
print ("Same:",unchanged,"Different:",changed)

'''
Present the average index for each recommendation system. 
State which recommendation system is better for the facebook graph.
'''
evaluate_recommendation(facebook)