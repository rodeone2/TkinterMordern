""" Html Parser Engine """
from html.parser import HTMLParser
from html.entities import name2codepoint
re.purge()


"""
-------------------------------------------
    HTML PARSER ENGINE AND STORAGE CONTAINER LIST FOR RENDERING
-------------------------------------------
"""
#parsed_list=[]

class MyHTMLParser(HTMLParser):
    parsed_list=[]
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        parsed_list.append(tag)    
        for attr in attrs:
            if attr[0] == 'href':
                print("     href:", attr[1])
            elif attr[0] == 'class':
                print("     class:", attr[1])
                parsed_list.append(attr[1]) 
            elif attr[0] == 'id':
                print("     id:", attr[1])
            elif attr[0] == 'style':
                print("     style:", attr[1])
                
    """
    def handle_endtag(self, tag):
        print("End tag  :", tag)
        parsed_list.append(tag)
    """
    def handle_data(self, data):# text-------
        if data != ' ':
            print("Data     :", data)
            parsed_list.append(data)
        else: pass
    
    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)
    
    """
    def handle_decl(self, data):
        print("Decl     :", data)
    """
    """
    def handle_comment(self, data):
        print("Comment  :", data)
    """
    return parsed_list
