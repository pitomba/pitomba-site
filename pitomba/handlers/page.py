# coding: utf-8
from pitomba import settings
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
        success = False

        if not self.request.files.get('file', None):
            msg = "No file given."
        else:
            files = []
            for r_file in self.request.files.get('file'):
                original_fname = r_file['filename']
                extension = os.path.splitext(original_fname)[1]
                fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
                final_filename = fname + extension
                final_filepath = settings.UPLOAD_PATH + '/' + final_filename
                output_file = open(final_filepath, 'w')
                output_file.write(r_file['body'])

                files.append(final_filepath)

            success = True

        self.render("try.html",
                    SERVER_NAME=settings.SERVER_NAME,
                    message=msg,
                    success=success)
