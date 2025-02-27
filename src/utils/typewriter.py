import time 
def typewriter_print(text, delay=0.01, end='\n'):
    '''
    模拟打字机效果输出文本   
    '''
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)