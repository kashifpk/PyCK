<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
  
    <title>${self.title()}</title>
    ${self.meta()}
  
    <!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
	
	<!-- Optional theme -->
	<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap-theme.min.css">

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
	<div class="row">
		<div class="col-md-12">
			${self.header()}
		</div>
	</div>
	<div class="row">
		<div class="col-md-3">${self.side_menu()}</div>
		<div class="col-md-9">${self.content_wrapper()}</div>
	</div>
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
<div class="panel panel-default">
  <!-- Default panel contents -->
  <div class="panel-heading">
	
	<h1><a href="/"><span class="glyphicon glyphicon-home"></span></a> &nbsp;
	<span class="glyphicon glyphicon-fire"></span> Admin Interface</h1>
  </div>

</div>

</%def>
  
<%def name="content_wrapper()">
  <div id="content">
	<% flash_msgs = request.session.pop_flash() %>
	
	%for flash_msg in flash_msgs:
	  <div class="alert alert-success">
        ${flash_msg}
      </div>
	%endfor
    
  ${self.body()}
  </div>
</%def>
    
<%def name="side_menu()">
<ul class="nav nav-pills nav-stacked">
	<%
    row_class = ""
    if request.route_url(route_prefix + 'admin_index') == request.current_route_url():
        row_class = "active"
    %>
	<li class="${row_class}"><a href="${request.route_url(route_prefix + 'admin_index')}">Admin Home</a></li>

	%for model in models:
		<%
		row_class = ""
		if request.route_url(route_prefix + model.__name__ + 'CRUD_list') == request.current_route_url():
			row_class = "active"
		%>
		
		<li class="${row_class}"><a href="${request.route_url(route_prefix + model.__name__ + 'CRUD_list')}">${model.__tablename__.replace("_", " ").title().replace(" ", "&nbsp;")|n}</a></li>
		
	%endfor	
</ul>


</%def>
