def generate_affiliation_link(url):
    # use '/' to split url 
    item_id = url.split('/')[5]
    return f"http://www.amazon.com/dp/{item_id}/?tag=pyb0f-20"
