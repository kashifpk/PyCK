<%inherit file="base.mako"/>

<%def name="title()">
PyCK Project - Contact Us
</%def>

<div>
<h1>Contact Us</h1>

<form action="${request.route_url('contact')}" method="POST">
    <table cellpadding="5" cellspacing="5">
    ${contact_form.as_table(labels='top', errors='right') | n}
    <tr><td colspan="3" align="center"><input type="submit" name="form.submitted" value="Send Email" /></td></tr>
    </table>
</form>
<br /><br /><br /><br /><br /><br />
</div>