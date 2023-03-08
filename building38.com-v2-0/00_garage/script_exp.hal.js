function go_to(url) { 
window.location=url;
}
function rand_link() {
var a;
a = 1+Math.round(Math.random()*5);
if (a==1) go_to("01.html");
if (a==2) go_to("02.html");
if (a==3) go_to("03.html");
if (a==4) go_to("04.1.html");
if (a==5) go_to("05.html");
}

function nav(){
document.write("<tr>");
document.write("<td><img src='../../img/spacer.gif' width='10' height='5' alt='' border='0'></td>");
document.write("<tr>");
document.write("<td><table cellpadding='0' cellspacing='0' border='0'><!-- sub nav-->");
document.write("<tr>");

document.write("<td><table cellpadding='0' cellspacing='0' border='0' width='20' height='20'><!-- specail spacer -->");
document.write("<tr>");
document.write("<td align='left'><img src='../../img/spacer.gif' width='10' height='33' alt='' border='0'></td>");
document.write("</tr>");
document.write("</table></td><!-- /special spacer -->");

document.write("<td><table cellpadding='0' cellspacing='0' border='0' background='../../img/block_ground.exp.gif' width='20' height='20'><!--1 button -->");
document.write("<tr>");
document.write("<td align='left'><img src='../../img/block_left.exp.gif' width='1' height='20' alt='' border='0'></td>");
document.write("<td align='center'><a href='01.html' class='vertwo'>1</a></td>");
document.write("<td align='right'><img src='../../img/block_right.exp.gif' width='2' height='20' alt='' border='0'></td>");
document.write("</tr>");
document.write("</table></td><!-- /button -->");
document.write("<td><img src='../../img/spacer.gif' width='10' height='20' alt='' border='0'></td>");
document.write("<td><table cellpadding='0' cellspacing='0' border='0' background='../../img/block_ground.exp.gif' width='20' height='20'><!--2 button -->");
document.write("<tr>");
document.write("<td align='left'><img src='../../img/block_left.exp.gif' width='1' height='20' alt='' border='0'></td>");
document.write("<td align='center'><a href='02.html' class='vertwo'>2</a></td>");
document.write("<td align='right'><img src='../../img/block_right.exp.gif' width='2' height='20' alt='' border='0'></td>");
document.write("</tr>");
document.write("</table></td><!-- /button -->");
document.write("<td><img src='../../img/spacer.gif' width='10' height='20' alt='' border='0'></td>");
document.write("<td><table cellpadding='0' cellspacing='0' border='0' background='../../img/block_ground.exp.gif' width='20' height='20'><!--3 button -->");
document.write("<tr>");
document.write("<td align='left'><img src='../../img/block_left.exp.gif' width='1' height='20' alt='' border='0'></td>");
document.write("<td align='center'><a href='03.html' class='vertwo'>3</a></td>");
document.write("<td align='right'><img src='../../img/block_right.exp.gif' width='2' height='20' alt='' border='0'></td>");
document.write("</tr>");
document.write("</table></td><!-- /button -->");
document.write("<td><img src='../../img/spacer.gif' width='10' height='20' alt='' border='0'></td>");
document.write("<td><table cellpadding='0' cellspacing='0' border='0' background='../../img/block_ground.exp.gif' width='20' height='20'><!--4 button -->");
document.write("<tr>");
document.write("<td align='left'><img src='../../img/block_left.exp.gif' width='1' height='20' alt='' border='0'></td>");
document.write("<td align='center'><a href='04.1.html' class='vertwo'>4</a></td>");
document.write("<td align='right'><img src='../../img/block_right.exp.gif' width='2' height='20' alt='' border='0'></td>");
document.write("</tr>");
document.write("</table></td><!-- /button -->");
document.write("<td><img src='../../img/spacer.gif' width='10' height='20' alt='' border='0'></td>");
document.write("<td><table cellpadding='0' cellspacing='0' border='0' background='../../img/block_ground.exp.gif' width='20' height='20'><!--5 button -->");
document.write("<tr>");
document.write("<td align='left'><img src='../../img/block_left.exp.gif' width='1' height='20' alt='' border='0'></td>");
document.write("<td align='center'><a href='05.html' class='vertwo'>5</a></td>");
document.write("<td align='right'><img src='../../img/block_right.exp.gif' width='2' height='20' alt='' border='0'></td>");
document.write("</tr>");
document.write("</table></td><!-- /button -->");

}
