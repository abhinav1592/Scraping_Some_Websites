
hor_line = "=============================================="
small_hor_line = "==============="

from PyQt4 import QtCore, QtGui
from urllib.request import Request, urlopen
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re
import requests


combo_text = ""
search_text = ""
class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None,combo_text="",search_text=""):
        super(MyDialog, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        #self.combo_box_selection = self.comboBox.currentText()
        #self.passed_string = self.lineedit.text()
        self.textBrowser = QtGui.QTextBrowser(self)
        #print ("Combo Box : "+self.comboBox.currentText())
        #print ("Text Box : "+self.lineedit.text())
        #self.textBrowser.append("Combo Box : "+combo_text)
        #self.textBrowser.append("Text to be search : "+search_text)
        # Fetch details from passed string
        print ("Reached here")
        self.prod_url = ""
        if "Dell" == combo_text:
            print ("Inside If statement!")
            page_url = "https://www.dell.com/support/home/us/en/04/product-support/servicetag/"+str(search_text)+"/configuration"
            print ("Url to be extracted : {}".format(page_url))
            req = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
            #r = requests.get(page_url)
            #print ("Encoding : {}".format(r.encoding))
            webpage = urlopen(req).read()
            # Webpage 
            soup = BeautifulSoup(webpage.decode('utf-8'),"html.parser")
            getting_table = soup.find("table", {"class":"table table-striped"})
            #print ("getting_table:  "+str(getting_table))
            getting_all_tr_from_table = getting_table.findAll("tr")
            #print ("getting_all_tr_from_table:  "+str(getting_all_tr_from_table))
            get_all_td_from_tr = getting_table.findAll("td")
            #print ("get_all_td_from_tr:  "+str(get_all_td_from_tr))
            self.model_name = (str(get_all_td_from_tr[3].text)).strip().replace(" ", "+")
            print ("Model Name : "+self.model_name)
            self.prod_url = self.get_product_url(self.model_name)
        elif "PC"== combo_text:
            search_text = search_text.replace(" ", "+")
            self.prod_url = self.get_product_url(search_text)
        self.processor_info = ""
        self.processor_info = self.get_processor_info(self.prod_url)
        #main_element = soup.findAll('a',{"class":"highlighted-button"})
        self.textBrowser.append("Processor Info for this model : "+str(self.processor_info))
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.buttonBox)

    def get_product_url(self,model_name):
        print ("Getting Product URL information from model name({})...".format(model_name))
        google_search_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description="+model_name+"&N=-1&isNodeId=1"
        print ("URL to be searched: "+google_search_url)
        req = Request(google_search_url, headers={'User-Agent': 'Mozilla/5.0'})
        r1 = requests.get(google_search_url)
        encoding = r1.encoding
        print ("Encoding : {}".format(encoding))
        print ("r1 : "+str(r1))
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage.decode(encoding),"html.parser")
        #print (str(soup.encode(encoding)))
        prod_url = soup.find("div",{"class":"items-view is-grid"}).find("a").get("href")
        print ("Product URL : ",str(prod_url))
        return str(prod_url)
        #for a in get_div_0_tag:
        #    print ("\n : ",str(a.encode(encoding)))
        #    #if "cnet" in str(a.get("data-href")):
            #    print ("CNET Link : ",a.get("data-href"))
            #    break
    def get_processor_info(self,product_url):
        self.info = []
        print ("Getting Processor information from Product URL({})...".format(product_url))
        google_search_url = product_url
        print ("URL to be searched: "+product_url)
        req = Request(google_search_url, headers={'User-Agent': 'Mozilla/5.0'})
        r1 = requests.get(google_search_url)
        encoding = r1.encoding
        print ("Encoding : {}".format(encoding))
        print ("r1 : "+str(r1))
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage.decode(encoding),"html.parser")
        #print (str(soup.encode(encoding)))
        div_info = soup.find("div",{"id":"Specs"})
        fieldset_info = div_info.findAll("fieldset")
        one_time = False
        for f in fieldset_info:
            if one_time is False:
                one_time = True
            else:
                #print ("fieldset_info : ",str(f.encode(encoding)))
                for dl in f.findAll("dl"):
                    #for dd in dl.find("dd"):
                    #print ("Infor: ",str(dl.encode(encoding)))
                    dd_tag = dl.findAll("dd")
                    self.ctr = 0
                    
                    for dd in dd_tag:
                        s_string = str(dd.encode(encoding))
                        s_string = s_string [6:-6]
                        self.info.append(str(s_string))
                        print ("str(s_string)  : ",str(s_string))
                    #info = ''.join(info)
                    #print ("Info: ",info[0:4])
                    #return info
                    break
        for i in self.info:
           print ("i: ",i)
        return self.info[1]
                   

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.pushButtonWindow = QtGui.QPushButton(self)
        # Category
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("Dell")
        self.comboBox.addItem("PC")
        self.comboBox.addItem("MAC")
        self.model = QtGui.QStringListModel()
        self.model.setStringList(['some', 'words', 'in', 'my', 'dictionary'])
        self.completer = QtGui.QCompleter()
        self.completer.setModel(self.model)
        self.lineedit = QtGui.QLineEdit()
        self.lineedit.setCompleter(self.completer)
        self.lineedit.setText("31H9GV1")
        #self.lineedit.show()
        self.pushButtonWindow.setText("Extract!")
        #self.comboBox.activated[str].connect(self.on_pushButton_clicked)
        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.lineedit)
        self.layout.addWidget(self.pushButtonWindow)
        self.pushButtonWindow.clicked.connect(self.on_pushButton_clicked)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        combo_text = self.comboBox.currentText()
        search_text = self.lineedit.text()
        print ("Combo Box : "+combo_text)
        print ("Text Box : "+search_text)
        self.dialogTextBrowser = MyDialog(self,combo_text,search_text)
        self.dialogTextBrowser.exec_()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())