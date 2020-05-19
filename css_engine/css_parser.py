import re
""" CSS PARSER TOKENIZER """
#--NOTE--WHEN EVALUATING NUMERIC VALUES FROM CSS ATTS CHANGE "_" TO "-"
def css_token(st):
    """ HTML PRE FILTER """
    re.purge()
    st=re.sub('\/\*.*?\*\/\n', '', st)#REMOVE COMMENTS
    """ PRE CSS STYLE FILTER """
    st=re.findall('<style>.*?</style>', st, flags=re.DOTALL)
    st=''.join(map(str, st))
    #print('-------ALL STYLES--------')
    #print(st)
    #st=re.sub('<body.*?</body>', '', tt, flags=re.DOTALL)
    #st=re.sub('background-color:', 'background_color:', st)#ts shadow copy
    st=re.sub('-', '_', st)
    st=re.sub('content:.*?;', '', st)
    #st=re.sub(';', 'X;', st)#--PLANT A DELIMITER FOR #COLOR
    st=re.sub('-width', '-wide', st)#--PATCH FOR CSS BORDER-STYLE:BORDER-WIDTH;
    st=re.sub('<style>', '<style>}', st)
    st=re.sub('\s', ' ', st)
    #st=re.findall('<style>.*?</style>', st, flags=re.DOTALL)
    #st=''.join(map(str, st))
    #print('CSCSCSCSCSCSCSCSCSCSCSCSCSCS')
    #print(st)
    """ CONVERT PERCENTILES TO PIXEL FORMAT """
    #def percent_to_pixel(st):
    wt=re.findall('width:(.*?);', st, flags=re.DOTALL)
    wt2=re.findall('height:(.*?%);', st, flags=re.DOTALL)
    if 'px in wt2':
        st=st.replace('px', '')
    #print(wt)
    """ CONVERT % TO PIXELS """
    for h in wt:
        h=str(h)
        if'%' in h: 
            h1=re.sub('%', '', h)
            nh1=float(h1)
            nh2=nh1*13.4000 #WAS .40
            nh3=round(nh2)
            nh4=str(nh3)
            st=st.replace(h, nh4)
            print(nh4)
        if 'px' in h:
            px=re.sub('px', '', h)
            st=st.replace('px', '')
            print(px)
        pass
    """ FORMAT THE CSS """
    rr=re.findall('color:(#.*?);', st, flags=re.DOTALL)
    for c in rr:
        if c:
            c=str(c)
            st=st.replace(c, '"'+c+'X"')
    st=re.sub('\s', ' ', st)
    st=re.sub(':', '":"', st)
    st=re.sub(';}', '" }', st)
    st=re.sub('; ', '", "', st, flags=re.DOTALL)
    st=re.sub(' }', '}', st)
    st=re.sub('{', '{ "', st)
    st=re.sub('}', ' }\n', st)
    st=re.sub(': ', ':', st)
    st=re.sub('""', '"', st)
    st=re.sub(' { ', '{', st)
    st=re.sub(' }', '}', st)
    # -after- remove quotes from numbered integers
    st=re.sub('0"', '0', st)
    st=re.sub('1"', '1', st)
    st=re.sub('2"', '2', st)
    st=re.sub('3"', '3', st)
    st=re.sub('4"', '4', st)
    st=re.sub('5"', '5', st)
    st=re.sub('6"', '6', st)
    st=re.sub('7"', '7', st)
    st=re.sub('8"', '8', st)
    st=re.sub('9"', '9', st)
    # -before-
    st=re.sub('"0', '0', st)
    st=re.sub('"1', '1', st)
    st=re.sub('"2', '2', st)
    st=re.sub('"3', '3', st)
    st=re.sub('"4', '4', st)
    st=re.sub('"5', '5', st)
    st=re.sub('"6', '6', st)
    st=re.sub('"7', '7', st)
    st=re.sub('"8', '8', st)
    st=re.sub('"9', '9', st)
    #st=re.sub('#', '', st)#--fix color
    # Intermediate replacements to get proper "#color"
    #s2.replace('b',' ')
    #s2.replace('v','b')
    #s2.replace(' ','v')
    #st=re.sub('}', ' }', st)# shift for color find
    #st=re.sub(',', '",', st)# shift for color find
    
    #rt=re.findall('color:#.*? ', st, flags=re.DOTALL)
    #print(rt)
    #rt=''.join(map(str, rt))
    #for c in rt:
    #    if c:
    #        c=str(c)
    #        st=st.replace(c, '"'+c+'X"')
    st=re.sub('X', '', st)# REMOVE COLOR DELIMITER
    st=re.sub('""', '"', st)
    st=re.sub('""', '"', st)
    st=re.sub('""', '"', st)
    #st=re.sub(' }', '}', st)# unshift color find
    #st=re.sub(' ,', ',', st)# shift for color find
    #st=re.sub('""', '"', st)
    #st=re.sub(';', '', st)
    st=str(st)
    print(st)
    return st

















