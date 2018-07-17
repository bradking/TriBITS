#!/usr/bin/env python

# @HEADER
# ************************************************************************
#
#            TriBITS: Tribal Build, Integrate, and Test System
#                    Copyright 2013 Sandia Corporation
#
# Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
# the U.S. Government retains certain rights in this software.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the Corporation nor the names of the
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY SANDIA CORPORATION "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL SANDIA CORPORATION OR THE
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# ************************************************************************
# @HEADER

from TribitsPackageFilePathUtils import *


#
# Read in the commandline arguments
#

usageHelp = \
r"""filter-packages-list.py --deps-xml-file=<PROJECT_DEPS_FILE> \
  --input-packages-list=<P1>,<P2>,... --keep-types=<T1>,<T2>,...

This script takes in a comma-seprated list of TriBITS package names
<P1>,<P2>,... and keeps the package names matching the categories listed in
<T1>,<T2>,... given the TriBITS-generated project dependencies file.

The comma-seprated filtered list of packages is printed to STDOUT.
"""

from optparse import OptionParser

clp = OptionParser(usage=usageHelp)

clp.add_option(
  "--input-packages-list", dest="inputPackagesList", type="string", default="",
  help="Comma-seprated List of packages that needs to be filtered (i.e. \"P1,P2,...\")." )

clp.add_option(
  "--keep-types", dest="keepTypes", type="string", default="",
  help="List of package types to keep (i.e. \"PT,ST,EX\"." )

clp.add_option(
  "--deps-xml-file", dest="depsXmlFile", type="string",
  help="TriBITS generated XML file containing the listing of packages, dir names, dependencies, etc.")

(options, args) = clp.parse_args()

trilinosDependencies = getProjectDependenciesFromXmlFile(options.depsXmlFile)

inputPackagesList = options.inputPackagesList.split(",")
keepTypesList = options.keepTypes.split(",")
outputPackagesList = trilinosDependencies.filterPackageNameList(inputPackagesList, keepTypesList)
print ','.join(outputPackagesList)
