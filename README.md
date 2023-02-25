# Video Label Tool 

This project was developed as a solution to a problem I had when creating a dataset for image models. When training a model for an object from everyday life, a video recording is usually taken, then this video recording is fragmented and the images are lablized one by one. This process is both tedious and time consuming. In this project, I wrote a program to track a selected object from the video using the ready-made trackers in the OpenCV library. The program consists of two main modules: testing and tagging. In the test module, you try all tracking methods for the object you want to track in your video and choose the most suitable option. In the tagging module, it starts the tagging process with the tracker of your choice. <br>

> **Note** <br>
> If you try the trackers first and then move on to lablizing, you can continue with the pre-set bounding box

## Setup

1. Clone this repostiory : `git clone https://github.com/Arslanex/Video-Label-Tool.git `
2. Instal requirements : `pip install -r requirements.txt`
3. Run main.py script : `python main.py`


## Program Insights
<h3 align="center"> Try all the trackers for your object </h3>
<p align="center">

[video](https://user-images.githubusercontent.com/44752389/190900389-2c12431f-32d7-4e5a-ad9f-3c98ca24fea4.mp4)

</p>

<h3 align="center"> Try only one tracker for your object </h3>
<p align="center">

[video](https://user-images.githubusercontent.com/44752389/190899000-7c4c8851-3a8d-4c73-b054-eca21e335702.mp4)

</p>

<h3 align="center"> Start labelling progress </h3>
<p align="center">

[video](https://user-images.githubusercontent.com/44752389/190899004-ce9337b1-0ca1-4d9e-8ae0-497cbe19d295.mp4
)

</p>


***
<h3 align="center"> Enes ARSLAN </h3>
<p align="center">
<a href="https://www.instagram.com/_enes.arslan_/?next=%2F">
<img src="https://img.shields.io/badge/Instagram-000000?style=for-the-badge&logo=instagram&logoColor=white"/>
<a href="https://www.linkedin.com/in/enes-arslan-/">
<img src="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&logo=linkedin&logoColor=white"/>
<a href="https://github.com/Arslanex">
<img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white"/ >
</p>
