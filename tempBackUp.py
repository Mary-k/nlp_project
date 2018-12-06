    url_poem_page=PoemUrlPart1+str(poetId)+PoemUrlPart2+str(poemId)                                                
                                response  = session.get(url_poem_page)
                                soup = BeautifulSoup(response.text.encode('cp1252').decode('cp1256'), 'lxml')
                                table = soup.find_all(class_="poem") 
                                title = soup.find('title')
                                (authorName,poemName)=getAuthorName(str(title.string))        
                                items = ET.SubElement(data, 'poem')  
                                items.set('author',authorName) 
                                items.set('title',poemName)  
                                FileSave=open(filePath+'poemes.txt','w',encoding = "utf-8")
                                for row in table:
                                        if len(re.findall(r'>(.+?)<',str(row)))>0 :
                                                string=html.unescape(str(re.findall(r'>(.+?)<',str(row))[0]))                          
                                                item1 = ET.SubElement(items, 'verse')  
                                                item1.text =html.unescape(string)
                                                FileSave.write(string)     
                                mydata = ET.tostring(data)  
                                myfile = open(filePath+"poemes.xml", "w")  
                                myfile.write(html.unescape(mydata.decode("utf-8")) )          
                                FileSave.close()


corpus_path=corpusPath+ErasforldersList[target_era]+poemTypes[0]
                        url_poem=url_poem_page=PoemUrlPart1+str(poetId)+PoemUrlPart2+str(poemId)
                        print(corpus_path)
                        print(url_poem)
        