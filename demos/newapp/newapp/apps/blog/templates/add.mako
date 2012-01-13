<%inherit file="/base.mako"/>

<%def name="title()">
The Blog app
</%def>

<div>
  <div class="middle align-center">
    <p class="app-welcome">
    <img src="${request.static_url(APP_BASE + ':static/webapp.png')}" />  Welcome to Blog app
    </p>
    <a href="${request.route_url(APP_NAME + '.home')}">Back To Home</a> 
  </div>
  <h1>Add a Post</h1>
  <form action="${request.route_url(APP_NAME + '.add')}" method="POST">
  ${form.as_p() | n}
  <br />
  <input type="submit" name="form.submitted" value="Add Post" />
  </form>
</div>

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />