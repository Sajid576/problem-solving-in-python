from selenium import webdriver 
import time
import getpass
import json

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


csv_file="facebook_group_posts.csv"

#group  name -> group URL      
groups={
    "Lets flutter with dart": "https://mbasic.facebook.com/groups/425920117856409",

}
#It is used for logging into the facebook
def login():
    
    try:
        your_email = input("Enter the email address of your facebook ")
        your_password = getpass.getpass("enter the password of your facebook ")
    
        browser.get("https://mbasic.facebook.com")

        email = browser.find_element_by_css_selector("input[name='email']")
        email.send_keys(str(your_email))
        time.sleep(1)

        password = browser.find_element_by_css_selector("input[name='pass']")
        password.send_keys(str(your_password))
        button = browser.find_element_by_css_selector("input[type='submit']")
        button.click()
        time.sleep(2)
        return 1
    except:
        print("Exception occured")
        return 0
    

# This method collects all of the help posts regarding the programming from a facebook programming group 
def getPosts(url):
    posts=[]
    browser.get(url)

    scrolls = 2

    for i in range(0,scrolls):
        
       
        elems = browser.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if("facebook.com/groups/425920117856409/permalink" in str(elem.get_attribute("href"))):
                postUrl=str(elem.get_attribute("href"))
                posts.append({
                    "postUrl":postUrl,
                })
            
            
        # code for scrolling down 
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    
    return posts


if __name__ == "__main__":
    ck=login()
    if(ck==1):#login successful
        for groupname,groupURL in groups.items():
            posts=getPosts(groupURL)
            print (json.dumps(posts, indent=2))
            print("Number of posts: " + str(len(posts)))
    else:
        print("Login failed")
    
