from pytest import fixture

MANIFEST_KEYBAG_ZEROS = (
    # Version
    b'VERS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x05'
    # Type
    b'TYPE'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x01'
    # Root UUID
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'HMCK'
    b'\x00\x00\x00\x28'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Salt
    b'SALT'
    b'\x00\x00\x00\x14'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Iterations
    b'ITER'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x27\x10'
    # Decryption password wrap type
    b'DPWT'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x01'
    # Decryption password iteration count
    b'DPIC'
    b'\x00\x00\x00\x04'
    b'\x00\x98\x96\x80'
    # Decryption password salt
    b'DPSL'
    b'\x00\x00\x00\x14'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # UUID 1
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 11
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x0b'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x03'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 2
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 10
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x0a'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x03'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 3
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 9
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x09'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x03'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 4
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 8
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x08'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x02'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 5
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 7
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x07'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x02'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 6
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 6
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x06'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x02'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 7
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 5
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x05'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x03'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 8
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 4
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x04'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x02'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 9
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 3
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x03'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x02'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 10
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 2
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x02'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x02'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
    # UUID 11
    b'UUID'
    b'\x00\x00\x00\x10'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Class 1
    b'CLAS'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x01'
    # Key wrap
    b'WRAP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x02'
    # Key type
    b'KTYP'
    b'\x00\x00\x00\x04'
    b'\x00\x00\x00\x00'
    # Wrap key
    b'WPKY'
    b'\x00\x00\x00\x28'
    b'R\x8c\x9cQq\xbf\x8b\xef\x1e\xa3\x97\xcf)\xd2\xa88\xc9\x05)\xdf\x02\xa6\xad/\x82:\x1co:[ @\xe2\xa3\t\xc5 \xc6\xa2'
    b'\xab'
)


@fixture
def manifest_keybag_zeros():
    return MANIFEST_KEYBAG_ZEROS
