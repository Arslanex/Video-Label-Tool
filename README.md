# Video-Label-Tool
## Why Did I Developed Something Like This ?
Models prepared for object recognition and tracking are created by bringing together many pictures of the relevant object. In the Unmanned Underwater Systems competitions I competed in, objects under water had to be detected. For this, we were collecting dataset material for training by making replicas of mission objects and recording them underwater. I developed this project because the process of breaking the captured video frame by frame and then labeling it is both tedious and long. While the program tracks the selected object in a video with OpenCV trackers, it also assigns labels and removes all the burden of the user.

## To-Do
 - [ ] Takip oranının arttırmak için resimler küçültülebilir
 - [ ] Takip oranını arttırmak için resim yumuşatılabilir, gürültü azaltılabilir
 - [ ] Göresel arayüz ekelenmeli
 - [ ] Görsel arayüz üzerinden videonun istenilen kısımlarında işelem yapılabilecek

## SetUp

```git clone https://github.com/Arslanex/Video-Label-Tool.git ```

```cd Video-Label-Tool ```

```pip install -r requirements.txt```

```python main.py```


## Videos
### Trying all trackers on the video

https://user-images.githubusercontent.com/44752389/190900389-2c12431f-32d7-4e5a-ad9f-3c98ca24fea4.mp4

### Trying selected tracker on the video


https://user-images.githubusercontent.com/44752389/190899000-7c4c8851-3a8d-4c73-b054-eca21e335702.mp4


### Creating data set with selected tracker


https://user-images.githubusercontent.com/44752389/190899004-ce9337b1-0ca1-4d9e-8ae0-497cbe19d295.mp4

