from mlprojectest.lib import get_coordinates

def test_output():

    assert (get_coordinates("NOVA SBE")[0]=='38.679086') and (get_coordinates("NOVA SBE")[1]=='-9.3268883')