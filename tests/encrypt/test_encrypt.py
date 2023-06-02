from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    palavra = 'ABCDEF'

    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message(palavra, '3')

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(52, 3)

    key_impar = encrypt_message(palavra, 3)
    assert key_impar == 'CBA_FED'

    key_par = encrypt_message(palavra, 4)
    assert key_par == 'FE_DCBA'

    key_impar_9 = encrypt_message(palavra, 9)
    assert key_impar_9 == 'FEDCBA'
