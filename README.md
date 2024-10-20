# FFN - Fight against deepFake News

## Introduction

This project consists of an api server that provides deepfake image detection services and text-image relationship analysis, and a wrapper chrome extension that allows users to detect deepfake images in news articles.

## Installation

Please refer to [server/README.md](server/README.md) for backend installation instructions, and [client/README.md](client/README.md) for frontend installation instructions.

## Usage

Once installed the chrome extension, users can click on the extension icon to configure the extension settings. You should:

1. Set the server URL to the URL of the backend server. (If you are running the backend server locally, it should be `http://localhost:8086`.)
2. Pick your desired detector model. They should be listed out in the dropdown menu.
3. When you visit a news article, the extension will automatically scan the images on the page and highlight any deepfake images it detects.

## Citation

- [WisconsinAIVision/UniversalFakeDetect](https://github.com/WisconsinAIVision/UniversalFakeDetect) for deepfake detection model.
- [ZhendongWang6/DIRE](https://github.com/ZhendongWang6/DIRE) for deepfake detection model.
- [OpenAI API](https://openai.com/index/openai-api/) for text-image relationship analysis.

## Acknowledgements

This project was developed as part of the [2024 Meichu Hackathon](https://meichuhackathon.org/2024/) event. We would like to thank the organizers for hosting the event, and Chunghwa Telecom for providing the subject and guidance.

## Contributors

Listed in alphabetical order.

- 張以寧 Chang, Yi-Ning
- 廖幃萱 Liao, Wei-Syuan
- 李文婷 Lee, Wen-Ting
- 賴姿妘 Lai, Zi-Yun
- 毛柏毅 Mao, Bo-Yi
