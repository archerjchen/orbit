from conans import python_requires
llvm_common = python_requires('llvm-common/0.0.3@orbitdeps/stable')

class LLVMConan(llvm_common.LLVMComponentPackage):
    name = "llvm"
    version = llvm_common.LLVMComponentPackage.version
    short_paths = True

    custom_cmake_options = {
        'LLVM_BUILD_TOOLS': True,
        'LLVM_ENABLE_ZLIB': True
    }
    package_info_exclude_libs = [
        'BugpointPasses', 'LLVMHello', 'LTO'
    ]

    def requirements(self):
        self.requires('gtest/1.8.1@bincrafters/stable', private=True)
        self.requires('zlib/1.2.11@conan/stable', private=True)
        super().requirements()