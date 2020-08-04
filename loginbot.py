from selenium import webdriver
from time import sleep
from passwords import *

class InstaBot:
    def __init__(self,instausername,instapw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input").send_keys(instausername)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input").send_keys(instapw)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button").click()

    def inslogin(self):
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        print("Select the account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:DeviantArt\n5:KupujemProdajem\n6:Exit")
        choice = int(input("For which account you need to login:"))

class FbBot:
    def __init__(self,fbusername,fbpw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://facebook.com")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input").send_keys(fbusername)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(fbpw)

    def fblogin(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input").click()
        print("Select the account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:DeviantArt\n5:KupujemProdajem\n6:Exit")
        choice = int(input("For which account you need to login:"))

class TwitterBot:
    def __init__(self,twitterusername,twitterpw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://twitter.com/login")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input").send_keys(twitterusername)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input").send_keys(twitterpw)

    def twlogin(self):
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div").click()
        print("Select the account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:DeviantArt\n5:KupujemProdajem\n6:Exit")
        choice = int(input("For which account you need to login:"))
        
class GithubBot:
    def __init__(self,githubusername,githubpw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://github.com/login")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]").send_keys(githubusername)
        self.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]").send_keys(githubpw)

    def ghlogin(self):
        self.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]").click()
        print("Select the account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:DeviantArt\n5:KupujemProdajem\n6:Exit")
        choice = int(input("For which account you need to login:"))
        
class DeviantArtBot:
    def __init__(self,githubusername,githubpw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.deviantart.com/users/login")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[1]/form/div[1]/div/div[1]/input").send_keys(devartusername)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[1]/form/div[2]/div/div[1]/input").send_keys(devartpw)

    def devlogin(self):
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[1]/form/div[3]/button").click()
        print("Select the account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:DeviantArt\n5:KupujemProdajem\n6:Exit")
        choice = int(input("For which account you need to login:"))

class KupujemProdajemBot:
    def __init__(self,kupujemprodajemusername,kupujemprodajempw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.kupujemprodajem.com/login")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/main/div/div[7]/form/div/div[1]/input").send_keys(kupujemprodajemusername)
        self.driver.find_element_by_xpath("//html/body/main/div/div[7]/form/div/div[2]/div[1]/input").send_keys(kupujemprodajempw)

    def kplogin(self):
        self.driver.find_element_by_xpath("/html/body/main/div/div[7]/form/div/button").click()
        print("Select the account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:DeviantArt\n5:KupujemProdajem\n6:Exit")
        choice = int(input("For which account you need to login:"))

print("********************Welcome To The AppBot!********************")
print("Select the account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:DeviantArt\n5:KupujemProdajem\n6:Exit")
choice = int(input("For which account you need to login:"))

if choice==0:
    mybot = InstaBot(instausername,instapw)
    mybot.inslogin()

elif choice==1:
    mybot = FbBot(fbusername,fbpw)
    mybot.fblogin()

elif choice==2:
    mybot = TwitterBot(twitterusername,twitterpw)
    mybot.twlogin()

elif choice==3:
    mybot = GithubBot(githubusername,githubpw)
    mybot.ghlogin()

elif choice==4:
    mybot = DeviantArtBot(devartusername,devartpw)
    mybot.devlogin()

elif choice==5:
    mybot = KupujemProdajemBot(kupujemprodajemusername,kupujemprodajempw)
    mybot.kplogin()
else:
    print("Select the account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:DeviantArt\n5:KupujemProdajem\n6:Exit")
    choice = int(input("For which account you need to login:"))
if choice==0:
    mybot = InstaBot(instausername,instapw)
    mybot.inslogin()

elif choice==1:
    mybot = FbBot(fbusername,fbpw)
    mybot.fblogin()

elif choice==2:
    mybot = TwitterBot(twitterusername,twitterpw)
    mybot.twlogin()

elif choice==3:
    mybot = GithubBot(githubusername,githubpw)
    mybot.ghlogin()

elif choice==4:
    mybot = DeviantArtBot(devartusername,devartpw)
    mybot.devlogin()

elif choice==5:
    mybot = KupujemProdajemBot(kupujemprodajemusername,kupujemprodajempw)
    mybot.kplogin()
else:
    pass
    

