<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
  
    <title>${self.title()}</title>
    ${self.meta()}
  
    <style type="text/css">
    /*PyCK styles*/
    body{
      /*background-color: #373535;*/
      background-color: #BBBBBB;
      font-family: verdana;
      min-height: 700px;
    }
    
    div#wrap{
      background-color: #FFFFFF;
      width: 95%;
      margin: 10px auto;
      margin-top: 30px;
    }
    
    .admin_header {
      text-align: center;
      font-size: 16px;
      font-weight: bold;
    }
    
    .admin_side_menu{
      text-align: left;
      vertical-align: top;
      font-weight: bold;
      color: #d7d7d7;
      
      background: #1E1E1E;
      /*width: 20%;*/
      padding: 0px;
      margin: 0px;
      border-width: 0px;
    }
    
    
    
    .admin_side_menu a, .admin_side_menu a:hover, .admin_side_menu a:visited{
        text-decoration: none;
        color: #d7d7d7;
        border-width: 0px;
    }
    
    .admin_side_menu table{
        margin: 0px;
        padding: 0px;
        border-width: 0px;
        margin-left: 10px;
        margin-top: 20px;
    }
    
    .admin_side_menu td{
        margin-right: 0px;
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 10px;
        padding-right: 20px;
        border-width: 0px;
    }
    
    .active_menu, .active_menu a, .active_menu a:hover, .active_menu a:visited{
        text-decoration: none;
        color: #1E1E1E;
        background: #ffffff;
        border-width: 0px;
    }
    
    .admin_page_content{
        width: 100%;
	vertical-align: top;
    }
    .errors {color: #ff0000; font-weight: bold;}
    .flash {background-color: #0E3A00; color: #fff; font-size: 16pt; alignment-adjust: middle; text-align: center}
    
    .tr_heading, .tr_heading th {
      background-color: #1C1C1C;
      color: #E5E5E5;
      font-weight: bold;
    }
    
    .oddrow {
        background-color: #FFFFFF;
        color: black;
    }
    
    .evenrow {
        background-color: #EFEFEF;
        color: black;
    }
    /*.tr_heading th, .oddrow td, .evenrow td { padding: 3px; }*/
    td, th {
        padding: 5px;
        
    }
    
    table, tr {
        border: solid 1px #1E1E1E;
    }
    
    .list-actions {text-align: right; background-color: #1C1C1C; color: #E5E5E5; }
    .list-actions a{text-align: right; background-color: #1C1C1C; color: #E5E5E5; font-weight: bold;}
    
    h1 {
      text-align: center;
    }
    
    /* button 
    ---------------------------------------------- */
    .button {
          
      display: inline-block;
      zoom: 1; /* zoom and *display = ie7 hack for display:inline-block */
      *display: inline;
      vertical-align: baseline;
      margin: 0 2px;
      outline: none;
      cursor: pointer;
      text-align: center;
      text-decoration: none;
      font: 14px/100% Arial, Helvetica, sans-serif;
      padding: .5em 2em .55em;
      text-shadow: 0 1px 1px rgba(0,0,0,.3);
      -webkit-border-radius: .5em; 
      -moz-border-radius: .5em;
      border-radius: .5em;
      -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.2);
      -moz-box-shadow: 0 1px 2px rgba(0,0,0,.2);
      box-shadow: 0 1px 2px rgba(0,0,0,.2);
    }
    .button:hover {
      text-decoration: none;
    }
    .button:active {
      position: relative;
      top: 1px;
    }
    
    .bigrounded {
      -webkit-border-radius: 2em;
      -moz-border-radius: 2em;
      border-radius: 2em;
      font-size: 12pt;
      font-weight: bold;
      font-family: Verdana;
    }
    .medium {
      font-size: 12px;
      padding: .4em 1.5em .42em;
    }
    .small {
      font-size: 11px;
      padding: .2em 1em .275em;
    }
    
    /* color styles 
    ---------------------------------------------- */
    
    /* black */
    .black {
      color: #d7d7d7;
      border: solid 1px #333;
      background: #333;
      background: -webkit-gradient(linear, left top, left bottom, from(#666), to(#000));
      background: -moz-linear-gradient(top,  #666,  #000);
      filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#666666', endColorstr='#000000');
    }
    .black:hover {
      background: #000;
      background: -webkit-gradient(linear, left top, left bottom, from(#444), to(#000));
      background: -moz-linear-gradient(top,  #444,  #000);
      filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#444444', endColorstr='#000000');
    }
    .black:active {
      color: #666;
      background: -webkit-gradient(linear, left top, left bottom, from(#000), to(#444));
      background: -moz-linear-gradient(top,  #000,  #444);
      filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#000000', endColorstr='#666666');
    }
    
    /* gray */
    .gray {
      color: #e9e9e9;
      border: solid 1px #555;
      background: #6e6e6e;
      background: -webkit-gradient(linear, left top, left bottom, from(#888), to(#575757));
      background: -moz-linear-gradient(top,  #888,  #575757);
      filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#888888', endColorstr='#575757');
    }
    .gray:hover {
      background: #616161;
      background: -webkit-gradient(linear, left top, left bottom, from(#757575), to(#4b4b4b));
      background: -moz-linear-gradient(top,  #757575,  #4b4b4b);
      filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#757575', endColorstr='#4b4b4b');
    }
    .gray:active {
      color: #afafaf;
      background: -webkit-gradient(linear, left top, left bottom, from(#575757), to(#888));
      background: -moz-linear-gradient(top,  #575757,  #888);
      filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#575757', endColorstr='#888888');
    }
    
    /* green */
    .green {
      color: #e8f0de;
      border: solid 1px #538312;
      background: #64991e;
      background: -webkit-gradient(linear, left top, left bottom, from(#7db72f), to(#4e7d0e));
      background: -moz-linear-gradient(top,  #7db72f,  #4e7d0e);
      filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#7db72f', endColorstr='#4e7d0e');
    }
    .green:hover {
      background: #538018;
      background: -webkit-gradient(linear, left top, left bottom, from(#6b9d28), to(#436b0c));
      background: -moz-linear-gradient(top,  #6b9d28,  #436b0c);
      filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#6b9d28', endColorstr='#436b0c');
    }
    .green:active {
      color: #a9c08c;
      background: -webkit-gradient(linear, left top, left bottom, from(#4e7d0e), to(#7db72f));
      background: -moz-linear-gradient(top,  #4e7d0e,  #7db72f);
      filter:  progid:DXImageTransform.Microsoft.gradient(startColorstr='#4e7d0e', endColorstr='#7db72f');
    }
    </style>
    <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/dojo/1.8.3/dojo/resources/dojo.css" type="text/css" charset="utf-8" />
    <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/dojo/1.8.3/dijit//themes/claro/claro.css" type="text/css" charset="utf-8" />
    <script src="//ajax.googleapis.com/ajax/libs/dojo/1.8.3/dojo/dojo.js" data-dojo-config="isDebug: true, async: true, parseOnLoad: true"></script>
    <script type="text/javascript">
        require(['dojo/parser', 'dojo/domReady'],function(parser,ready){ready(function(){
          parser.parse();
          });});
    </script>
</head>

<body class="${self.body_class()}" ${self.body_attrs()}>
  <div id="wrap">
    <div class="admin_header black">
      ${self.header()}
    </div>
    <table>
        <tr>
            <td class="admin_side_menu">
              ${self.side_menu()}
            </td>
            <td class="admin_page_content">
                ${self.content_wrapper()}
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

<%def name="body_class()">claro</%def>
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
<table style="width:100%;">
    <%
    row_class = ""
    if request.route_url(route_prefix + 'admin_index') == request.current_route_url():
        row_class = "active_menu"
    %>
    <tr class="${row_class}">
        <td><a href="${request.route_url(route_prefix + 'admin_index')}">Admin&nbsp;Home</a></td>
    </tr>
%for model in models:
    <%
    row_class = ""
    if request.route_url(route_prefix + model.__name__ + 'CRUD_list') == request.current_route_url():
        row_class = "active_menu"
    %>
    <tr class="${row_class}">
        <td><a href="${request.route_url(route_prefix + model.__name__ + 'CRUD_list')}">${model.__tablename__.replace("_", " ").title().replace(" ", "&nbsp;")|n}</a></td>
    </tr>
%endfor
</table>
</%def>
