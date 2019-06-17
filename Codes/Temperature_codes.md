
* ***Temperature Data Program*** : The programs code.php and code.php who are responsible for receiving the data 
temperature sent by the Arduino boards and store 
them within two text files data.txt and data2.txt.

~~~
************************************ Code.php *******************************
 
<?php
if(!empty ($_GET)) {     
// Temperature recovery function
$message = htmlspecialchars($_GET["temperature"]); 

if(filter_var($message, FILTER_VALIDATE_FLOAT) !== false)  {
$monfichier = fopen(’data.txt’, ’a+’);   
fputs($monfichier,$message."\r\n");   // Save the message in the created file.
fclose($monfichier);    // Closing the file
}
}
?>

********************************** Code2.php *************************************
<?php
if(!empty ($_GET)) {     
// Temperature recovery function
$message = htmlspecialchars($_GET["temperature"]); 

if(filter_var($message, FILTER_VALIDATE_FLOAT) !== false)  {
$monfichier = fopen(’data2.txt’, ’a+’);   
fputs($monfichier,$message."\r\n");   // Save the message in the created file.
fclose($monfichier);    // Closing the file
}
}
?>

~~~