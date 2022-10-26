from project import first_degree, second_degree
from project import sinusoidal, cosinusoidal, constant
import numpy as np
import pytest

def test_first_degree():
    assert first_degree( 2, 1, 4) == (2 , 1*2 + 4)
    assert first_degree( 2, 2, 3) == (2 , 2*2 + 3)
    assert first_degree( 2, 3, 2) == (2 , 3*2 + 2)
    assert first_degree( 2, 4, 1) == (2 , 4*2 + 1)

def test_second_degree():
    assert second_degree(2 , 1, 1, 2) ==  (2, 1*(2**2) + 1 * 2 + 2)
    assert second_degree(2 , 2, 2, 4) ==  (2, 2*(2**2) + 2 * 2 + 4)
    assert second_degree(2 , 3, 3, 6) ==  (2, 3*(2**2) + 3 * 2 + 6)
    assert second_degree(2 , 4, 4, 8) ==  (2, 4*(2**2) + 4 * 2 + 8)

def test_sinusoidal():
    assert sinusoidal(2, 10) == (2, 10*np.sin(2)) 
    assert sinusoidal(2,  8) == (2,  8*np.sin(2))
    assert sinusoidal(2,  3) == (2,  3*np.sin(2))
    assert sinusoidal(2,  1) == (2,  1*np.sin(2))

def test_cosinusoidal():
    assert cosinusoidal( 2, 8) == ( 2, 8*np.cos(2))
    assert cosinusoidal( 1, 4) == ( 1, 4*np.cos(1))
    assert cosinusoidal( 4, 1) == ( 4, 1*np.cos(4))
    assert cosinusoidal( 8, 2) == ( 8, 2*np.cos(8))

def test_constant():
    assert constant(320, 35)  == (320, 35) 
    assert constant(140, 94)  == (140, 94) 
    assert constant(325,100)  == (325, 100)
    assert constant(985,300)  == (985, 300)
