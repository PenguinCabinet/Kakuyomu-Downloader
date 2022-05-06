import requests
from bs4 import BeautifulSoup
import io
import zipfile
import json
import base64


def Get_title(event, context):
    headers_plain_text={
        "Content-Type": "text/plain",
        "Access-Control-Allow-Headers" : "Content-Type",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
    }
    if event.get('queryStringParameters') is None:
        return {
                    "statusCode": 501,
                    "headers": headers_plain_text,
                    "body": "event.get('queryStringParameters') is None.",
                }
    title=get_title_from_data(event.get('queryStringParameters').get('url'))
    response = {
        "statusCode": 200,
            "headers": headers_plain_text,
        "body": title,
    }

    return response

def Make_zip(event, context):
    print('event:', json.dumps(event))
    headers_plain_text={
        "Content-Type": "text/plain",
        "Access-Control-Allow-Headers" : "Content-Type",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
    }
    if event.get('queryStringParameters') is None:
        return {
                    "statusCode": 501,
                    "headers": headers_plain_text,
                    "body": "event.get('queryStringParameters') is None.",
                }
    try:
        url=event.get('queryStringParameters').get('url')
        if url is None:
            return {
                        "statusCode": 501,
                        "headers": headers_plain_text,
                        "body": "url is None.",
                    }
    except AttributeError:
            return {
                        "statusCode": 501,
                        "headers": headers_plain_text,
                        "body": "url is None.",
                    }

    zip_data,title=get_zip_from_data(url)

    response = {
        "statusCode": 200,
        "headers": headers_plain_text,
        "body": base64.b64encode(zip_data).decode("utf-8"),
        "isBase64Encoded": True,
    }

    return response

def get_title_from_data(target_url):
    r = requests.get(target_url)  
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.select_one('#workTitle').text


def get_zip_from_data(target_url):
    r = requests.get(target_url)  
    soup = BeautifulSoup(r.text, "html.parser")


    dir_name=soup.select_one('#workTitle').text
    print(dir_name)
    """
    try:
        os.mkdir("./{0}".format(dir_name))
    except FileExistsError:
        pass
    """

    zip_stream = io.BytesIO()

    #with zipfile.ZipFile(zip_stream, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:

    def if_episode(x):
        return "episodes" in x

    with zipfile.ZipFile(zip_stream, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        for a in soup.find_all("a"):
            URL=a.get('href')
            if if_episode(URL):
                soup2 = BeautifulSoup(requests.get("https://kakuyomu.jp"+URL).text)

                #print(soup2)
                title = soup2.select_one('.widget-episodeTitle').text
                print(title)
                txt = soup2.select_one('.widget-episodeBody').get_text()
                """
                with open("{0}/{1}.txt".format(dir_name,title),"w",encoding="utf-8") as f:
                    f.write(title+"\n\n"+txt)
                """
                new_zip.writestr("{0}/{1}.txt".format(dir_name,title), title+"\n\n"+txt)
    #print(zip_stream.getvalue())
    return zip_stream.getvalue(),dir_name

"""
A,dir_name=Get_zip('https://kakuyomu.jp/works/16816700426335359442')
with open("{0}.zip".format(dir_name),"wb") as f:
    f.write(A)
"""
