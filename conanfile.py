import os
from conans import ConanFile, CMake

class IgeConan(ConanFile):
    name = 'taskflow'
    version = '3.1.0'
    license = "MIT"
    author = "Indi Games"
    url = "https://github.com/indigames"
    description = name + " library for IGE Engine"
    topics = ("#Python", "#IGE", "#Games")
    settings = []
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake_find_package"
    exports_sources = "*.h*"
    no_copy_source = True
    requires = []
    short_paths = True
    revision_mode="scm"

    def package(self):
        self.copy("*.h*", dst="include/taskflow", src="taskflow")

    def package_id(self):
        self.info.header_only()
