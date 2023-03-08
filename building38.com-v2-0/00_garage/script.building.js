function hi_there(){
RightNow = new Date();
document.write((RightNow.getMonth()+1) + "." + RightNow.getDate() + "." + RightNow.getFullYear());
}

function palurl(){
	var url = document.palurlform.palurlselect.options[document.palurlform.palurlselect.options.selectedIndex].value;
	if(url != "")
		window.open(url,'palurlselect','directories=no,location=yes,menubar=yes,resizeable=yes,scrollbars=yes,status=yes,toolbar=yes');
	document.palurlform.palurlselect.options[0].selected = true;
}

function wowy(){
	var url = document.wowyform.wowyselect.options[document.wowyform.wowyselect.options.selectedIndex].value;
	if(url != "")
		window.open(url,'wowyselect','directories=no,location=yes,menubar=yes,resizeable=yes,scrollbars=yes,status=yes,toolbar=yes');
	document.wowyform.wowyselect.options[0].selected = true;
}

function graphics(){
	this.parent.location=this.document.graphicsform.graphicsselect.options[this.document.graphicsform.
graphicsselect.selectedIndex].value;
}

function beauxarts(){
	this.parent.location=this.document.beauxartsform.beauxartsselect.options[this.document.beauxartsform.
beauxartsselect.selectedIndex].value;
}

function photos(){
	this.parent.location=this.document.photosform.photosselect.options[this.document.photosform.
photosselect.selectedIndex].value;
}

function experimentals(){
	this.parent.location=this.document.experimentalsform.experimentalsselect.options[this.document.experimentalsform.
experimentalsselect.selectedIndex].value;
}

function information(){
	this.parent.location=this.document.informationform.informationselect.options[this.document.informationform.
informationselect.selectedIndex].value;
}

{link01on = new Image;
 link01on.src = "../../img/nav_arrow_previous.ani.gif";
 link02on = new Image;
 link02on.src = "../../img/nav_arrow_next.ani.gif";
 link03on = new Image;
 link03on.src = "../../img/nav_arrow_random.ani.gif";
 link04on = new Image;
 link04on.src = "../../img/nav_arrow_down.ani.gif";
 link05on = new Image;
 link05on.src = "../../img/nav_arrow_down.ani.gif";
 
 link01off = new Image;
 link01off.src = "../../img/nav_arrow_previous.gif";
 link02off = new Image;
 link02off.src = "../../img/nav_arrow_next.gif";
 link03off = new Image;
 link03off.src = "../../img/nav_arrow_random.gif";
 link04off = new Image;
 link04off.src = "../../img/nav_arrow_down.gif";
 link05off = new Image;
 link05off.src = "../../img/nav_arrow_down.gif";
 
 }
 
function img_on(imgName)
 {imgOn = eval(imgName + "on.src");
  document [imgName].src = imgOn;}

function img_off(imgName)
 {imgOff = eval(imgName + "off.src");
  document [imgName].src = imgOff;}

