# ethics.py
# Taylor Grant-Knight
# CSCI 77800 Fall 2022
# collaborators: Wei (Amanda) Lee

# Statistics from BuzzFeed News
# https://www.buzzfeednews.com/article/craigsilverman/partisan-fb-pages-analysis

# Outline:
# 1. Method for taking one post and producing retweeted results
#    a. A "post" is a tuple: (x, y) <- Or dictionary?
#         x = -1 left, 0 center, 1 right
#         y = -1 false, 0 mixed or nonfactual, 1 true
#    b. Write a method for one of the three first, then refactor
#    c. Estimate repost rate, create additional posts in a new list
#    d. return the list, append the list to the original set

import random

def new_post():
  # Posts have two attributes: category (left, center, right) and truth (false, mixed/nonfactual, right)
  _category = 0
  _truth = 0

  # Set random values
  category_seed = random.random()
  truth_seed = random.random()
  
  # In the end, our team rated and gathered data on 2,282 posts. 
  # 145 posts from mainstream pages
  # 666 from hyperpartisan right-wing pages
  # 471 from hyperpartisan left-wing pages.
  chance_right = 666 / 2282
  chance_center = 1145 / 2282
  chance_left = 471 / 2282

  # Use chances to produce max range values
  max_left = chance_left
  max_center = max_left + chance_center
  max_right = max_center + chance_right # should be 1

  # Assign category
  if (category_seed < max_left):
    # Left
    _category = -1
  elif category_seed < max_center:
    # Center
    _category = 0
  else:
    # Right
    _category = 1
  
  # Rating by category (False, Mixed, True, Non)
  # center: 0.0, 0.7, 94.8, 4.5 -> Use 0.0, 0.7, 95.5, 100
  # left: 4.7, 14.4, 56.3, 24.6 -> Use 4.7, 19.1, 75.4, 100
  # right: 12.3, 25.4, 47.9, 14.4 -> Use 12.3, 37.7, 85.6, 100
  if _category == 0:
    # Center
    if truth_seed < 0.000: # for completeness, this will never activate
      _truth = -1
    elif truth_seed < 0.007:
      _truth = 0
    elif truth_seed < 0.955:
      _truth = 1
    else:
      _truth = 0
  
  elif _category == -1:
    # Left
    if truth_seed < 0.047:
      _truth = -1
    elif truth_seed < 0.191:
      _truth = 0
    elif truth_seed < 0.754:
      _truth = 1
    else:
      _truth = 0

  else:
    # Right
    if truth_seed < 0.123:
      _truth = -1
    elif truth_seed < 0.377:
      _truth = 0
    elif truth_seed < 0.856:
      _truth = 1
    else:
      _truth = 0
    
  return (_category, _truth)


# parameter: post -> tuple (category, truth)
def generate_reposts(post):
  # Sum of each of the three news sites per category
  left_reposts = 563 + 10931 + 3942
  center_reposts = 13 + 50 + 33
  right_reposts = 92 + 947 + 266

  # Test numbers - DELETE AFTER TESTING
  # left_reposts = 1
  # center_reposts = 2
  # right_reposts = 3

  # determine reposts for this post
  _reposts = 0

  if post[0] == -1:
    _reposts = left_reposts
  elif post[0] == 0:
    _reposts = center_reposts
  else:
    _reposts = right_reposts

  list_reposts = [] # list of new posts

  for i in range(_reposts):
    list_reposts.append(post)

  return list_reposts


def print_stats(post_list):
  truth_stats = [0, 0, 0]
  category_stats = [0, 0, 0]

  for post in post_list:
    if post[0] == -1:
      category_stats[0] += 1
    elif post[0] == 0:
      category_stats[1] += 1
    elif post[0] == 1:
      category_stats[2] += 1

    if post[1] == -1:
      truth_stats[0] += 1
    elif post[1] == 0:
      truth_stats[1] += 1
    elif post[1] == 1:
      truth_stats[2] += 1  

  print( \
    "Left: " + str(category_stats[0]) +" (" + str(round(category_stats[0]/len(post_list)*100,1)) + "%)"\
    + "\nCenter: " + str(category_stats[1]) +" (" + str(round(category_stats[1]/len(post_list)*100,1)) + "%)"\
    + "\nRight: " + str(category_stats[2]) +" (" + str(round(category_stats[2]/len(post_list)*100,1)) + "%)"\
    + "\n"\
    + "\nFalse: " + str(truth_stats[0]) +" (" + str(round(truth_stats[0]/len(post_list)*100,1)) + "%)"\
    + "\nMixed: " + str(truth_stats[1]) +" (" + str(round(truth_stats[1]/len(post_list)*100,1)) + "%)"\
    + "\nTrue: " + str(truth_stats[2]) +" (" + str(round(truth_stats[2]/len(post_list)*100,1)) + "%)"\
  )

# main

# Store all posts and reposts
all_posts = []
all_reposts = []

# Number of fresh posts directly from sites in total
num_posts = 100

for i in range(num_posts):
  post = new_post()
  post_reposts = generate_reposts(post)
  all_posts.append(post)
  all_reposts = all_reposts + post_reposts

combined_posts = all_posts + all_reposts

print("Initial: ")
print_stats(all_posts)
print()
print("Ending: ")
print_stats(combined_posts)