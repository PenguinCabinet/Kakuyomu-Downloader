import unittest
from main import *
import time
import os

def get_archive_NOTZIP_from_data(target_url):
    r = requests.get(target_url)  
    soup = BeautifulSoup(r.text, "html.parser")


    dir_name=soup.select_one('#workTitle').text
    print(dir_name)
    try:
        os.mkdir("./{0}".format(dir_name))
    except FileExistsError:
        pass
    """

    zip_stream = io.BytesIO()
    """


    def if_episode(x):
        return "episodes" in x

    if True:
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
                with open("{0}/{1}.txt".format(dir_name,title),"w",encoding="utf-8") as f:
                    f.write(title+"\n\n"+txt)
                #new_zip.writestr("{0}/{1}.txt".format(dir_name,title), title+"\n\n"+txt)
    #print(zip_stream.getvalue())
    #return zip_stream.getvalue(),dir_name

class TestAPI(unittest.TestCase):
    def test_tashizan(self):
        start_time = time.perf_counter()
        #get_archive_NOTZIP_from_data("https://kakuyomu.jp/works/1177354054882029230")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print("NOTZIP {0}".format(elapsed_time))

        start_time = time.perf_counter()
        get_zip_from_data("https://kakuyomu.jp/works/1177354054882029230")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print("ZIP {0}s".format(elapsed_time))


if __name__ == "__main__":
    unittest.main()