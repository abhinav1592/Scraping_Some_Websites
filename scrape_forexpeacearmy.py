from urllib.request import Request, urlopen
from bs4 import BeautifulSoup



theurl = 'http://www.forexpeacearmy.com/community/forums/scam-alerts.30/page-2'
thepage,webpage = None, None
try:
    req = Request(theurl, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
except Exception as e:
    print ("Page Can't be opened")
    print (e)

soup = BeautifulSoup(webpage,"html.parser")

#print (soup.title.text)
#f = open("forexpeacearmy.txt","w+")
#for link in soup.findAll('a'):
#    x = link.get('href')
#    y = link.text
#    if "threads/" in str(x) and "/page-" not in str(x):
#        f.write(str(y)+"***"+str(x)+"\n")
#        print (x)
#f.close()
hor_line = "=============================================="
small_hor_line = "==============="
f = open("temp_data.txt","w+")
a = []
for x in soup.findAll('li',{'class':'discussionListItem visible '}):
    # print (hor_line)
    # print (x)
    f.write("\n"+hor_line+"\n")
    div_elements = x.findAll('div')
    ''' 
    1. div_elements[0] = Not used
    2. div_elements[1] = Use first 3 <a> tags
        1st <a> tag --> URL + Title [Append Full URL in excel sheet
        2nd <a> tag --> Memeber URL + Memeber Name
        3nd <a> tag --> Date Posted
    3. div_elements[2] = Not used
    4. div_elements[3] = Not used
    5. div_elements[4] = Not used
    6. div_elements[5] = Not used
    7. div_elements[6] = Use to get Reply and View Count
    8. div_elements[7] =
        2nd <a> tag --> Memeber URL + Memeber Name
        3nd <a> tag --> Data Last Replied
    
    '''
    # Extracting Data from div_element[1]
    a_element_links = div_elements[1].findAll("a")
    # 1st <a> tag
    get_title_text_of_post = a_element_links[0].text
    get_url_of_post = a_element_links[0].get("href")
    f.write("\nTitle : {}".format(str(get_title_text_of_post))+" --> {}"\
        .format(str(get_url_of_post)))
    # 2nd <a> tag
    get_member_posted_by_name = a_element_links[1].text
    get_member_posted_by_url = a_element_links[1].get("href")
    f.write("\nMember Name : {}".format(str(get_member_posted_by_name))+" --> {}"\
        .format(str(get_member_posted_by_url)))
    # 3rd <a> tag
    get_time_of_post = a_element_links[2].text
    if get_time_of_post is None:
        get_time_of_post = a_element_links[2].text
    f.write("\nTime_Of_Post : {}".format(str(get_time_of_post)))
    
    # Extracting Data from div_element[6]
    dl_elements_links = div_elements[6].findAll("dl")
    get_reply_count = dl_elements_links[0].text
    get_view_count = dl_elements_links[1].text
    f.write("\n Reply: {}".format(str(get_reply_count))+\
        "\n ViewCount: {}".format(str(get_view_count)))

    # Extracting Data from div_element[7]
    a_element_links_last = div_elements[7].findAll("a")
    last_commented_by_name = a_element_links_last[1].text
    last_commented_by_url = a_element_links_last[1].get("href")
    last_commented_time = a_element_links_last[2].text
    f.write("\n Last Commented On By : {}".format(str(last_commented_by_name))+\
        "\n Member URL : {}".format(str(last_commented_by_url))+\
        "\n Time Stamp of Last Comment : {}".format(str(last_commented_time)))




f.close()