# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libqglviewer(CMakePackage):
    """libQGLViewer is a C++ library based on Qt that eases the creation of
    OpenGL 3D viewers."""

    homepage = "https://gillesdebunne.github.io/libQGLViewer/"
    git = "https://github.com/GillesDebunne/libQGLViewer.git"

    license("LGPL-3.0-only", when="@3.0.0:")

    version("3.0.0", commit="c8bb8810e70f0c902cbf5c222ee6fc1e4cd11d34")
    # version(
    #     "3.0.0",
    #     sha256="f9ae1c902daa0e35ea98878edbe1b902f6e731c9c9427c19942d5351cdf05cb9",
    #     url="https://github.com/GillesDebunne/libQGLViewer/tarball/c8bb8810e70f0c902cbf5c222ee6fc1e4cd11d34"
    # )

    patch("fix-cmake.patch", when="@3.0.0")

    depends_on("cxx", type="build")

    depends_on("cmake@3.16:", type="build")
    depends_on("qt@5.15: +gui +opengl")
    depends_on("gl")
    depends_on("glu")
