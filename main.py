# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:23:49 2018

@author: laura
"""

#%%

#%%
import utils.functions as uf
import data.triangles as dt


def calculate_triangles():
    for i in dt.triangle_definitions:
        print(uf.area_triangle(i["base"],i["height"]))
    
calculate_triangles()

#%%