import requests
def reqHeader(url,header_type='Content-Length',TIME_OUT=3):
   
    try:
        response = requests.head(url,timeout=TIME_OUT)
        content=response
        response.close()
        return (content.status_code,content.headers['server'],content.headers['last-modified'],content.headers[header_type])
    except:
        return (404,'')

        
def mycurl(url,TIME_OUT=3):
    try:
        response = requests.get(url,timeout=TIME_OUT)
        response.close()
    except Exception as e:
        return(0,'')
    return (response.status_code,response.text)
if __name__=='__main__':
    print(mycurl('http://127.0.0.1/rsupgrade/rspcver12.xml'))
    print(mycurl('http://192.168.10.100/rsupgrade/rspcver12.xml'))