# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Nsol(CMakePackage):
    """nsol (NeuroScience Objects Library) provides a set of C++ classes
    to represent, read, write and manipulate neuron morphologies and
    related neuroscientific data structures."""

    homepage = "https://github.com/vg-lab/nsol"
    git = "https://github.com/vg-lab/nsol.git"

    license("LGPL-3.0-only")

    version("master", branch="master")
    version("1.0.0", commit="d5ca1e20592847b9475c277d7cc79ff915bc99d2")

    variant("shared", default=True, description="Build shared libraries")
    variant("examples", default=False, description="Build examples")
    variant("tests", default=False, description="Build unit tests")
    variant("doc", default=False, description="Build API documentation with Doxygen")
    variant("hdf5", default=False, description="Build with HDF5 support")

    depends_on("cxx", type="build")

    depends_on("cmake@3.25:", type="build")

    depends_on("boost+test")
    depends_on("eigen@3.4.0")
    depends_on("hdf5+cxx", when="+hdf5")

    depends_on("doxygen", type="build", when="+doc")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("BUILD_DOCS", "doc"),
            self.define_from_variant("NSOL_WITH_EXAMPLES", "examples"),
            self.define_from_variant("NSOL_WITH_TESTS", "tests"),
            self.define("NSOL_USE_BRION", False),
            self.define("NSOL_USE_FIRES", False),
        ]
        return args

    def setup_build_environment(self, env):
        eigen = self.spec["eigen"]
        env.remove_path("CPATH", eigen.prefix.include.eigen3)
        env.prepend_path("CPATH", eigen.prefix.include)
