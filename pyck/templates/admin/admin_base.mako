<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
  
  <title>${self.title()}</title>
  ${self.meta()}
  <style type="text/css">
  .admin_header {
    background-color: #272626;
    color: #00AEFF;
    text-align: center;
    
  }
  
  .admin_side_menu{
    background-color: #272626;
    color: #EAFFFC;
    text-align: center;
    width: 20%;
    
  }
  
  .admin_footer{
    background-color: #272626;
    color: #EAFFFC;
    text-align: center;
    
  }
  
  </style>
  
</head>

<body class="${self.body_class()}" ${self.body_attrs()}>
  <div id="wrap">
    <table width="100%" cellspacing="0">
        <tr class="admin_header">
            <td colspan="2">
                ${self.header()}
            </td>
        </tr>
        <tr>
            <td class="admin_side_menu" valign="top">
                ${self.side_menu()}
            </td>
            <td class="admin_page_content">
                ${self.content_wrapper()}
            </td>
        </tr>
        <tr class="admin_footer">
            <td colspan="2">
                ${self.footer()}
            </td>
        </tr>
    </table>
  </div>
</body>
</html>
<%def name="title()">Admin - The PyCK Web Application Development Framework</%def>

<%def name="meta()">
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="PyCK web application" />
</%def>

<%def name="body_class()">
</%def>
<%def name="body_attrs()">
</%def>
<%def name="header()">
  <h1>Admin Interface</h1>
</%def>
  
<%def name="content_wrapper()">
  <div id="content">
    <div class="flash">
      <% flash_msgs = request.session.pop_flash() %>
      
      %for flash_msg in flash_msgs:
        ${flash_msg}<br />
      %endfor
    </div>
  ${self.body()}
  </div>
</%def>
    
<%def name="side_menu()">
<p>
  Side links come here
</p>
</%def>
<%def name="footer()">
  <div id="footer">
    <div class="footer">&copy; Copyright 2008-2012, Set your company name here</div>
  </div>
</%def>
    
  
  
</body>
</html>
