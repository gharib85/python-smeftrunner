import unittest
import numpy as np
import numpy.testing as npt
from smeftrunner import SMEFT, io
import pkgutil
import pylha

class TestIO(unittest.TestCase):
    def test_lhamatrix(self):
        M = np.random.rand(2,3,4)
        values = io.matrix2lha(M)
        M2 = io.lha2matrix(values, (2,3,4))
        npt.assert_array_equal(M, M2)

    def test_load(self):
        sm = pkgutil.get_data('smeftrunner', 'tests/data/SMInput-CPV.dat').decode('utf-8')
        wc = pkgutil.get_data('smeftrunner', 'tests/data/WCsInput-CPV-SMEFT.dat').decode('utf-8')
        wcout = pkgutil.get_data('smeftrunner', 'tests/data/Output_SMEFTrunner.dat').decode('utf-8')
        io.sm_lha2dict(pylha.load(sm))
        io.wc_lha2dict(pylha.load(wc))
        CSM = io.sm_lha2dict(pylha.load(wcout))
        C = io.wc_lha2dict(pylha.load(wcout))
        C2 = io.wc_lha2dict(io.wc_dict2lha(C))
        for k in C:
            npt.assert_array_equal(C[k], C2[k])
        smeft = SMEFT()
        smeft.load_initial((wcout,))
        for k in C:
            npt.assert_array_equal(C[k], smeft.C_in[k], err_msg="Failed for {}".format(k))
        for k in CSM:
            npt.assert_array_equal(CSM[k], smeft.C_in[k], err_msg="Failed for {}".format(k))
        CSM2 = io.sm_lha2dict(io.sm_dict2lha(CSM))
        for k in CSM:
            npt.assert_array_equal(CSM[k], CSM2[k], err_msg="Failed for {}".format(k))

    def test_dump(self):
        wcout = pkgutil.get_data('smeftrunner', 'tests/data/Output_SMEFTrunner.dat').decode('utf-8')
        smeft = SMEFT()
        smeft.load_initial((wcout,))
        smeft.scale_in = 1000
        smeft.scale_high = 1000
        C_out = smeft.rgevolve(scale_out=900)
        C_dump = smeft.dump(C_out)
        smeft.load_initial((C_dump,))
        for k in C_out:
            npt.assert_array_almost_equal(C_out[k].real, smeft.C_in[k].real, err_msg="Failed for {}".format(k))
