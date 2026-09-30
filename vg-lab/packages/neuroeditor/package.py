# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Neuroeditor(CMakePackage):
    """NeuroEditor is a software tool for the visualization and edition of
    morphological tracings. It offers manual edition capabilities together
    with a set of algorithms that can automatically identify potential
    errors in the tracings and, in some cases, propose a set of actions to
    automatically correct them. NeuroEditor visualizes the original tracing,
    the modified tracing, and a 3D mesh that approximates the neuronal
    membrane, computed on-the-fly and instantaneously reflecting any changes
    made to the tracing."""

    homepage = "https://github.com/vg-lab/NeuroEditor"
    git = "https://github.com/vg-lab/NeuroEditor.git"

    license("GPL-3.0-only")

    version("master", branch="master")
    version("1.0.1", commit="8ef5f26444d11cc563b50377a35f5dba608f3a3e")

    variant("doc", default=False, description="Build API documentation with Doxygen")

    depends_on("cxx", type="build")

    depends_on("cmake@3.25:", type="build")

    depends_on("qt@5.15: +gui +opengl")
    depends_on("glew")
    depends_on("freeglut")
    depends_on("gl")
    depends_on("glu")
    depends_on("eigen@3:")

    depends_on("pygems@4.0.0:")
    depends_on("nsol@1.0.0:")
    depends_on("neurolots@1.0.1:")
    depends_on("libqglviewer@3.0.0:")

    depends_on("doxygen", type="build", when="+doc")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_DOCS", "doc"),
        ]
        return args

    def setup_build_environment(self, env):
        eigen = self.spec["eigen"]
        env.remove_path("CPATH", eigen.prefix.include.eigen3)
        env.prepend_path("CPATH", eigen.prefix.include)
