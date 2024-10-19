console.log("purple");
document.querySelector("div.story").querySelectorAll("p.no_margin").forEach(async p => {
    let img = p.querySelector("img");
    let text = p.querySelector("strong");

    if (img && text) {
        let src = img.getAttribute("src");
        let textContent = text.textContent;

        if (src && textContent) {
            // console.log("src",src,"textContent",textContent);
            // const spoof = await fetch("http://localhost:8086/spoof_detect", {
            //     method: "POST",
            //     mode: "cors",
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     body: JSON.stringify({
            //         "image": src,
            //         "uuid": crypto.randomUUID(),
            //         "model": ""
            //     })
            // });

            // const relation = await fetch("http://localhost:8086/text_image_relation", {
            //     method: "POST",
            //     mode: "cors",
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     body: JSON.stringify({
            //         "text": text,
            //         "image": src,
            //         "uuid": crypto.randomUUID(),
            //         "model": ""
            //     })
            // });

            // if (spoof && relation) {
            //     let newDiv = document.createElement("div");
            //     newDiv.style.backgroundColor = "lightblue";
            //     newDiv.textContent = "Detected content: " + textContent;

            //     // 插入新的 div 到 img 后面
            //     img.parentNode.insertBefore(newDiv, img.nextSibling);
            // }
        }
    }
});