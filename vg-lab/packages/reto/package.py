# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Reto(CMakePackage):
    """ReTo (Render Tools) is a set of utilities to simplify common OpenGL
    rendering tasks such as shader/program management, camera handling and
    mesh loading."""

    homepage = "https://github.com/vg-lab/ReTo"
    git = "https://github.com/vg-lab/ReTo.git"

    license("GPL-3.0-only")

    version("master", branch="master")
    version("1.0.1", commit="8431f434180b944b5255db37830a559704699240")

    variant("shared", default=True, description="Build shared libraries")
    variant("examples", default=False, description="Build examples")
    variant("tests", default=False, description="Build unit tests")
    variant("doc", default=False, description="Build API documentation with Doxygen")
    variant("glut", default=True, description="Build with GLUT support")
    variant("freeimage", default=False, description="Build with FreeImage support")

    depends_on("cxx", type="build")

    depends_on("cmake@3.25:", type="build")

    depends_on("gl")
    depends_on("glew")
    depends_on("eigen@3:")
    depends_on("boost+test")
    depends_on("freeglut", when="+glut")
    depends_on("freeimage", when="+freeimage")

    depends_on("doxygen", type="build", when="+doc")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("BUILD_DOCS", "doc"),
            self.define_from_variant("RETO_WITH_EXAMPLES", "examples"),
            self.define_from_variant("RETO_WITH_TESTS", "tests"),
        ]
        return args

    def setup_build_environment(self, env):
        eigen = self.spec["eigen"]
        env.remove_path("CPATH", eigen.prefix.include.eigen3)
        env.prepend_path("CPATH", eigen.prefix.include)
