import argparse
import os
import shutil
import pathlib
import dload


TEMPLATE_DATA_DIR = os.path.join(os.path.expanduser('~'), 'mkignore')
MASTER_ZIP_URL = 'https://github.com/github/gitignore/archive/master.zip'


def create_parser():
    parser = argparse.ArgumentParser(
        prog='mkignore',
        description='Generate .gitignore files',
    )

    parser.add_argument('-g, --generate', dest='generate', action='store_true', help='Generate .gitignore')
    parser.add_argument('-u, --update', dest='update', action='store_true', help='Update available .gitignore templates')
    parser.add_argument('-l, --list', dest='list', action='store_true', help='List available .gitignore templates')

    parser.add_argument('templates', metavar='TEMPLATES', type=str, nargs='*')

    return parser


def get_templates():
    templates = []

    for path in pathlib.Path(TEMPLATE_DATA_DIR).rglob('*.gitignore'):
        templates.append({
            'name': path.name[:-10],
            'path': path,
        })

    templates = sorted(templates, key=lambda template: template['name'])

    return templates


def update_templates():
    shutil.rmtree(TEMPLATE_DATA_DIR, ignore_errors=True)
    os.mkdir(TEMPLATE_DATA_DIR)

    dload.save_unzip(MASTER_ZIP_URL, TEMPLATE_DATA_DIR)



def generate_gitignore(templates):
    templates = [template.lower() for template in templates]

    gitignore = '# Generated with mkignore - https://github.com/EClaesson/mkignore \n\n'

    for template in get_templates():
        if template['name'].lower() in templates:
            gitignore += '##### ' + template['name'] + ' ' + ('#' * (40 - len(template['name']))) + '\n'
            gitignore += open(template['path'], 'r').read()
            gitignore += '\n\n'

    return gitignore


def main():
    args_parser = create_parser()
    args = args_parser.parse_args()

    if args.generate:
        print(generate_gitignore(args.templates))
    elif args.update:
        print('Updating templates...')
        update_templates()
        print('Successfully downloaded {} .gitignore files'.format(len(get_templates())))
    elif args.list:
        for template in get_templates():
            print(template['name'], end=' ')
    else:
        args_parser.print_help()


if __name__ == '__main__':
    main()