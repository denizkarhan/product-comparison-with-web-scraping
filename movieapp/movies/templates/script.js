const veri = [];

function checkMe() {
  var cb = document.getElementById("abc");
  var text = document.getElementById("msg");
  if(cb.checked==true){
    veri.push("Apple");
    text.style.display="block";
    
  }else{
    if(veri.includes("Apple")){
       veri.pop("Apple");}
       text.style.display="none";       
  }    
}
function checkMe2() {
  var cb = document.getElementById("abc2");
  var text = document.getElementById("msg2");
  if(cb.checked==true){
    veri.push("Lenovo");
    text.style.display="block";
    
  }else{
    if(veri.includes("Lenovo")){
       veri.pop("Lenovo");}
       text.style.display="none";          
  }
}
function push() {
  var cb = document.getElementById("filtre");
  var text = document.getElementById("msg2");
  if(cb.checked==true){
    document.write()     
  }
}
  