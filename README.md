<h1>Tomato-leaves-disease-Predictor</h1>
 <h3> © Raj Gupta 2021</h3>
   <br> 
   
  <h1>Paper Referenced from:</h1>
 <h3>1. Rethinking the Inception Architecture for Computer Vision
Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, Zbigniew Wojna https://arxiv.org/pdf/1512.00567v3</h3>
  <h3>2. Very Deep Convolutional Networks for Large-Scale Image Recognition
Karen Simonyan, Andrew Zisserman https://arxiv.org/pdf/1409.1556</h3>  <br> 
  
   <h1> Dataset obtained from:   </h1>   
   https://www.kaggle.com/adinishad/tomato-leaf-detection-by-transfer-learning/data
     <br> 
  <h1> Architecture used</h1>
 <p title=Architecture used>  
<ul>
<li>VGG19</li>
  <li>InceptionV3</li>
<li> No. of classes: 10</li>
<li>Classes :-  ['Tomato___Late_blight' , 'Tomato___healthy' , 'Tomato___Early_blight' , 'Tomato___Septoria_leaf_spot' , 'Tomato___Tomato_Yellow_Leaf_Curl_Virus' , 
'Tomato___Bacterial_spot' , 'Tomato___Target_Spot' , 'Tomato___Tomato_mosaic_virus' , 'Tomato___Leaf_Mold' , 'Tomato___Spider_mites Two-spotted_spider_mite']</li>
  </ul> </p>  
 <br> 
 
  <h1> Metrics for 10 Epochs (for InceptionV3) </h1>
 <p title= Metrics for 10 Epochs in IneptionV3 >  
<ul>
  
<li>loss: 0.3708</li>  
<li>accuracy: 0.9639</li>
  <li>val_loss: 4.1287</li>
<li>val_accuracy: 0.8198</li>
  </ul> </p>  
 <br> 
 
 <h1> Metrics for 10 Epochs (for VGG19) </h1>
 <p title= Metrics for 10 Epochs in VGG19 >  
<ul>
  
<li>loss: 0.0531</li>  
<li>accuracy: 0.9804</li>
  <li>val_loss: 0.2975</li>
<li>val_accuracy: 0.9210</li>
  </ul></p>  
 <br> 
 
 
 
 <h1>Deployment</h1> 
<p title=Deployment>  
<ul>
<li>Deployed it as a web application using Flask.</li>
<!-- <li> I didn't add much because of github limits to storage.</li> -->
 </ul> </p> 
 <br> 
  
   <br> 
 <h1> Libraries used</h1>
 <p title=Libraries used>  
<ul>
 <li>python==3.7</li>
<li>Flask==1.1.2</li>
<li>numpy==1.18.4</li>
 <li>tensorflow==2.2.0</li>
<li>Werkzeug==1.0.1</li>  
</ul> </p> 
  <br>  
 
  <h1> Tools used</h1>
 <p title=Tools used>  
<ul>
<li>Pycharm</li>
<li>Google Colab</li>
<li>git</li>
<li>Flask</li>
<!-- <li>Visual Studio</li> -->
</ul> </p> 
  <br> 

<img src="https://i.ibb.co/JnMG6BG/Screenshot-2021-11-06-151905.jpg"> 
<img src="https://i.ibb.co/61qSfQJ/Screenshot-2021-11-06-152022.jpg"> 
</ul>
</p>
<br>  
<br>  
<br>  
<br>  
