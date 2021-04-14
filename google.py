from browser import *

class Google (Browser):
    def __init__(self):
        super().__init__()
    def fazerBusca(self, palavras):
        print("Você está pesquisando {}".format(palavras))
        paginas = ["https://www.google.com.br", "https://www.google.com", "https://www.google.com.ar", "https://www.google.com.vn", "https://www.google.com.pa",
		"https://www.google.co.uk/", "https://www.google.fr/", "https://www.google.ch/","https://www.google.de/", "https://www.google.pl/", "https://www.google.it/",
		"https://www.google.ie/webhp", "https://www.google.es/", "https://www.google.pt/", "https://www.google.at/", "https://www.google.com.au/webhp",
		"https://www.google.co.ma/", "https://www.google.cz/", "https://www.google.ca/webhp", "https://www.google.com.mx/", "https://www.google.com.co/",
		"https://www.google.com.ec/", "https://www.google.hn/", "https://www.google.no/", "https://www.google.se/", "https://www.google.nl/", "https://www.google.co.il/",
		"https://www.google.co.jp/" ]
        pagina = paginas[random.randint(0, len(paginas) - 1)]
        print("A pagina do google será: {}".format(pagina))

        self.driver.get(pagina)
        d = self.driver

        input_q = d.find_element_by_xpath("//input[@name='q']")
        input_q.send_keys(palavras)
        input_q.send_keys(Keys.RETURN)
        buffer_links = []
        links_ = []
        file = open(palavras.replace("?", "").replace(" ", "") + '.txt', 'w+')
        buffer_quadros = self.driver.find_elements_by_xpath("//*[@class='g' and div[1]/div[1]/a]")
        for i in range(len(buffer_quadros)):
            try:
                link = buffer_quadros[i].find_element_by_xpath("./div[1]/div[1]/a").get_attribute('href')
                buffer_links.append(link)
                for x in buffer_links:
                    if x not in links_:
                        links_.append(x)
            except:
                print('...Uma div foi ignorada....')
        for l in links_:
            file.write(l + '\n')
        print(links_)

