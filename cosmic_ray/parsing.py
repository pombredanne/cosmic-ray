"""Facilities for generating ASTs from modules.
"""

import ast
import inspect
import logging

LOG = logging.getLogger()

# TODO: This is where we can do different things for different kinds of
# modules. Right now we only really handle normal source-code, text-file
# modules.


def get_ast(module):
    """Generate an AST from a module object.

    This will be the AST for the contents of the module.

    Raises:
        OSError: If the source code for `module` can't be found.
        TypeError: If the source file for `module` can't be found.
    """
    try:
        source = inspect.getsource(module)
    except OSError:
        LOG.warning("Unable to read source for module %s", module)
        raise

    try:
        source_file = inspect.getsourcefile(module)
    except TypeError:
        LOG.error("Unable to get source file for object %s", module)
        raise

    return ast.parse(source, source_file, 'exec')
