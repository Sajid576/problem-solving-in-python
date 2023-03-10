from selenium import webdriver 
import time
import getpass

#this code used to read the comment text from comment.txt
final_comments = []
with open('comment.txt',encoding="utf8") as comment:
    comments = comment.readline()
    final_comments.append(comments)


'''  this function used to fetch url of recent posts of a friend timeline  
     url="url of a friend's timeline"
'''
def getAllpostURLs(url):
    postUrls=[]

    your_email = input("Enter the email address of your facebook ")
    your_password = getpass.getpass("enter the password of your facebook ")
    browser = webdriver.Chrome()
    browser.get("https://mbasic.facebook.com")
    

    email = browser.find_element_by_css_selector("input[name='email']")
    email.send_keys(str(your_email))
    time.sleep(1)

    password = browser.find_element_by_css_selector("input[name='pass']")
    password.send_keys(str(your_password))
    button = browser.find_element_by_css_selector("input[type='submit']")
    button.click()
    time.sleep(2)

    browser.get(url)

    time.sleep(2)
    scrolls = 2

    for i in range(0,scrolls):
        
        next_page_elem=""
        elems = browser.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if("#footer_action_list" in str(elem.get_attribute("href"))):
                postUrls.append(str(elem.get_attribute("href")))
                print("post url:      "+elem.get_attribute("href"))
                print('\n')
            if("/profile/timeline/stream/?cursor" in str(elem.get_attribute("href"))):
                next_page_elem=str(elem.get_attribute("href"))
                print("Next page reference:  "+next_page_elem)
        # code for scrolling down 
        #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("see more pressed")
        browser.get(next_page_elem)
        time.sleep(3)

    
    return postUrls,browser


'''this method used to do comment on fetched postUrls of friend's timeline'''
def auto_comment(striped_comment,postUrls,browser):
    

    for i in range(0,len(postUrls)):
        browser.get(postUrls[i])

        for sc in striped_comment:
            cb = browser.find_element_by_css_selector("textarea[name='comment_text']")
            cb.send_keys(sc)

            button = browser.find_element_by_css_selector("input[type='submit']")
            button.click()

            time.sleep(2)
            print(f'{sc} comment is done !!')


if __name__ == "__main__":
    
    postUrls,browser= getAllpostURLs('https://mbasic.facebook.com/NishanPauL007MLF')
    auto_comment(final_comments,postUrls,browser)
