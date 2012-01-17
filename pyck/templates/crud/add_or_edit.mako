<%inherit file="/base.mako"/>
<%! import itertools %>
<%
row_class_cycler = itertools.cycle(['oddrow', 'evenrow']);
%>

<div class="align-center">
    <h1>${action_type.title()} ${friendly_name}</h1>
    <div class="align-left">
    <form action="${request.current_route_url()}" method="POST">
    ${form.as_p(errors="right") | n}
    <br />
    <input type="submit" name="form.submitted" value="${action_type.title()} ${friendly_name}" />
    </form>
    </div>
</div>
<br /><br /><br /><br /><br /><br />