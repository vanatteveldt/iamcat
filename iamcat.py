import os, os.path, glob
from mako.template import Template

IMAGES_DIR = "cats" # relative to DOCUMENT_ROOT

DOCUMENT_ROOT = os.environ['DOCUMENT_ROOT']

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE = Template(filename=os.path.join(SCRIPT_DIR, 'template.html'))

FILE_PATTERN = os.path.join(DOCUMENT_ROOT, IMAGES_DIR, "*")

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])

    title = "I am CAT"

    files = [f for f in glob.glob(FILE_PATTERN)
             if os.path.isfile(f)
             and os.path.splitext(f)[-1] in ('.jpg','.png')]
    
    files.sort(key = lambda f: os.path.getmtime(f), reverse=True)
    files = [os.path.relpath(f, DOCUMENT_ROOT) for f in files]

    return [TEMPLATE.render(**locals()).encode("utf-8")]


