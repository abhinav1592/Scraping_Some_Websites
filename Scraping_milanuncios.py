from urllib.request import Request, urlopen
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re

hor_line = "=============================================="
small_hor_line = "==============="

categories = ["motor","inmobiliaria","ofertas-de-empleo","formacion","servicios",
              "negocios","informatica-segunda-mano","imagen-y-sonido","telefonia",
              "juegos","casa-y-jardin","moda-y-complementos","bebes","aficiones",
              "deportes-nautica","mascotas","comunidad"]

category_names = ["Motor","Inmobiliaria","Empleo","Formacion y libros","Servicios",
                  "Negocios","Informatica","Imagen y Sonido","Telefonia","Juegos",
                  "Casa y Jardin","Moda y complementos","Bebes","Aficiones y ocio",
                  "Deportes y nautica","Mascotas y agricultura","Comunidad"]

base_url = 'https://www.milanuncios.com/'
contact_base_url = 'https://www.milanuncios.com/datos-contacto/?id='
thepage,webpage = None, None

number_of_categories = 0
soup = None
contact_name = None
contact_number = None


for category in categories:
    try:
        f = open(category+".txt", 'a')
        f.write('Category : {}\n'.format(category))
        page_url = base_url + category + "/"
        # print ("Url to be extracted : {}".format(page_url))
        req = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
        # r = requests.get(page_url)
        # print ("Encoding : {}".format(r.encoding))
        webpage = urlopen(req).read()

        # Webpage 
        soup = BeautifulSoup(webpage.decode('ISO-8859-1'),"html.parser")
        print ("Getting all Contacts for Category : {} \n".format(category))
        #print (soup.findAll('div',{"class":"aditem"}))
        main_element = soup.findAll('a',{"class":"highlighted-button"})
        contact_ids = []
        for ele in main_element:
            # print (type(ele))
            #print (str(ele).enc)
            #f = open("temp.html","a")
            #f.write("\n "+hor_line+" \n")
            ##print (ele)
            post_id = str(ele.encode('ISO-8859-1'))
            output = post_id.split()
            y = re.findall('\d+',str(output[2]))
            try:
                print ("\n Advertisement ID : {}\n".format(str(y[0])))
                url_contact_page = contact_base_url + str(y[0])
                req = Request(url_contact_page, headers={'User-Agent': 'Mozilla/5.0'})
                webpage_contact = urlopen(req).read()
                soup_contact_details = BeautifulSoup(webpage_contact.decode('ISO-8859-1'),"html.parser")
                print ("\n Fetching Contact Details : \n")
                # print (str(soup_contact_details ))
                try:
                    # print ("From First Part : ")
                    contact_name_soup = soup_contact_details.find('div',{'class':'texto'})
                    contact_name = str(contact_name_soup.find('strong').text).strip()
                    print ("Contact Name  :{}".format(contact_name))
                    #contact_numbers = contact_name.find('script'})
                    strip_hex = contact_name_soup.find('script').get_text()
                    strip_hex = strip_hex[31:-5]
                    # print (" temp strip_hex : ",strip_hex)
                    strip_hex = strip_hex.replace("%", "\\")
                    data = strip_hex.replace("\\u00", "")
                    #htmlparser = HTMLParser()
                    #strip_hex = htmlparser.unescape(strip_hex)
                    data = ''.join(chr(int(data[i:i+2], 16)) for i in range(0, len(data), 2))
                    #print (" Data : ",data)
                    phone_number = re.findall('\d+',data)
                    #print ("1st strip_hex : ",data)
                    contact_number = phone_number[0]
                    print ("Contact Number : {}".format(contact_number))
                    print ("\n"+small_hor_line+"\n")
                    f.write("\n"+small_hor_line+"\n")
                    f.write(contact_name+" -- "+contact_number)
                    #
                    #strip_hex = strip_hex.replace("%", "\\")
                    # print (" Final : ",(str(strip_hex.decode())))
                except Exception as e2:
                    # print ("From Second Part : ")
                    contact_name_soup = soup_contact_details.find('div',{'class':'nombreTienda'})
                    contact_name = str(contact_name_soup.text).strip()
                    print ("Contact Name  :{}".format(contact_name))
                    contact_numbers = soup_contact_details.find('div',{'class':'telefonotienda'})
                    # print ("Contact Number : ")
                    # print (str(contact_numbers))
                    strip_hex = contact_numbers.find('script').get_text()
                    strip_hex = strip_hex[31:-5]
                    #print (" temp strip_hex : ",strip_hex)
                    strip_hex = strip_hex.replace("%", "\\")
                    data = strip_hex.replace("\\u00", "")
                    #htmlparser = HTMLParser()
                    #strip_hex = htmlparser.unescape(strip_hex)
                    data = ''.join(chr(int(data[i:i+2], 16)) for i in range(0, len(data), 2))
                    #print (" Data : ",data)
                    phone_number = re.findall('\d+',data)
                    #print ("1st strip_hex : ",data)
                    contact_number = phone_number[0]
                    print ("Contact Number : {}".format(contact_number))
                    print ("\n"+small_hor_line+"\n")
                    f.write("\n"+small_hor_line+"\n")
                    f.write(contact_name+" -- "+contact_number)
                    #strip_hex = strip_hex.replace("%", "\\")
                    #htmlparser = HTMLParser()
                    #strip_hex = htmlparser.unescape(strip_hex)
                    #print ("2nd strip_hex : ",strip_hex)
                    # print (" Final : ",(str(strip_hex.decode())))
                #contact_numbers = contact_name.find_all('div',{'class':'telefonos'})
                #print ("Contact Numbers : ")
                #print (str(contact_numbers))
                #for number in contact_numbers:
                #    print (number.find('strong').text)
                print ("\n"+hor_line+"\n")
            except Exception as e1:
                if contact_number is None or contact_name is None :
                    print (" One of the details is missing. This entry will not be created")
                #print ("Contact Page is not available")
                #print (e1)
        # Webpage 
        print ("Getting all <A> elements is complete : \n")
        f.close()
        #number_of_categories += 1
        #if number_of_categories is 1:
        #    break
    except Exception as e:
        f.close()
        print ("Page Can't be opened")
        # print (e)
