#! /usr/bin/python

import argparse
from datetime import date, datetime

POSTS_FOLDER = './_posts/'


def create_file(dir, content):
    print('Creating file %s...' % (content['title']))
    with open(dir, 'w') as f:
        f.write('---\r\n')
        for key in content:
            f.write('%s: %s\r\n' % (key, content[key]))
        f.write('---\r\n')


def create_post(args):
    title = args.name.replace(' ', '-')
    dir = POSTS_FOLDER + date.today().isoformat() + '-' + title + '.md'
    content = {}
    content['title'] = args.name
    content['layout'] = 'post'
    content['date'] = datetime.now().strftime('%Y-%m-%d %H:%M %z')
    if args.categories:
        content['categories'] = args.categories
    if args.tags:
        content['tags'] = args.tags
    create_file(dir, content)


def create_page(args):
    dir = './' + args.name + '.md'
    content = {}
    content['title'] = args.name
    content['layout'] = args.layout
    if args.permalink:
        content['permalink'] = args.permalink
    if args.fields:
        fields = fields.split()
        fields_iter = iter(fields[:-1])
        for el in fields_iter:
            content[el] = fields_iter.nex()
    create_file(dir, content)


parser = argparse.ArgumentParser(
    description='Create posts and pages for Jekyll blogs')
subparsers = parser.add_subparsers()

parser_post = subparsers.add_parser('post')
parser_post.set_defaults(func=create_post)
parser_post.add_argument('name')
parser_post.add_argument('--tags', action='store', help='Post Tags')
parser_post.add_argument('--categories',
                         action='store',
                         help='Post Categories')

parser_page = subparsers.add_parser('page')
parser_page.set_defaults(func=create_page)
parser_page.add_argument('name')
parser_page.add_argument('--layout',
                         action='store',
                         required=True,
                         help='Page Layout')
parser_page.add_argument('--permalink', action='store', help='Page Permalink')
parser_page.add_argument(
    '--fields',
    action='store',
    help='Additional fields to page header e.g. order 1 publish false')

args = parser.parse_args()
args.func(args)
