# Video-Label-Tool
## Neden böyle bir şey geliştridim ?
Nesne tanıma ve takibi için hazırlanan modeller ilgili nesnenin bir çok resmi bir araya getirilerek oluştururlur. Yarıştığım İnsansız Su Altı Sistemleri yarışmalaraında
su altında bulunan nesnelerin tespit edilmesi gerekiyordu. Bunun için görev objelerinin replikalarını yapıp su altında video kaydına alarak eğitim için veri seti 
materyali topluyorduk. Çekilen videon frame by frame parçalanması ve ardından labellanması işlemlleri hem sıkıcı hem de uzun bir iş olduğu için bu projeyi geliştirdim. 
Program bir videodaki seçili nesneyi OpenCV tracker'ları ile takip ederken aynı zamanda label atıyor ve kullanıcının tüm yükünü ortadan kaldırıyor. 

## To-Do
 - [ ] Takip oranının arttırmak için resimler küçültülebilir
 - [ ] Takip oranını arttırmak için resim yumuşatılabilir, gürültü azaltılabilir
 - [ ] Göresel arayüz ekelenmeli
 - [ ] Görsel arayüz üzerinden videonun istenilen kısımlarında işelem yapılabilecek
 
## Videos
### Trying all trackers on the video

Uploading vid1.mp4…


### Trying selected tracker on the video


https://user-images.githubusercontent.com/44752389/190899000-7c4c8851-3a8d-4c73-b054-eca21e335702.mp4


### Creating data set with selected tracker


https://user-images.githubusercontent.com/44752389/190899004-ce9337b1-0ca1-4d9e-8ae0-497cbe19d295.mp4

