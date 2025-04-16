from label import get_sentiment
from visualize import make_plot

import json
#url = 'data/raw/reviews.json'

def run(filepath: str):
    """
    Read reviews from a review.json file to access the sentiments and create a visualization
    to express sentiment ratio
    
    Args: Acess the JSON file that contains reviews.
    
    Return: A list of sentiment data contained within the review.json file
    """
    # open the json object
    with open(filepath, 'r') as j:
        reviews = json.load(j)
   
    # extract the reviews from the json file
    #ratio_reviews = reviews.get('results', [])
    ratio_reviews = reviews["results"]
    
    # get a list of sentiments for each line using get_sentiment
    
    sentiments_data = get_sentiment(ratio_reviews)
    
    # plot a visualization expressing sentiment ratio
    make_plot(sentiments_data)
    
    # return sentiments
    return sentiments_data

if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
