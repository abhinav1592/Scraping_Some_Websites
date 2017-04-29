# Scraping_Some_Websites
Lately I have been into scraping some websites. Beautiful Soup and Requests and PyQtGUI Python framework are used.

Following is the list of websites I have scraped. Each of the following in the list contains my experience towards that:

1. https://www.newegg.com & www.dell.com/support/home/us/en/04/product-support/servicetag/ : 
   It has three options: Dell, PC and MAC.
   You can enter Dell Service Tag number and it will fetch you Laptop model name and based on that we fetch the rest of details from newengg.com.
   If you select PC option: Then you can enter any model name and on that we fetch the rest of details from newengg.com.
   Learning: When you inject a model name into a search parameter you replace all the spaces with '+' character. MAC option doesn't work because site I used get everymac.com has started putting catpcha.
   Code can be found here: https://github.com/abhinav1592/Scraping_Some_Websites/blob/master/Demo_Scraping_Dell_CNET_NEW_EGG.py

   Demo: https://drive.google.com/open?id=0B_RInj9RyqrhZnJ0OHlrZ0QtSVE
   
2. https://www.milanuncios.com/: It's an advertisement site for Cars and other vehicles.       
   The script extracts all the names and contacts from 10-15 categories.
   Learning: Want to know what's in the pop up? Check out the REST calls. Also, this website gave me pretty hard time with respect to encoding
   it follows.

   Code can be found here: https://github.com/abhinav1592/Scraping_Some_Websites/blob/master/Scraping_milanuncios.py 

   Demo: https://drive.google.com/open?id=0B_RInj9RyqrhbWtBbHM2bGs3Uk0

3. http://www.forexpeacearmy.com/: This where scams are posted regularly. It's an awareness site.
   My script extracts all the 30 posts per page with all the details.
   Code can be found here: https://github.com/abhinav1592/Scraping_Some_Websites/blob/master/scrape_forexpeacearmy.py
   
================================================

Will keep on adding more as I go..
   
