#!C:\Python27\python.exe -u
#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import sys
print "Content-type: text/html"
print

print """
<html>

<head><title></title></head>

<body>
<script 
   type="text/javascript" 
   language="JavaScript">

   function insertion(size){
   		//if(size==2000000)
   	   		//alert("It takes a while to run 2m entries")
   	   	document.getElementById("random_insertiom").innerHTML="sorting.."	
	   	var xmlHttp = new XMLHttpRequest();
	  	theUrl = "http://127.0.0.1:8000/sort.py?param1="+String(size)
	    xmlHttp.open( "GET", theUrl, true); // false for synchronous request
	    xmlHttp.onreadystatechange=function()
		  {
		   	document.getElementById("random_insertiom").innerHTML="sorting.."	
		  if (xmlHttp.readyState==4 && xmlHttp.status==200)
		    {
		    //alert("hey")
		    document.getElementById("random_insertiom").innerHTML=xmlHttp.responseText;
		      //var parse = JSON.parse(xmlHttp.responseText);
		      //alert(parse)
		    }
		  }

	    xmlHttp.send( null );
   }
   function selection(size){
       //alert("I am here"+size)
   		//if(size==2000000)
   	   	//	alert("It takes a while to run 2m entries")
   	   	document.getElementById("selection_insertion").innerHTML="sorting.."	
	   	var xmlHttp = new XMLHttpRequest();
	  	theUrl = "http://127.0.0.1:8000/selection.py?param1="+String(size)
	    xmlHttp.open( "GET", theUrl, true); // false for synchronous request
	    xmlHttp.onreadystatechange=function()
		  {
		  if (xmlHttp.readyState==4 && xmlHttp.status==200)
		    {
		    //alert("hey")
		    document.getElementById("selection_insertion").innerHTML=xmlHttp.responseText;
		      //var parse = JSON.parse(xmlHttp.responseText);
		      //alert(parse)
		    }
		  }

	    xmlHttp.send( null );

   }
   function Bubble(size){
   		//if(size==2000000)
   	   	//	alert("It takes a while to run 2m entries")
   	   	document.getElementById("bubble_insertiom").innerHTML="sorting.."	
	   	var xmlHttp = new XMLHttpRequest();
	  	theUrl = "http://127.0.0.1:8000/bubble.py?param1="+String(size)
	    xmlHttp.open( "GET", theUrl, true); // false for synchronous request
	    xmlHttp.onreadystatechange=function()
		  {
		  	document.getElementById("bubble_insertiom").innerHTML="sorting.."	
		  if (xmlHttp.readyState==4 && xmlHttp.status==200)
		    {
		    //alert("hey")
		    document.getElementById("bubble_insertiom").innerHTML=xmlHttp.responseText;
		      //var parse = JSON.parse(xmlHttp.responseText);
		      //alert(parse)
		    }
		  }

	    xmlHttp.send( null );
   }
   function Shell(size){
   		//	if(size==2000000)
   	   	//	alert("It takes a while to run 2m entries")
   	   	document.getElementById("shell_insertiom").innerHTML="sorting.."	
	   	var xmlHttp = new XMLHttpRequest();
	  	theUrl = "http://127.0.0.1:8000/shell.py?param1="+String(size)
	    xmlHttp.open( "GET", theUrl, true); // false for synchronous request
	    xmlHttp.onreadystatechange=function()
		  {
		  document.getElementById("shell_insertiom").innerHTML="sorting.."	
		  if (xmlHttp.readyState==4 && xmlHttp.status==200)
		    {
		    //alert("hey")
		    document.getElementById("shell_insertiom").innerHTML=xmlHttp.responseText;
		      //var parse = JSON.parse(xmlHttp.responseText);
		      //alert(parse)
		    }
		  }

	    xmlHttp.send( null );
   }
   function Merge(size){
   		//if(size==2000000 ||size==1000000)
   	   	//	alert("It takes a while to run 2m entries")
   	   	document.getElementById("merge_insertiom").innerHTML="sorting.."	
	   	var xmlHttp = new XMLHttpRequest();
	  	theUrl = "http://127.0.0.1:8000/merge.py?param1="+String(size)
	    xmlHttp.open( "GET", theUrl, true); // false for synchronous request
	    xmlHttp.onreadystatechange=function()
		  {
		   	document.getElementById("merge_insertiom").innerHTML="sorting.."	
		  if (xmlHttp.readyState==4 && xmlHttp.status==200)
		    {
		    //alert("hey")
		    document.getElementById("merge_insertiom").innerHTML=xmlHttp.responseText;
		      //var parse = JSON.parse(xmlHttp.responseText);
		      //alert(parse)
		    }
		  }

	    xmlHttp.send( null );
   }
   function Quick(size){
		// 	if(size==2000000 ||size==1000000)
	   	//	alert("It takes a while to run 2m entries")
   	   	document.getElementById("quick_insertiom").innerHTML="sorting.."	
	   	var xmlHttp = new XMLHttpRequest();
	  	theUrl = "http://127.0.0.1:8000/quick.py?param1="+String(size)
	    xmlHttp.open( "GET", theUrl, true); // false for synchronous request
	    xmlHttp.onreadystatechange=function()
		  {
		  document.getElementById("quick_insertiom").innerHTML="sorting.."
		  if (xmlHttp.readyState==4 && xmlHttp.status==200)
		    {
		    //alert("hey")
		    document.getElementById("quick_insertiom").innerHTML=xmlHttp.responseText;
		      //var parse = JSON.parse(xmlHttp.responseText);
		      //alert(parse)
		    }
		  }

	    xmlHttp.send( null );
   }
   function Quick3(size){
   //	if(size==2000000 ||size==1000000)
	 //  		alert("It takes a while to run 2m entries")
   	   	document.getElementById("quick3_insertiom").innerHTML="sorting.."	
	   	var xmlHttp = new XMLHttpRequest();
	  	theUrl = "http://127.0.0.1:8000/quick3.py?param1="+String(size)
	    xmlHttp.open( "GET", theUrl, true); // false for synchronous request
	    xmlHttp.onreadystatechange=function()
		  {
		  document.getElementById("quick3_insertiom").innerHTML="sorting.."
		  if (xmlHttp.readyState==4 && xmlHttp.status==200)
		    {
		    //alert("hey")
		    document.getElementById("quick3_insertiom").innerHTML=xmlHttp.responseText;
		      //var parse = JSON.parse(xmlHttp.responseText);
		      //alert(parse)
		    }
		  }

	    xmlHttp.send( null );
   }

   function typeofsorting(type){

    d= document.getElementsByTagName("input")
    var size=0;
    for(var i=0; i<d.length;i++){
    	if(d[i].name=='group1' && d[i].checked)
    		size = d[i].value
    }
    //alert(size)
    //alert(type)
    switch(type){
    	case "Insertion":
    		insertion(size)
    	break;
        case "selection":

        	selection(size)
    	break;
    	case "Bubble":
    		Bubble(size)
    	break;
    	case "Shell":
    		Shell(size)
    	break;
    	case "Merge":
    		Merge(size)
    	break;
    	case "Quick":
    		 Quick(size)
    	break;
    	case "Quick3":
    		Quick3(size)
    	break;
    	default:
    	  alert("node of the code got selected")
    		
    }

   
    
   }
 </script>



  <h3> Comparing sorting Algorithms </h3>
  <div align="left">
        <p>Size of the sample set</p>
		<input type="radio" name="group1" value="10" > 10</input>
		<input type="radio" name="group1" value="100" checked> 100</input>
		<input type="radio" name="group1" value="1000" >1000 </input>
		<input type="radio" name="group1" value="10000" >10000 </input>
		<input type="radio" name="group1" value="2000000" >1000000 </input>
		<input type="radio" name="group1" value="2000000" >2000000 </input>
</div>
<br>
  <table style="width:100%">
    <tr>
	    <td>Algorithms</td>
	  	<td>Time Taken(milli seconds)</td>
	  	
	  	
  	</tr>
   	<tr>
  		<td><input type="button" name="group2" value="Insertion" onclick="typeofsorting('Insertion')"></input></td>
  		<td id="random_insertiom">0.0</td>
	  	

  	</tr>
  	<tr>
  		<td><input type="button" name="group2" value="selection" onclick="typeofsorting('selection')"></input></td>
  		<td id="selection_insertion">0.0</td>
	  	

  	</tr>
  	<tr>
  		<td><input type="button" name="group2" value="Bubble" onclick="typeofsorting('Bubble')"></input></td>
  		<td id="bubble_insertiom">0.0</td>
	  	

  	</tr>
  	<tr>
  		<td><input type="button" name="group2" value="Shell" onclick="typeofsorting('Shell')"></input></td>
  		<td id="shell_insertiom">0.0</td>
	  	

  	</tr>
  	<tr>
  		<td><input type="button" name="group2" value="Merge" onclick="typeofsorting('Merge')"></input></td>
  		<td id="merge_insertiom">0.0</td>
	  
  	</tr>
    <tr>
  		<td><input type="button" name="group2" value="Quick" onclick="typeofsorting('Quick')"></input></td>
  		<td id="quick_insertiom">0.0</td>
	  	

  	</tr>

    <tr>
  		<td><input type="button" name="group2" value="Quick3" onclick="typeofsorting('Quick3')"></input></td>
  		<td id="quick3_insertiom">0.0</td>
	  	

  	</tr>


  </table>
  

</body>

</html>
"""