#
# Copyright OpenEmbedded Contributors
#
# SPDX-License-Identifier: MIT
#

import os

from oeqa.selftest.case import OESelftestTestCase
from oeqa.utils.commands import bitbake, get_bb_var
import oeqa.utils.ftools as ftools

class LayerAppendTests(OESelftestTestCase):
    layerconf = """
# We have a conf and classes directory, append to BBPATH
BBPATH .= ":${LAYERDIR}"

# We have a recipes directory, add to BBFILES
BBFILES += "${LAYERDIR}/recipes*/*.bb ${LAYERDIR}/recipes*/*.bbappend"

BBFILE_COLLECTIONS += "meta-layerINT"
BBFILE_PATTERN_meta-layerINT := "^${LAYERDIR}/"
BBFILE_PRIORITY_meta-layerINT = "6"
"""
    recipe = """
LICENSE="CLOSED"
INHIBIT_DEFAULT_DEPS = "1"

python do_build() {
    bb.plain('Building ...')
}
addtask build
"""
    append = """
FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append = " file://appendtest.txt"

sysroot_stage_all:append() {
	install -m 644 ${UNPACKDIR}/appendtest.txt ${SYSROOT_DESTDIR}/
}

"""

    append2 = """
FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append = " file://appendtest.txt"
"""
    layerappend = ''

    def tearDownLocal(self):
        if self.layerappend:
            ftools.remove_from_file(self.builddir + "/conf/bblayers.conf", self.layerappend)
        super(LayerAppendTests, self).tearDownLocal()

    def test_layer_appends(self):
        corebase = get_bb_var("COREBASE")

        for l in ["0", "1", "2"]:
            layer = os.path.join(corebase, "meta-layertest" + l)
            self.assertFalse(os.path.exists(layer))
            os.mkdir(layer)
            os.mkdir(layer + "/conf")
            with open(layer + "/conf/layer.conf", "w") as f:
                f.write(self.layerconf.replace("INT", l))
            os.mkdir(layer + "/recipes-test")
            if l == "0":
                with open(layer + "/recipes-test/layerappendtest.bb", "w") as f:
                    f.write(self.recipe)
            elif l == "1":
                with open(layer + "/recipes-test/layerappendtest.bbappend", "w") as f:
                    f.write(self.append)
                os.mkdir(layer + "/recipes-test/layerappendtest")
                with open(layer + "/recipes-test/layerappendtest/appendtest.txt", "w") as f:
                    f.write("Layer 1 test")
            elif l == "2":
                with open(layer + "/recipes-test/layerappendtest.bbappend", "w") as f:
                    f.write(self.append2)
                os.mkdir(layer + "/recipes-test/layerappendtest")
                with open(layer + "/recipes-test/layerappendtest/appendtest.txt", "w") as f:
                    f.write("Layer 2 test")
            self.track_for_cleanup(layer)

        self.layerappend = "BBLAYERS += \"{0}/meta-layertest0 {0}/meta-layertest1 {0}/meta-layertest2\"".format(corebase)
        ftools.append_file(self.builddir + "/conf/bblayers.conf", self.layerappend)
        stagingdir = get_bb_var("SYSROOT_DESTDIR", "layerappendtest")
        bitbake("layerappendtest")
        data = ftools.read_file(stagingdir + "/appendtest.txt")
        self.assertEqual(data, "Layer 2 test")
        os.remove(corebase + "/meta-layertest2/recipes-test/layerappendtest/appendtest.txt")
        bitbake("layerappendtest")
        data = ftools.read_file(stagingdir + "/appendtest.txt")
        self.assertEqual(data, "Layer 1 test")
        with open(corebase + "/meta-layertest2/recipes-test/layerappendtest/appendtest.txt", "w") as f:
            f.write("Layer 2 test")
        bitbake("layerappendtest")
        data = ftools.read_file(stagingdir + "/appendtest.txt")
        self.assertEqual(data, "Layer 2 test")
