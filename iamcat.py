import os, os.path, glob
from mako.template import Template

DOCUMENT_ROOT = os.environ['DOCUMENT_ROOT']
IMAGES_DIR = os.environ['IMAGES_DIR']
TITLE = os.environ['TITLE']

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE = Template(filename=os.path.join(SCRIPT_DIR, 'template.html'))

FILE_PATTERN = os.path.join(IMAGES_DIR, "*")


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])

    print IMAGES_DIR, FILE_PATTERN

    files = [f for f in glob.glob(FILE_PATTERN)
             if os.path.isfile(f)
             and os.path.splitext(f)[-1] in ('.jpg','.png')]
    
    files.sort(key = lambda f: os.path.getmtime(f), reverse=True)
    files = [os.path.relpath(f, DOCUMENT_ROOT) for f in files]

    return [TEMPLATE.render(title=TITLE, files=files).encode("utf-8")]


