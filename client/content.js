document.querySelector("div.story").querySelectorAll("p").forEach(async (p, index, pElements) => {
    let img = p.querySelector("img");

    if (img) {
        let nextP = pElements[index + 1];
        let text = nextP ? nextP.querySelector("strong") : null;

        if (text) {
            let src = img.getAttribute("src");
            let textContent = text.innerText;

            

            if (src && textContent) {
                console.log("Image Source:", src);
                console.log("Text Content:", textContent);

                const spoofPromise = fetch("http://localhost:8086/spoof_detect", {
                    method: "POST",
                    mode: "cors",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        "image": src,
                        "uuid": crypto.randomUUID(),
                        "model": ""
                    })
                });

                const relationPromise = fetch("http://localhost:8086/text_image_relation", {
                    method: "POST",
                    mode: "cors",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        "text": text,
                        "image": src,
                        "uuid": crypto.randomUUID(),
                        "model": ""
                    })
                });

                Promise.all([spoofPromise, relationPromise]).then(async ([spoofResponse, relationResponse]) => {
                    if (spoofResponse.ok && relationResponse.ok) {
                        const spoofData = await spoofResponse.json();
                        const relationData = await relationResponse.json();
                        console.log("Spoof Detection Response:", spoofData);
                        console.log("Text-Image Relation Response:", relationData);

                        let newDiv = document.createElement("div");
                        newDiv.style.backgroundColor = "lightblue";
                        newDiv.style.padding = "10px";
                        newDiv.style.marginTop = "10px";
                        newDiv.textContent = `Detected content: \nSpoof Detection - Result: ${spoofData.result}, Confidence: ${spoofData.confidence}\nText-Image Relation - Result: ${relationData.result}, Confidence: ${relationData.confidence}`;

                        // 插入新的 div 到 img 后面
                        img.parentNode.insertBefore(newDiv, img.nextSibling);
                    } else {
                        if (!spoofResponse.ok) {
                            console.error("Failed to fetch spoof detection response.");
                        }
                        if (!relationResponse.ok) {
                            console.error("Failed to fetch text-image relation response.");
                        }
                    }
                })
                .catch(error => {
                    console.error("Error occurred while fetching data:", error);
                });
            }
        }
    }
});

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