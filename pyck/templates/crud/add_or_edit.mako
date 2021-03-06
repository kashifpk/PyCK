<%inherit file="${context.get('base_template')}" />

<div class="panel panel-primary">
  <!-- Default panel contents -->
  <div class="panel-heading">
		<h3 class="panel-title">${action_type.title()} ${friendly_name}</h3>
  </div>

  <div class="panel-body">
    <form action="${request.current_route_url()}" method="POST" role="form">
    ${form.as_p(errors="right") | n}
    <br />
    <input class="btn btn-success" type="submit" name="form.submitted" value="${action_type.title()} ${friendly_name}" />
    </form>
  </div>
</div>

