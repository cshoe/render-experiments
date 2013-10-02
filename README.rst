The idea for this little project came from looking at the templates for
a Django project I was working on. In one of the templates, I came across
a section that looked like:

::

    {% for thing in many_things %}
        {% include "template_that_renders_a_single_thing.html" %}
    {% endfor %}

I found myself wondering, "Is there any performance impact in having an
include statement in a for loop versus having the HTML directly in the for
loop?".

If you're confused, this is what I mean by "directly in the for loop":

::

    {% for thing in many_things %}
        <li>
            {{ thing.name }} is going to {{ thing.place }}.
        </li>
    {% endfor %}

After mentioning my curiosity to a coworker, he suggested throwing
`Jinja <http://jinja.pocoo.org/>`_ in the mix. So, we'll be running some
experiments with the Django templating engine and Jinja.
