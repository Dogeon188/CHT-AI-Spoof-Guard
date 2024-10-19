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