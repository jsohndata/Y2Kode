<?php
  print
  ("
    <html>
    <head>
    <title>[^_^]</title>
    <script language='javascript'>
    function nav_go()
    {
      var which = this.document.this_form.this_select.options[this.document.this_form.this_select.selectedIndex].value;
      document.here.src = which;
    }
    </script>
    </head>
    
    <body bgcolor='#ffffff' topmargin='0' leftmargin='0' marginwidth='0' marginheight='0'>
    <form name='this_form'>
    <table cellpadding='0' cellspacing='0' border='0' width='100%' height='97%'>
      <tr>
        <td align='center' valign='middle'><table cellpadding='0' cellspacing='0' border='0'>
          <tr>
            <Td valign='top'><img 
              src='spacer.gif'
              width='200' height='1' alt='' border='0'></td>
              
            <td><img src='logo.jpg' width='250' height='81' alt='' border='0'>
              <Br>
              <select name='this_select' onChange='nav_go()'>
                <option value='spacer.gif'>-----></option>
                <option value='print1.jpg'>Print 1:</option>
                <option value='print2.jpg'>Print 2:</option>
                <option value='print3.jpg'>Print 3:</option>
                <option value='web1.jpg'>web 1:</option>
                <option value='web2.jpg'>web 2:</option>
                <option value='web3.jpg'>web 3:</option>
              </select></td>
          </tr>
          
          <tr>
            <td colspan='2'>
            <br>
            <br>
            <img src='spacer.gif' name='here' height='300' alt='' border='0'></td>
          </tr>
        </table></td>
      </tr>
    </table></form></body></html>
  ");
?>
        