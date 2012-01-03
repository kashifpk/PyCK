<%inherit file="/base.mako"/>

<%def name="title()">
The WiKi app
</%def>

<div>
  <div class="middle align-center">
    <p class="app-welcome">
    <img src="${request.static_url(APP_BASE + ':static/webapp.png')}" />  Welcome to wiki app
    </p>
  </div>
  <h1>Wiki page title: ${page.title}</h1>
  <p>${page.content}</p>
</div>

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />