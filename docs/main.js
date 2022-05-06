async function downloader(url){
    if(document.getElementById('console').innerText!="")
        return;
    document.getElementById('console').innerText="ダウンロード中..."
    fetch(
        `https://oq9b5canwh.execute-api.us-east-1.amazonaws.com/dev/title?url=${url}`,
        {'Accept': 'text/plain',method: 'GET',},
    ).then(async (title)=>{
        let title_data=await title.text()
        console.log((title_data));
        fetch(
            `https://oq9b5canwh.execute-api.us-east-1.amazonaws.com/dev/make?url=${url}`,
            {'Accept': 'application/zip',method: 'GET',},
        )
        .then(async(res)=>{
            document.getElementById('console').innerText=""
            let blob = await res.blob();
            let link = document.createElement('a');
            console.log(blob);
            link.href = window.URL.createObjectURL(
                blob
            );
            document.body.appendChild(link);
            link.download = `${title_data}`
            link.click();
        })
    })

}//https://oq9b5canwh.execute-api.us-east-1.amazonaws.com/dev/make?url=
//https://kakuyomu.jp/works/16816700426335359442

function downloader_rapper(){
    downloader(document.getElementById("url").value);
}

