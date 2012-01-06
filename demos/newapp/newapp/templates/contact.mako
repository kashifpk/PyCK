<%inherit file="base.mako"/>

<%def name="title()">
PyCK Project - Contact Us
</%def>

<div>
<h1>Contact Us</h1>

<form action="${request.route_url('contact')}" method="POST">
<input type="hidden" name="csrf_token" value="${csrf_token}" />

<table>
    <tr>
        <td>
            ${contact_form.subject.label()}<br />
            %if contact_form.subject.errors:
                <span class="errors">
                %for e in contact_form.subject.errors:
                ${e}<br />
                %endfor
                </span>
            %endif
            ${contact_form.subject()}
            
        </td>
    </tr>
    <tr>
        <td>
            ${contact_form.email.label()}<br />
            %if contact_form.email.errors:
                <span class="errors">
                %for e in contact_form.email.errors:
                ${e}<br />
                %endfor
                </span>
            %endif
            ${contact_form.email()}
            
        </td>
    </tr>
    <tr>
        <td>
            ${contact_form.message.label()}<br />
            %if contact_form.message.errors:
                <span class="errors">
                %for e in contact_form.message.errors:
                ${e}<br />
                %endfor
                </span>
            %endif
            ${contact_form.message(rows=7,cols=50)}
        </td>
    </tr>
    <tr>
        <td>
            <input type="submit" name="form.submitted" value="Send Email" />
        </td>
    </tr>
</table>
</form>
<br /><br /><br /><br /><br /><br />
</div>