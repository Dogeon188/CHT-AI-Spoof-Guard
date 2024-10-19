chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
  
    document.getElementById('url').textContent = url;
  
    let data = {
      url: url
    };
  
    // 使用 fetch 發送 POST 請求給後端
    fetch('http://localhost:5000/core/scrape', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
      console.log('成功:', data);
    })
    .catch((error) => {
      console.error('錯誤:', error);
    });
  });
  
  