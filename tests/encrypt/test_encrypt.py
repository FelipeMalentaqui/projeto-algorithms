from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('ABCDEF', '3')
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(52, 3)

    key_impar = encrypt_message('ABCDEF', 3)
    assert key_impar == 'CBA_FED'

    key_par = encrypt_message('ABCDEF', 4)
    assert key_par == 'FE_DCBA'
