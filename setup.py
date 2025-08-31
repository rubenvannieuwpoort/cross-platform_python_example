from setuptools import setup
from distutils.command.build import build
from distutils import ccompiler
import os

class CustomBuild(build):
    def run(self):
        # Create a compiler instance
        compiler = ccompiler.new_compiler()

        # Ensure build_temp exists
        self.mkpath(self.build_temp)

        # Compile the C source into object files
        objects = compiler.compile(['foo.c'], output_dir=self.build_temp)

        # Determine the target directory for the shared library (inside the package)
        target_dir = os.path.join(self.build_lib, 'mypackage')

        # Ensure target_dir exists
        self.mkpath(target_dir)

        # Link the object files into a shared library
        compiler.link_shared_lib(objects, 'foo', output_dir=target_dir)

        # Run the original build command
        super().run()

setup(
    name='myproject',
    version='0.1',
    packages=['mypackage'],
    package_dir={'mypackage': 'mypackage'},
    cmdclass={'build': CustomBuild},
    # Include the shared library as package data (wildcard for platform-specific extensions)
    package_data={'mypackage': ['libfoo.*', 'foo.*']},
)
