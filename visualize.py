import matplotlib.pyplot as plt

def make_plot(sentiments: list) -> list:
    
    """
    Examines the list of reviews and plots the amount of each sentiment (`positive`, `neutral`, `negative`, and `irrelevant)
    
    Args: supplies a list of strings(reviews) to determine the number of positive, negative, neutral or irrelevant reviews
    
    Returns: a bar graph with the number of sentiments (positive, negative, neutral or irrelevant ) reviews
    """
    # Counts the number of each sentiment reviews
    
    p_count = sentiments.count('positive')
    neg_count =sentiments.count('negative')
    ne_count = sentiments.count ('neutral')
    irr_count =sentiments.count('irrelevant')
    
    #note - return reviews_count - will cause an error/not show data

    #Colors to coordinate with the reviews
   
    colors = ['red','green', 'grey', 'purple'] 
    
    #Creates the bar graph
    
    fig,ax = plt.subplots()
    ax.bar(["positive","negative", "netural","irrelevant"],[p_count,neg_count,ne_count,irr_count],color = colors)
    
    #sets title, x-axis and y-axis labesl 
    ax.set_title("Sentiment Analysis")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Sentiment Count")
    
    #Saves bar graph as png
    fig.savefig("images/reviews_bar.png")
    
