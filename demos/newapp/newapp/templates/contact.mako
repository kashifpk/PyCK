<%inherit file="base.mako"/>

<%def name="title()">
PyCK Project - Contact Us
</%def>

<div>
<h1>Contact Us</h1>

<form action="${request.route_url('contact')}" method="POST">
<input type="hidden" name="csrf_token" value="${csrf_token}" />
    ${contact_form.as_p() | n}
    <input type="submit" name="form.submitted" value="Send Email" />
</form>
<br /><br /><br /><br /><br /><br />
</div>'