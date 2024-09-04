import requests




# 1. Target Resource - Webpage - https://jsonplaceholder.typicode.com/users

def get_other_data():
    pass

def get_user_data(value, key):
    url_of_data_source = f"https://jsonplaceholder.typicode.com/users"
    parameters = {key: value} #dictionary, object

# 2. What we want to do with data at the target resource
    response = requests.get(url_of_data_source, params=parameters)
    response.raise_for_status()

    #3. Getting the data
    data = response.json() # JSON - Javascript Object Notation
    print(data)
    #Response
    #1. Status Code - 200 (OK)
    #2. Data 
    #3. Error. #400, #404 
    #  "username": "Samantha",


def create_new_post(userId, title, body):
    #1. Url https://jsonplaceholder.typicode.com/posts
    #2. Schema Object Structure - UserId, id, title, body - Autoincrementation 
    #3. Write Some Code ;)
    #4. Header Configurations - What time data the request has 
    
    url_of_posts = "https://jsonplaceholder.typicode.com/posts"
    
    new_post = {
        "userId": userId,
        "title": title,
        "body": body
    }
    #images/jpeg
    #videos/mp4
    header_config = {"Content-Type": "application/json"} #MIME Type
    
    response = requests.post(url_of_posts, headers=header_config, json=new_post)
    #Conditionals
    #201 - Succesfully created a object of data
    if response.status_code == 201:
        print("The POST request to add a new post was successful")
    else:
        print("Sorry this request was not able to be handled as requested ")
    
    #Response Status Code
    #2xx - Successful
    #4xx Client Side 
    #5xx Server Issues
    
#updating existing data
def update_post(title_new, body_new, user_id):
    url_of_posts = f"https://jsonplaceholder.typicode.com/posts/{user_id}"
    parameters = {"id": user_id}
     
    update = {
#   "userId": 1,
#   "id": 1,
  "title": title_new,
  "body": body_new
}
    header_config = {"Content-Type": "application/json"} #MIME Type
    response = requests.put(url_of_posts, headers=header_config, json=update, params=parameters)
    
    if response.status_code == 200:
        print("This PUT request to change existing data was successful!")
    else:
        print(response.status_code)
        
def delete_post(id): 
    url_of_posts = f"https://jsonplaceholder.typicode.com/posts/{id}"
    parameters = {"id": id}
    
    response = requests.delete(url_of_posts, params=parameters)
    if response.status_code == 200:
        print("This DELETE request was successful!")
    else:
        print(response.status_code)
    
    


#__REPL__ = dunder
if __name__ == "__main__":
    #   get_user_data("Samantha", "username")
    # create_new_post(1, "How to use APIs", "APIs are the best resource in programming ever! ;)")
    # update_post("APIs are Great", "APIs are even better than I previous mentioned :)", 50)
    delete_post(100)
    #404 - Bad Request
    
    
