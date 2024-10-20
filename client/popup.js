var spoofSelect = document.getElementById('spoof-select');
var tirSelect = document.getElementById('tir-select');
var apiUrlInput = document.getElementById('api-url');
var enabledCheck = document.getElementById('enabled');

async function loadModels(apiurl) {
    const spoof_models = await (await fetch(`${apiurl}/spoof_detect/models`)).json();
    spoofSelect.innerHTML = '';
    for (var i = 0; i < spoof_models.length; i++) {
        var option = document.createElement('option');
        option.text = spoof_models[i];
        spoofSelect.add(option);
    }

    const tir_models = await (await fetch(`${apiurl}/text_image_relation/models`)).json();
    tirSelect.innerHTML = '';
    for (var i = 0; i < tir_models.length; i++) {
        var option = document.createElement('option');
        option.text = tir_models[i];
        tirSelect.add(option);
    }
}

chrome.storage.sync.get(['spoof', 'tir', 'apiurl', 'enabled'], async function (result) {
    const spoof = result.spoof;
    const tir = result.tir;
    const apiurl = result.apiurl;
    const enabled = result.enabled;

    await loadModels(apiurl);

    if (enabled) enabledCheck.checked = true;
    if (spoof) spoofSelect.value = spoof;
    if (tir) tirSelect.value = tir;
    if (apiurl) apiUrlInput.value = apiurl;
});

spoofSelect.addEventListener("input", function () {
    chrome.storage.sync.set({ 'spoof': spoofSelect.value });
})

tirSelect.addEventListener("input", function () {
    chrome.storage.sync.set({ 'tir': tirSelect.value });
})

apiUrlInput.addEventListener("input", function () {
    chrome.storage.sync.set({ 'apiurl': apiUrlInput.value });
    loadModels(apiUrlInput.value);
})

enabledCheck.addEventListener("input", function () {
    chrome.storage.sync.set({ 'enabled': enabledCheck.checked });
})
