# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Pygems(CMakePackage):
    """PyGEMS (PYthon Generic Embedding System) is a C++ library for
    embedding Python in C++ applications."""

    homepage = "https://github.com/vg-lab/pygems"
    git = "https://github.com/vg-lab/pygems.git"

    license("GPL-3.0-only")

    version("master", branch="master")
    version("4.0.0", commit="bdb06a56d2d400bd9872bfc6656210ef3b0ac265")

    variant("shared", default=True, description="Build shared libraries")
    variant("examples", default=False, description="Build examples")
    variant("doc", default=False, description="Build API documentation with Doxygen")

    depends_on("cxx", type="build")

    depends_on("cmake@3.25:", type="build")

    depends_on("python@3:")
    depends_on("boost+python")

    depends_on("doxygen", type="build", when="+doc")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("BUILD_DOCS", "doc"),
            self.define_from_variant("PYGEMS_WITH_EXAMPLES", "examples"),
        ]
        return args
