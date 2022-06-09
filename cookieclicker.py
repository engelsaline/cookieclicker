from operator import truediv
from tkinter import FIRST
from selenium import webdriver

import time

class CookieClicker:
    
    def __init__(self):
       self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
       self.SITE_MAP = {
           "buttons": {
               "biscoito":{
                   "xpath": "/html/body/div/div[2]/div[15]/div[8]/button"                                                       
               },
               "upgrade":{
                   "xpath": "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[$$number$$]"                            
               },
               "pt":{
                   "xpath": "/html/body/div[2]/div[2]/div[2]/div/div[11]"
               },
               "clique_em_go_it":{
                   "xpath": "/html/body/div[1]/div/a[1]"
               },
               "label_qtd_cookies":{
                   "xpath": "/html/body/div/div[2]/div[15]/div[4]"
               }
           }
       }

       self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")   
       self.driver.maximize_window()

    def abrir_site(self):
           time.sleep(2)
           self.driver.get(self.SITE_LINK)
           time.sleep(10)

    def clicar_em_pt(self):
           self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["pt"]["xpath"]).click()

    def clique_em_go_it(self):
           self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["clique_em_go_it"]["xpath"]).click()       

    
    def clicar_no_cookei(self):                    
        self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["biscoito"]["xpath"]).click()

    def pega_melhor_upgrade(self):
            encontrei = False  

            elemento_atual = 2 

            while not encontrei:
                objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$number$$" , str(elemento_atual))
                classes_objeto = self.driver.find_element_by_xpath(objeto).get_attribute("class")      

                if not "enabled" in classes_objeto:                    
                    encontrei: True
                    break
                else: 
                    elemento_atual += 1
            
            return  elemento_atual - 1
       
    def comprar_upgrade(self):
           objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$number$$", str(self.pega_melhor_upgrade()))
           self.driver.find_element_by_xpath(objeto).click()

    def recuperarValorDeCookies(self):
            valor_do_campo_cookie = self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["label_qtd_cookies"]["xpath"]).get_attribute("innerHTML")
            return valor_do_campo_cookie

biscoito = CookieClicker()
biscoito.abrir_site()
biscoito.clicar_em_pt()
biscoito.clique_em_go_it()

i = 0
time.sleep(3)
while True:
    if i % 100 == 0 and i != 0:
        time.sleep(1)
        qtd_cookies = biscoito.recuperarValorDeCookies()
        print("o valor de I é ", i)
        print("quantidade de cookies quando cliquei é ", qtd_cookies)
        biscoito.comprar_upgrade()
        time.sleep(1)
    biscoito.clicar_no_cookei()
    i += 1