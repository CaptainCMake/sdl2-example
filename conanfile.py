from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires.add("android_sdl2/0.1.0#debda07d9c722b256dc83beccc487d30fffbd274")
        self.build_requires.add("cmake_utils/0.3.1#7b308615a235fdf046db096dd35325c0375c2f88")

    def requirements(self):
        self.requires.add("sdl2/2.0.8#60fdb231f6e74bb622017585003a2c09c82d8b35")
