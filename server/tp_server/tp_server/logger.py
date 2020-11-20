import sys
import traceback

from promise import is_thenable

class DebugMiddleware(object):
    def on_error(self, error):
        print(error)
        for line in traceback.format_exception(None,  # <- type(e) by docs, but ignored
                                         error, error.__traceback__):
            print(line, file=sys.stderr, flush=True)

    def resolve(self, next, root, info, **args):
        result = next(root, info, **args)
        if is_thenable(result):
            result.catch(self.on_error)

        return result
