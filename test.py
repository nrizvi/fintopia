import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html" charset="utf-8"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/5.6.0/d3.min.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<link href="https://fonts.googleapis.com/css?family=Raleway:400|Roboto:300" rel="stylesheet"> 
<style>
.heading {
  width: 75%;
  margin-left: 150px;
  font-weight: bold;
}

body{
    background-color:  #fd7a7a;
    font-family: 'Raleway';
}

.slider {
  -webkit-appearance: none;
  width: 75%;
  margin-left: 150px;
  height: 25px;
  background: white;
  outline: none;
  opacity: 0.7;
  -webkit-transition: .2s;
  transition: opacity .2s;
  border-radius: 5px;
}

.slider:hover {
  opacity: 1;
}


.slider::-moz-range-thumb {
  width: 20px;
  height: 35px;
  background: #454545;
  cursor: pointer;
  border: none;
  margin-top: 40%;
}
.left{
    float: left;
    margin-left: 150px;
    font-style: italic;
}
.right{
    float: right;
    margin-right: 168px;
    font-style: italic;
}

h1{
    text-align: center;
    margin-top: 35px;
}

</style>
</head>
<body>
  <h1>On a scale of 1 to 5...</h1><br><br>
  <span class="question">
  <p class="heading">Where do you think your current financial status falls?</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange1">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  <br>
  </span>
  <span class="question">
  <br>
  <br><br>
  <p class="heading">Can you handle a major unexpected expense?</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange2">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  </span>
  </span>
  <span class="question">
  <br><br><br><br>
  <p class="heading">Are you securing your financial status?</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange3">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  </span>
   </span>
  <span class="question">
  <br><br><br><br>
  <p class="heading">I have money left over at the end of the month</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange4">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  </span>
   </span>
  <span class="question">
  <br><br><br><br>
  <p class="heading">I am behind my finances</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange5">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  </span>
   </span>
  <span class="question">
  <br><br><br><br><br>
  <p class="heading">I know how to get myself to follow through on my financial intentions</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange6">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  </span>
   </span>
  <span class="question">
  <br><br><br><br><br>
  <p class="heading">I know where to find advice I need to make decisions involving money</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange7">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  </span>
   </span>
  <span class="question">
  <br><br><br><br><br>
  <p class="heading">Because of my money situation I will never have things I want in life</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange8">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  </span>
   </span>
  <span class="question">
  <br><br><br><br><br>
  <p class="heading">I know how to make complex financial decisions</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange9">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  </span>
   </span>
  <span class="question">
  <br><br><br><br><br>
  <p class="heading">How would you assess your overall financial knowledge?</p>
  <input type="range" min="1" max="5" value="3" class="slider" id="myRange10">
  <br>
  <p class= "left">1</p>
  <p class= "right">5</p>
  </span>
</div>
<script>
var range1 = document.getElementById("myRange1");
var range2 = document.getElementById("myRange2");
var range3 = document.getElementById("myRange3");
var range4 = document.getElementById("myRange4");
var range5 = document.getElementById("myRange5");
var range6 = document.getElementById("myRange6");
var range7 = document.getElementById("myRange7");
var range8 = document.getElementById("myRange8");
var range9 = document.getElementById("myRange9");
var range10 = document.getElementById("myRange10");

var sum = (Number(range1.value)+Number(range2.value)+Number(range3.value)+Number(range4.value)+Number(range5.value)+Number(range6.value)+Number(range7.value)+Number(range8.value)+Number(range9.value)+Number(range10.value));
var avg = sum/10;
console.log(avg);
</script>
</body>
</html>
"""

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())