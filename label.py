from openai import OpenAI

def get_sentiment(text: list) -> list:
    
    """
    Examines a list of review on Zico Coconut Water and returns a list of sentiments based on the reviews (positive, negative, neutral or irrelevant)
    
    Args: supplies a list of strings where the reviews are examined to determine postive, negative or neutral reviews
    
    Returns: 
    
    list: supplies a list of sentiments that will denote sentiments of each review (postive, negative, neutralor irrelevant)
    str: If an empty list or list containing an incorrect data-types, will return "Wrong input. text must be an array of strings."
    
    """
    # Will check if an empty string - Error due to Empty List
    if text == []:
        return "Wrong input. text must be an array of strings."
    
    # Will check if list containes an incorrect data-types other than an array of strings - error due to wrong type
    for item in text:
        if not isinstance(item, str):
         return "Wrong input. text must be an array of strings."
    #Note - return text  - did not pass test functionality error due to empty list or wrong type    
     
    system_prompt = """ You are an helpful expert in interpreting human sentiment across cultures to categorize text review into the following sentiment categories: postive, 
    neutral, negative or irrelevant  
    """
    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant:
 
    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
	    { "role": "developer",  "content": system_prompt},
     
        { "role": "user",  "content": prompt}
    ]
)
    # converts strings into a list
    #variable_data = completion.choices[0].message.content.split()
    
    variable_data = completion.choices[0].message.content.strip().split("\n")

    empty_list = []
    for items in variable_data:
        items = items.strip()
        empty_list.append(items)
    return empty_list



