"""
--------------------------------------------------------
                CSS <style> FETCHER
--------------------------------------------------------
"""
import ast
"""
--------------------------------------------------------
HERE WE FEED THE CLASS-NAME AND PARSED CSS TO FETCH
THEIR CSS RULES AND CONVERT THEM TO PYTHON DICTIONARIES
--------------------------------------------------------
"""
def fetch_css(cls, st):
    st=re.findall('\.'+cls+'(.*?})', st, flags=re.DOTALL)
    st=''.join(map(str, st))
    st = ast.literal_eval(st)
    #print(st)
    if st:
        #print('smuk')
        #print(st)
        return st
    else:
        pass
