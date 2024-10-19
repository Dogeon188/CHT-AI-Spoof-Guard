let spoofModel = "dummy"
let relationModel = "dummy"
let apiurl = "http://localhost:8086"

function requestSpoof(src, textContent) {
    const spoofPromise = fetch(`${apiurl}/spoof_detect`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "model": spoofModel,
            "image": src,
        })
    });

    const relationPromise = fetch(`${apiurl}/text_image_relation`, {
        method: "POST",
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "model": relationModel,
            "image": src,
            "text": textContent,
        })
    });

    return Promise.all([spoofPromise, relationPromise]);
}

function siblingCount(node) {
    if (!node.parentNode) return 1
    return node.parentNode.children.length
}

function main() {
    const article = document.querySelector("article")
    if (!article) return
    article.querySelectorAll("img").forEach(async img => {
        if (!img.checkVisibility()) return

        // iteratively find the container of the image
        let container = img
        while (siblingCount(container) === 1) {
            container = container.parentNode
        }

        // get text of prev/next sibling of container
        let text = ""
        if (container.previousElementSibling) {
            text += container.previousElementSibling.innerText + "\n"
        }
        if (container.nextElementSibling) {
            text += container.nextElementSibling.innerText + "\n"
        }
        if (img.alt) {
            text += img.alt
        }
        console.log("text", text)

        const response = await requestSpoof(img.src, text)
        if (!response[0].ok) {
            console.error("Failed to fetch spoof detection response.")
            return
        }
        if (!response[1].ok) {
            console.error("Failed to fetch text-image relation response.")
            return
        }

        const spoofData = await response[0].json()
        const relationData = await response[1].json()
        console.log("spoofData", spoofData)
        console.log("relationData", relationData)

        let newDiv = document.createElement("div")
        newDiv.style.backgroundColor = "lightblue"
        newDiv.innerHTML = `
            <strong>Detected content:</strong><br>
            Spoof Detection - Result: ${spoofData.result}, Confidence: ${spoofData.confidence}<br>
            Text-Image Relation - Result: ${relationData.result}, Confidence: ${relationData.confidence}
        `
        img.parentNode.insertBefore(newDiv, img.nextSibling)
    })
}

function main_ettoday() {
    document.querySelectorAll("div.story p").forEach(async (p, index, pElements) => {
        let img = p.querySelector("img");

        if (img) {
            let nextP = pElements[index + 1];
            let text = nextP ? nextP.querySelector("strong") : null;

            if (text) {
                let src = img.src;
                let textContent = text.innerText;

                if (src && textContent) {
                    console.log("Image Source:", src);
                    console.log("Text Content:", textContent);

                    requestSpoof(src, textContent).then(async ([spoofResponse, relationResponse]) => {
                        console.log("Spoof Detection Response:", spoofResponse);
                        console.log("Text-Image Relation Response:", relationResponse);
                        if (spoofResponse.ok && relationResponse.ok) {
                            const spoofData = await spoofResponse.json();
                            const relationData = await relationResponse.json();

                            let newDiv = document.createElement("div");
                            newDiv.style.backgroundColor = "lightblue";
                            newDiv.innerHTML = `
                            <strong>Detected content:</strong><br>
                            Spoof Detection - Result: ${spoofData.result}, Confidence: ${spoofData.confidence}<br>
                            Text-Image Relation - Result: ${relationData.result}, Confidence: ${relationData.confidence}
                            `;

                            // 插入新的 div
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
}

chrome.storage.sync.get(['spoof', 'tir', 'apiurl'], async function (result) {
    spoofModel = result.spoof;
    relationModel = result.tir;
    apiurl = result.apiurl;
    main()
    // main_ettoday();
});
