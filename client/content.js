const spoofModel = "dummy"
const relationModel = "dummy"

function requestSpoof(src, textContent) {
    const spoofPromise = fetch('http://localhost:8086/spoof_detect', {
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

    const relationPromise = fetch("http://localhost:8086/text_image_relation", {
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
        console.log("img", img)
        const altText = img.alt
        let container = img
        while (siblingCount(container) === 1) {
            container = container.parentNode
        }
        console.log("container", container)
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


console.clear()
// main()
main_ettoday()
