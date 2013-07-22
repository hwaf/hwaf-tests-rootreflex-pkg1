# -*- python -*-
# automatically generated wscript

import waflib.Logs as msg

PACKAGE = {
    'name': 'pkg1',
    'author': ["Sebastien Binet"], 
}

def pkg_deps(ctx):
    ctx.use_pkg('pkg-settings')
    return

def options(ctx):
    pass

def configure(ctx):
    pass

def build(ctx):

    ctx.build_linklib(
        name = "pkg1",
        includes = "inc",
        source = "src/pkg1.cxx",
        )
    # ctx(
    #     features="cxx cxxshlib",
    #     source = "src/pkg1.cxx",
    #     target = "pkg1",
    #     includes = "./inc",
    #     export_includes = "./inc",
    #     )
    # ctx.env['INCLUDES_pkg1'] = [
    #     "${INSTALL_AREA}/include",
    #     ctx.path.find_node("inc").abspath(),
    #     ]
    return
