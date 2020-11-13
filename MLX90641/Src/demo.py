import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.subscribe as subscribe
import matplotlib
from Track import Track
from Frame import Frame
from utils import *

data01 = np.load("../Dataset/data03.npy")

piexls = data01[163]

F = Frame(piexls)
print(F.index_list)