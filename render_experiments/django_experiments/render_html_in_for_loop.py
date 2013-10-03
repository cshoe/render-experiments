import sys

from django.template.loader import render_to_string

from render_experiments.utils import generate_things


def main(num_things):
    """
    Render `html_in_for_loop.html` with a list of of items with length
    `num_things`.
    """
    many_things = generate_things(num_things)
    context = {'many_things': many_things}
    content  = render_to_string('html_in_for_loop.html', context)


if __name__ == '__main__':
    num_things = int(sys.argv[1])
    main(num_things)