# f.close()   



#print (soup.title.text)
#f = open("forexpeacearmy.txt","w+")
#for link in soup.findAll('a'):
#    x = link.get('href')
#    y = link.text
#    if "threads/" in str(x) and "/page-" not in str(x):
#        f.write(str(y)+"***"+str(x)+"\n")
#        print (x)
#f.close()
#hor_line = "=============================================="
#small_hor_line = "==============="
#f = open("temp_data.txt","w+")
#a = []
#for x in soup.findAll('li',{'class':'discussionListItem visible '}):
#    # print (hor_line)
#    # print (x)
#    f.write("\n"+hor_line+"\n")
#    div_elements = x.findAll('div')
#    ''' 
#    1. div_elements[0] = Not used
#    2. div_elements[1] = Use first 3 <a> tags
#        1st <a> tag --> URL + Title [Append Full URL in excel sheet
#        2nd <a> tag --> Memeber URL + Memeber Name
#        3nd <a> tag --> Date Posted
#    3. div_elements[2] = Not used
#    4. div_elements[3] = Not used
#    5. div_elements[4] = Not used
#    6. div_elements[5] = Not used
#    7. div_elements[6] = Use to get Reply and View Count
#    8. div_elements[7] =
#        2nd <a> tag --> Memeber URL + Memeber Name
#        3nd <a> tag --> Data Last Replied
    
#    '''
#    # Extracting Data from div_element[1]
#    a_element_links = div_elements[1].findAll("a")
#    # 1st <a> tag
#    get_title_text_of_post = a_element_links[0].text
#    get_url_of_post = a_element_links[0].get("href")
#    f.write("\nTitle : {}".format(str(get_title_text_of_post))+" --> {}"\
#        .format(str(get_url_of_post)))
#    # 2nd <a> tag
#    get_member_posted_by_name = a_element_links[1].text
#    get_member_posted_by_url = a_element_links[1].get("href")
#    f.write("\nMember Name : {}".format(str(get_member_posted_by_name))+" --> {}"\
#        .format(str(get_member_posted_by_url)))
#    # 3rd <a> tag
#    get_time_of_post = a_element_links[2].text
#    if get_time_of_post is None:
#        get_time_of_post = a_element_links[2].text
#    f.write("\nTime_Of_Post : {}".format(str(get_time_of_post)))
    
#    # Extracting Data from div_element[6]
#    dl_elements_links = div_elements[6].findAll("dl")
#    get_reply_count = dl_elements_links[0].text
#    get_view_count = dl_elements_links[1].text
#    f.write("\n Reply: {}".format(str(get_reply_count))+\
#        "\n ViewCount: {}".format(str(get_view_count)))

#    # Extracting Data from div_element[7]
#    a_element_links_last = div_elements[7].findAll("a")
#    last_commented_by_name = a_element_links_last[1].text
#    last_commented_by_url = a_element_links_last[1].get("href")
#    last_commented_time = a_element_links_last[2].text
#    f.write("\n Last Commented On By : {}".format(str(last_commented_by_name))+\
#        "\n Member URL : {}".format(str(last_commented_by_url))+\
#        "\n Time Stamp of Last Comment : {}".format(str(last_commented_time)))




#f.close()