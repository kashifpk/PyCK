<%
dojo_base = request.registry.settings.get('dojo_base', 'http://ajax.googleapis.com/ajax/libs/dojo/1.10.4')
%>
<!DOCTYPE html>
<html>
<head>
    <title>${self.title()}</title>

	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="/static/bootstrap/css/bootstrap.min.css">
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap/js/bootstrap.min.js"></script>
	
	<!-- Optional theme -->
	<link rel="stylesheet" href="/static/bootstrap/css/bootstrap-theme.min.css">
	

	<link rel="stylesheet" href="${dojo_base}/dojo/resources/dojo.css" type="text/css" charset="utf-8" />
    <link rel="stylesheet" href="${dojo_base}/dijit/themes/claro/claro.css" type="text/css" charset="utf-8" />
    <script src="${dojo_base}/dojo/dojo.js" data-dojo-config="async: true"></script>
    <script type="text/javascript">
          require(['dojo/parser', 'dojo/domReady'],function(parser,ready){ready(function(){
            parser.parse();
            });});
    </script>
	${self.meta()}
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
<div class="panel panel-primary">
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
    
    %if flash_msgs:
      %for flash_msg in flash_msgs:
        <%
        alert_type = 'info'
        if flash_msg.lower().startswith("error:"):
          alert_type = 'danger'
          flash_msg = flash_msg[6:]
        elif flash_msg.lower().startswith("warning:"):
          alert_type = 'warning'
          flash_msg = flash_msg[8:]
        %>
        
        <div class="alert alert-${alert_type}">
          ${flash_msg}
          <a class="close" onclick="$(this).parent().hide()">×</a> 
        </div>
      %endfor
    %endif

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

	%if dict == type(models):
		%if '__main__' in models:
			%for model in models['__main__']:
				<%
				row_class = ""
				if request.route_url(route_prefix + model.__name__ + 'CRUD_list') == request.current_route_url().split('?')[0]:
					row_class = "active"
				%>
				
				<li class="${row_class}">
					<a href="${request.route_url(route_prefix + model.__name__ + 'CRUD_list')}">${model.__tablename__.replace("_", " ").title().replace(" ", "&nbsp;")|n}
					%if model_record_counts:
					<span class="badge">${model_record_counts[model.__tablename__]}</span>
					%endif
					</a>
				</li>
				
			%endfor
		%endif
		
		%for appname, app_models in list(models.items()):
			%if '__main__' != appname:
				<h2 class="info">${appname.replace("_", " ").title().replace(" ", "&nbsp;")|n}</h2>
				%for model in models[appname]:
					<%
					row_class = ""
					if request.route_url(route_prefix + model.__name__ + 'CRUD_list') == request.current_route_url():
						row_class = "active"
					%>
					
					<li class="${row_class}"><a href="${request.route_url(route_prefix + model.__name__ + 'CRUD_list')}">${model.__tablename__[len(appname)+1:].replace("_", " ").title().replace(" ", "&nbsp;")|n}</a></li>
					
				%endfor
			%endif
		%endfor
		
	%else:
		%for model in models:
			<%
			row_class = ""
			if request.route_url(route_prefix + model.__name__ + 'CRUD_list') == request.current_route_url():
				row_class = "active"
			%>
			
			<li class="${row_class}"><a href="${request.route_url(route_prefix + model.__name__ + 'CRUD_list')}">${model.__tablename__.replace("_", " ").title().replace(" ", "&nbsp;")|n}</a></li>
			
		%endfor
	%endif
</ul>


</%def>
