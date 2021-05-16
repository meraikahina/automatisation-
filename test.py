from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/opt/apps/chromedriver")

driver = webdriver.Chrome('./chromedriver')



#aviguer sur l url http://shop.demoqa.com/

driver.get("http://shop.demoqa.com")

#Choisir n importe quel article et le selectionner.
driver.find_element_by_xpath("//*[contains(text(),'Black Cross Back Maxi Dress')]").click()

#Choisir une option couleur (Color) et une option taille (Size)
driver.find_element_by_xpath("//select[@name='attribute_pa_color']/option[@value='black']").click()
driver.find_element_by_xpath("//select[@name='attribute_pa_size']/option[@value='medium']").click()

# Cliquer sur le bouton ADDTO CART
driver.find_element_by_xpath("//*[contains(text(),'Add to cart')]").click()


#Un message de succes doit s afficher
message_alert = driver.find_element_by_xpath("//div[@class='woocommerce-message']")
#assert "“Black Cross Back Maxi Dress” has been added to your cart.".__eq__(message_alert)

#Cliquer ensuite sur le bouton \«View cart\»
driver.find_element_by_xpath("//a[contains(text(),'View cart')]").click()

#L’article doit se rajouter dans le panier, et le total de prix doit s’afficher dans le panier en haut.
cart_count = driver.find_element_by_xpath("//span[@class='cart-count']")
cart_total = driver.find_element_by_xpath("//span[@class='woocommerce-Price-currencySymbol']")
#assert cart_count.text == "1"
#assert cart_total.text == "20.00"

#Cliquer sur le bouton «Proceed to checkout»-Unformulaire de payement doit s’afficher
driver.find_element_by_xpath("//*[contains(text(),'Proceed to checkout')]").click()

time.sleep(2)
#Remplir tous les champs obligatoires du formulaire à savoir le nom, le prénom, le pays, l’adresse,
# le numéro de téléphone, l’adresse mail,
first_name = driver.find_element_by_id("billing_first_name")
first_name.clear()
first_name.send_keys("kahina")

last_name = driver.find_element_by_id("billing_last_name")
last_name.clear()
last_name.send_keys("merai")

driver.find_element_by_xpath("//select[@name='billing_country']/option[@value='FR']").click()

address = driver.find_element_by_id("billing_address_1")
address.clear()
address.send_keys("6 rue aime morot")

code_postale = driver.find_element_by_id("billing_postcode")
code_postale.send_keys("75013")

city = driver.find_element_by_id("billing_city")
city.send_keys("PARIS")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("0780868082")

email = driver.find_element_by_id("billing_email")
email.send_keys("kahina.merai@email.com")

#et cocher la case «I HAVE READ AND AGREE TO THE WEBSITETERMS AND CONDITIONS»
time.sleep(2)
terms = driver.find_element_by_id("terms")
terms.click()

#Cliquer ensuite sur le bouton «PLACE ORDER»
driver.find_element_by_id("place_order").click()

# Un message de succès doit s’afficher avec les détails de la commande d’achat.
thankyou = driver.find_element_by_xpath("//*[@class='woocommerce-thankyou-order-received']")
assert thankyou.text == 'Thank you. Your order has been received.'


time.sleep(3)
driver.close()