function top_nav(){
document.write("<td align='left' valign='top'><table cellpadding='0' cellspacing='0' border='0' width='100%' height='100%'><!-- content -->");
document.write("<tr>");
document.write("<td align='left' valign='top'><table cellpadding='0' cellspacing='0' border='0' width='100%' height='28' class='table-nav'><!-- nav -->");
document.write("<tr>");
document.write("<td align='left'><table cellpadding='0' cellspacing='0' border='0' width='680'>");
  document.write("<tr>");
  document.write("<td><a href='/site/building38' name='top'><img src='../../img/name_dark.grey.gif' width='247' height='33' alt='' border='0'></a><br><div class='content' style='color:#666666'; font-weight:bold;>&nbsp;&nbsp;&nbsp;&nbsp;constructing+deconstructing+experimenting+good music = play</div></td>");
    document.write("<td align='right'><table cellpadding='0' cellspacing='0' border='0'>");
      document.write("<tr>");
      document.write("<td><img src='../../img/spacer.gif' width='7' height='3' alt='' border='0'>");
      document.write("</tr>");
      document.write("<tr>");
      document.write("<td valign='middle'><a href='/site/building38/01_welcome/homepage/index/01.html' class='top-nav-text'>&nbsp;&nbsp;<img src='../../img/top_nav_img.gif' width='10' height='10' alt='' border='0'>");
      document.write("&nbsp;&nbsp;home&nbsp;&nbsp;<img src='../../img/spacer.gif' width='1' height='12' alt='' border='0'></a></td>");
      document.write("</tr>");
      document.write("<tr>");
      document.write("<td><img src='../../img/spacer.gif' width='7' height='3' alt='' border='0'>");
      document.write("</tr>");
      document.write("<tr>");
      document.write("<td valign='middle'><a href='/site/building38/01_welcome/informations/contact/01.html' class='top-nav-text'>&nbsp;&nbsp;<img src='../../img/top_nav_img.gif' width='10' height='10' alt='' border='0'>");
      document.write("&nbsp;&nbsp;contact&nbsp;&nbsp;<img src='../../img/spacer.gif' width='1' height='12' alt='' border='0'></a></td>");
      document.write("</tr>");
      document.write("<tr>");
      document.write("<td><img src='../../img/spacer.gif' width='7' height='3' alt='' border='0'>");
      document.write("</tr>");
      document.write("<tr>");
      document.write("<td valign='middle'><a href='#' class='top-nav-text'>&nbsp;&nbsp;<img src='../../img/spacer.gif' width='10' height='10' alt='' border='0'>");
      document.write("&nbsp;&nbsp;<script>hi_there()</script>&nbsp;&nbsp;<img src='../../img/spacer.gif' width='1' height='12' alt='' border='0'></a></td>");
      document.write("</tr>");
    document.write("</table></td>");
  document.write("</table></td>");
document.write("</tr>");
document.write("<tr>");
document.write("<td><img src='../../img/spacer.gif' width='10' height='9' alt='' border='0'></td>");
document.write("</tr>");
document.write("<tr>");
document.write("<td valign='top'><table cellpadding='0' cellspacing='0' border='0' height='25'><!-- pulldown -->");
document.write("<tr>");

document.write("<td><img src='../../img/spacer.gif' width='18' height='1' alt='' border='0'></td>");
document.write("<td><form name='graphicsform'><select name='graphicsselect' onChange='graphics()'>");
document.write("<option value='#'>graphics</option>");

document.write("<option value='/site/building38/01_welcome/graphics/ads/01.html'>-- Ads</option>");
document.write("<option value='/site/building38/01_welcome/graphics/brochures_booklets/01.html'>-- Brochures/Booklests</option>");
document.write("<option value='/site/building38/01_welcome/graphics/illustrations/01.html'>-- Illustrations</option>");
document.write("<option value='/site/building38/01_welcome/graphics/logos/01.html'>-- Logos</option>");
document.write("<option value='/site/building38/01_welcome/graphics/cd/01.html'>-- CD</option>");
document.write("<option value='/site/building38/01_welcome/graphics/posters/01.html'>-- Posters</option>");
document.write("<option value='/site/building38/01_welcome/graphics/http/01.html'>-- Http://</option></select></form></td>");

document.write("<td><img src='../../img/spacer.gif' width='10' height='1' alt='' border='0'></td>");
document.write("<td><form name='beauxartsform'><select name='beauxartsselect' onChange='beauxarts()'>");
document.write("<option value='#'>beaux arts</option>");

document.write("<option value='/site/building38/01_welcome/beaux_arts/ceramics97/01.html'>-- Ceramics  97</option>");
document.write("<option value='/site/building38/01_welcome/beaux_arts/ceramics98/01.html'>-- Ceramics  98</option>");
document.write("<option value='/site/building38/01_welcome/beaux_arts/paintings95_96/01.html'>-- Paintings 95_96</option>");
document.write("<option value='/site/building38/01_welcome/beaux_arts/paintings97_98/01.html'>-- Paintings 97_98</option></select></form></td>");

// document.write("<td><img src='../../img/spacer.gif' width='10' height='1' alt='' border='0'></td>");
// document.write("<td><form name='photosform'><select name='photosselect' onChange='photos()'>");
// document.write("<option value='#'>photos</option>");

// document.write("<option value='/site/building38/01_welcome/photos/from_the_milk_cart_vault/01.html'>-- from the milk cart vault</option>");
// document.write("<option value='/site/building38/01_welcome/photos/07.01/01.html'>-- 07.01</option>");
// document.write("<option value='/site/building38/01_welcome/photos/08.01/01.html'>-- 08.01</option></select></form></td>");

document.write("<td><img src='../../img/spacer.gif' width='10' height='1' alt='' border='0'></td>");
document.write("<td><form name='experimentalsform'><select name='experimentalsselect' onChange='experimentals()'>");
document.write("<option value='#'>experimentals</option>");

document.write("<option value='/site/building38/01_welcome/experimentals/00_laboratory/01.html'>-- 00 Laboratory</option>");
document.write("<option value='/site/building38/01_welcome/experimentals/kevin/01.html'>-- Kevy</option>");
document.write("<option value='/site/building38/01_welcome/experimentals/hal/01.html'>-- Hal</option></select></form></td>");

document.write("<td><img src='../../img/spacer.gif' width='10' height='1' alt='' border='0'></td>");
document.write("<td><form name='informationform'><select name='informationselect' onChange='information()'>");
document.write("<option value='#'>information</option>");

document.write("<option value='/site/building38/01_welcome/informations/resume/01.html'>-- Resume</option>");
document.write("<option value='/site/building38/01_welcome/informations/contact/01.html'>-- Contact</option></select></form></td>");
document.write("</tr>");
document.write("</table></td><!-- pulldown -->");
document.write("</tr>");
document.write("</table></td><!-- /nav -->");
document.write("</tr>");
}

function end_one(){
document.write("</tr>");
document.write("</table></td><!-- /sub nav -->");
document.write("</tr>");
document.write("</table></div></td><!-- /bottom nav -->");
}

function end_two(){
document.write("</tr>");
document.write("</table></td><!-- /content -->");
document.write("</tr>");
document.write("</table><!-- /parent -->");
}
