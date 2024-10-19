var spoofSelect = document.getElementById('spoof-select');
var tirSelect = document.getElementById('tir-select');
var apiUrlInput = document.getElementById('api-url');

async function loadModels(apiurl) {
    const spoof_models = await (await fetch(`${apiurl}/spoof_detect/models`)).json();
    for (var i = 0; i < spoof_models.length; i++) {
        var option = document.createElement('option');
        option.text = spoof_models[i];
        spoofSelect.add(option);
    }

    const tir_models = await (await fetch(`${apiurl}/text_image_relation/models`)).json();
    for (var i = 0; i < tir_models.length; i++) {
        var option = document.createElement('option');
        option.text = tir_models[i];
        tirSelect.add(option);
    }
}

chrome.storage.sync.get(['spoof', 'tir', 'apiurl'], async function (result) {
    const spoof = result.spoof;
    const tir = result.tir;
    const apiurl = result.apiurl;

    await loadModels(apiurl);

    if (spoof) spoofSelect.value = spoof;
    if (tir) tirSelect.value = tir;
    if (apiurl) apiUrlInput.value = apiurl;
});

spoofSelect.addEventListener("input", function () {
    chrome.storage.sync.set({ 'spoof': spoofSelect.value });
    console.log("spoof", spoofSelect.value);
})

tirSelect.addEventListener("input", function () {
    chrome.storage.sync.set({ 'tir': tirSelect.value });
    console.log("tir", tirSelect.value);
})

apiUrlInput.addEventListener("input", function () {
    chrome.storage.sync.set({ 'apiurl': apiUrlInput.value });
    loadModels(apiUrlInput.value);
    console.log("apiurl", apiUrlInput.value);
})

