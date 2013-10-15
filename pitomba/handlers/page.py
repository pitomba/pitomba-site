# coding: utf-8
from pitomba import settings
from spriter.sprite import Sprite
from tornado.web import RequestHandler

import os
import random
import string


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        if kwargs.get('context'):
            self.render("%s.html" % kwargs['context'],
                        SERVER_NAME=settings.SERVER_NAME,
                        success=False,
                        message="as many as you want")
        else:
            self.render("index.html", SERVER_NAME=settings.SERVER_NAME)

    def post(self, **kwargs):
        msg = ''
        success = True
        urls_paths = []
        paths = []
        original_names = []

        if not self.request.files.get('file', None):
            if self.request.arguments.get('urls'):
                urls_paths = self.request.arguments['urls'][0].split()

                for url in urls_paths:
                    original_names.append(url.split('/')[-1].split(".")[0])
            else:
                msg = "No file given."
                success = False
        else:
            for r_file in self.request.files.get('file'):
                original_fname = r_file['filename']
                original_names.append(original_fname.split(".")[0])
                extension = os.path.splitext(original_fname)[1]

                if extension != '.png':
                    msg = "Invalid file format: " + extension
                    success = False
                    break

                final_filepath = settings.UPLOAD_PATH + '/' + original_fname

                with open(final_filepath, 'w') as output_file:
                    output_file.write(r_file['body'])

                paths.append(final_filepath)

        fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        fname += '.png'

        sprite = Sprite(paths=paths,
                        urls_paths=urls_paths,
                        sprite_path=settings.STATIC_DEMO_PATH,
                        sprite_name=fname,
                        sprite_url=settings.SERVER_NAME + '/static/demo/',
                        css_path=settings.STATIC_DEMO_PATH,
                        class_name="demo")

        sprite.do_write_css()
        sprite.do_write_image()

        self.render("try.html",
                    SERVER_NAME=settings.SERVER_NAME,
                    message=msg,
                    success=success,
                    css=sprite.get_css(),
                    css_url=settings.SERVER_NAME + '/static/demo/sprite.css',
                    img_url=settings.SERVER_NAME + '/static/demo/' + fname,
                    entidades=original_names)
