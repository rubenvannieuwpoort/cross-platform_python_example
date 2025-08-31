import ctypes
import os
import sysconfig
import platform

def load_and_call_hello():
    # Determine the shared library extension and prefix based on platform
    ext = sysconfig.get_config_var('SHLIB_SUFFIX')
    if ext is None:
        ext = '.so'  # Fallback
    prefix = '' if platform.system() == 'Windows' else 'lib'

    # Construct the library path relative to this package
    dir_path = os.path.dirname(__file__)
    lib_path = os.path.join(dir_path, prefix + 'foo' + ext)

    # Load the library
    lib = ctypes.CDLL(lib_path)

    # Set the return type
    lib.hello.restype = ctypes.c_int

    # Call the function
    lib.hello()

# Example usage (you can call this from your code)
if __name__ == '__main__':
    load_and_call_hello()
