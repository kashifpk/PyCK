<%!
from newapp.auth import is_allowed
%>

<!DOCTYPE html>
<html>
<head>
  
  <title>${self.title()}</title>
  ${self.meta()}
  
  <link rel="shortcut icon" href="${request.static_url('newapp:static/favicon.ico')}" />
  <!-- Bootstrap -->
  <link rel="stylesheet" href="${request.static_url('newapp:static/bootstrap/css/bootstrap.min.css')}">
  <link rel="stylesheet" href="${request.static_url('newapp:static/bootstrap/css/bootstrap-theme.min.css')}">
  
  <!-- Custom CSS -->
  <link rel="stylesheet" href="${request.static_url('newapp:static/pyck.css')}" type="text/css" media="screen" charset="utf-8" />
  
  <!-- Dojo -->
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
  <div class="container">
  ${self.header()}
  
  ${self.content_wrapper()}
  ${self.footer()}
  </div>
</body>
</html>

<%def name="title()">The PyCK Web Application Development Framework</%def>

<%def name="meta()">
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="PyCK web application" />
</%def>

<%def name="body_class()">
claro
</%def>
<%def name="body_attrs()">
</%def>
<%def name="header()">
  <div id="top-small">
    <img src="${request.static_url('newapp:static/pyck-small.png')}"  alt="pyck"/>
    ${self.main_menu()}
  </div>
</%def>
  
<%def name="content_wrapper()">
  <div id="content">
    
    <% flash_msgs = request.session.pop_flash() %>
    
    %for flash_msg in flash_msgs:
      <div class="alert alert-info">
        ${flash_msg}
      </div>
    %endfor
    
  ${self.body()}
  </div>
</%def>
    
<%def name="main_menu()">
<p>
  
  <a href="${request.route_url('home')}">Home</a> |
  <a href="${request.route_url('contact')}">Contact Us</a> |
  %if is_allowed(request, 'pyckauth_manager'):
  <a href="${request.route_url('pyckauth_manager')}">Auth Manager</a> |
  %endif
  
  %if is_allowed(request, 'admin.admin_index'):
  <a href="${request.route_url('admin.admin_index')}">Admin Section</a> |
  %endif
  
  %if request.session.get('logged_in_user', None):
  <a href="${request.route_url('pyckauth_logout')}">Logout</a>
  %else:
  <a href="${request.route_url('pyckauth_login')}">Login</a>
  %endif
  
</p>
</%def>
<%def name="footer()">
  <div id="footer">
    <div class="footer">&copy; Copyright 2008-2012, Set your company name here</div>
  </div>
</%def>

