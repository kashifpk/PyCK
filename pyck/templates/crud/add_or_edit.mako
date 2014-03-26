<%inherit file="${context.get('base_template')}" />

<div class="panel panel-success">
  <!-- Default panel contents -->
  <div class="panel-heading">
	<h1>${action_type.title()} ${friendly_name}</h1>
  </div>

  <div class="panel-body">
    <form action="${request.current_route_url()}" method="POST" role="form">
    ${form.as_p(errors="right") | n}
    <br />
    <input class="btn btn-success" type="submit" name="form.submitted" value="${action_type.title()} ${friendly_name}" />
    </form>
  </div>
</div>

