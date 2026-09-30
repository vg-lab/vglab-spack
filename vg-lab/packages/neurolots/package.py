# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Neurolots(CMakePackage):
    """NeuroLOTs is a set of libraries and tools for generating neuronal meshes
    and for visualizing them at different levels of detail using GPU-based
    tessellation. Providing tools for the generation of 3D polygonal meshes that
    approximate the membrane of neuronal cells, from the morphological tracings
    that describe the morphology of the neurons. The 3D models can be tessellated
    at different levels of detail, providing either homogeneous or adaptive
    resolution along the model. The soma shape is recovered from the incomplete
    information of the tracings, applying a physical deformation model that can
    be interactively adjusted."""

    homepage = "https://github.com/vg-lab/neurolots"
    git = "https://github.com/vg-lab/neurolots.git"

    license("GPL-3.0-only")

    version("master", branch="master")
    version("1.0.1", commit="ab9c65911a8ea13c29ff45d6fdee6269989c171f")

    variant("shared", default=True, description="Build shared libraries")
    variant("examples", default=False, description="Build examples")
    variant("doc", default=False, description="Build API documentation with Doxygen")
    variant("glut", default=False, description="Build with GLUT support")

    depends_on("cxx", type="build")

    depends_on("cmake@3.25:", type="build")

    depends_on("gl")
    depends_on("glew")
    depends_on("eigen@3:")
    depends_on("freeglut", when="+glut+examples")

    depends_on("nsol@1.0.0:")
    depends_on("reto@1.0.1:")

    depends_on("doxygen", type="build", when="+doc")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("BUILD_DOCS", "doc"),
            self.define_from_variant("NEUROLOTS_WITH_EXAMPLES", "examples"),
            self.define("NSOL_USE_BRION", False),
            self.define("NSOL_USE_FIRES", False)
        ]
        return args

    def setup_build_environment(self, env):
        eigen = self.spec["eigen"]
        env.remove_path("CPATH", eigen.prefix.include.eigen3)
        env.prepend_path("CPATH", eigen.prefix.include)
