import sys

from jinja2 import Environment, PackageLoader

from render_experiments.utils import generate_things, get_execution_time


def main(num_things):
    """
    Render `include_in_for_loop.html` with a list of of items with length
    `num_things`.
    """
    env = Environment(loader=PackageLoader('render_experiments', 'templates'))
    template = env.get_template('include_in_for_loop.html')
    context = {'many_things': generate_things(num_things)}
    print get_execution_time(template.render, context)


if __name__ == '__main__':
    num_things = int(sys.argv[1])
    main(num_things)
