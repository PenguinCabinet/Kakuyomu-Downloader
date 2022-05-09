base_url="https://p9bwl9j7df.execute-api.ap-northeast-1.amazonaws.com/dev";

const my_sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function downloader(url){
    if(document.getElementById('console').innerText!="")
        return;
    document.getElementById('console').innerText="ダウンロード中..."
    fetch(
        `${base_url}/title?url=${url}`,
        {'Accept': 'text/plain',method: 'GET',},
    ).then(async (title)=>{
        let title_data=await title.text()
        console.log((title_data));
        let download_and_check=async(res)=>{
            let temp=function(){
                fetch(
                    `${base_url}/download?dir_name=${title_data}`,
                    {'Accept': 'application/zip',method: 'GET',},
                )
                .then(async(res2)=>{
                    console.log(res2);
                    let blob = await res2.blob();
                    let link = document.createElement('a');
                    console.log(blob);
                    if(blob.type!="application/zip"){
                        await my_sleep(2000);
                        temp();
                        return
                    }
                    document.getElementById('console').innerText=""
                    link.href = window.URL.createObjectURL(
                        blob
                    );
                    document.body.appendChild(link);
                    link.download = `${title_data}`
                    link.click();
                })
            }
            temp();
        };
        fetch(
            `${base_url}/make?url=${url}`,
            {'Accept': 'application/zip',method: 'GET',},
        )
        .then(download_and_check)
        .catch(download_and_check);
    })

}//https://oq9b5canwh.execute-api.us-east-1.amazonaws.com/dev/make?url=
//https://kakuyomu.jp/works/16816700426335359442

function downloader_rapper(){
    downloader(document.getElementById("url").value);
}

