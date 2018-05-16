import os
from setuptools import setup, find_packages
from setuptools_rust import Binding, RustExtension

PACKAGE_NAME = "hermes_python"
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
PACKAGE_PATH = os.path.join(ROOT_PATH, PACKAGE_NAME)
README = os.path.join(ROOT_PATH, "README.rst")
VERSION = "__version__"

RUST_EXTENSION_NAME = "hermes_python.dylib.libhermes_mqtt_ffi"
CARGO_ROOT_PATH = os.path.join(ROOT_PATH, '../../../hermes-mqtt-ffi')

CARGO_FILE_PATH = os.path.join(CARGO_ROOT_PATH, 'Cargo.toml')
CARGO_TARGET_DIR = os.path.join(CARGO_ROOT_PATH, 'target')

TARGET = "hermes_python.dylib.libhermes_mqtt_ffi"

CARGO_PATH = ""

os.environ['CARGO_TARGET_DIR'] = CARGO_TARGET_DIR

setup(
    name='hermes_python',
    version='0.1.18',
    description='Python bindings for Hermes',
    author='Anthony Reinette',
    author_email='anthony.reinette@snips.ai',
    url='https://github.com/snipsco/snips-platform/tree/main/hermes-ffi-python-extension/hermes-protocol/hermes-ffi/platforms/hermes-python',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',  
        'Programming Language :: Python :: 3.4', 
        'Programming Language :: Python :: 3.5', 
        'Programming Language :: Python :: 3.6'],
    download_url='',
    license='MIT',
    keywords=['snips'],
    install_requires=['six'],
    rust_extensions=[RustExtension(TARGET, CARGO_FILE_PATH, binding=Binding.NoBinding, dinghy=True, rust_x_compile_target="armv7-unknown-linux-gnueabihf", dinghy_platform="raspbian")],
    test_suite="tests",
    packages=find_packages(),
    zip_safe=False
)
