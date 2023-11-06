# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:58:37 2023

@author: www.markazi.co
"""

#pip install barfi
from barfi import st_barfi, barfi_schemas, Block
import streamlit as st


feed1 = Block(name='Adder')
feed1.add_output('output1')

feed2 = Block(name='Readout')
feed2.add_input(name='input1')
feed2.add_output(name='output1')
feed2.add_option(name="setDepth", type='integer',value=1)

feed3= Block(name="Bluring")
feed3.add_option(name="Resolution", type='number', value=0.08 , min=0.0, max=1)
feed3.add_option(name="Reference Energy (keV)", type='number',value=140, min=1)
feed3.add_input(name='input2')
feed3.add_output(name='output2')

feed4=Block(name="Energy window")
feed4.add_option(name="Lower level (keV)",type='number',value=120 , min=0, max=10)
feed4.add_option(name="Upper level (keV)", type='number',value=160, min=0)

feed4.add_input(name='input3')
feed4.add_output(name='output3')
splitter = Block(name='Splitter')
splitter.add_input()
splitter.add_output()
splitter.add_output()
splitter.add_output()
def splitter_func(self):
    in_1 = self.get_interface(name='Input 1')
    value = (in_1/2)
    self.set_interface(name='Output 1', value=value)
    self.set_interface(name='Output 2', value=value)
    self.set_interface(name='Output 3', value=value)
splitter.add_compute(splitter_func)

mixer = Block(name='Mixer')
mixer.add_input()
mixer.add_input()
mixer.add_output()
mixer.add_output()
def mixer_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    in_3 = self.get_interface(name='Input 2')
    value = (in_1 + in_2+in_3)
    self.set_interface(name='Output 1', value=value)
mixer.add_compute(mixer_func)

result = Block(name='Result')
result.add_input()
def result_func(self):
    in_1 = self.get_interface(name='Input 1')
result.add_compute(result_func)

load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=[feed1, feed2, feed3, feed4],
                   compute_engine=compute_engine, load_schema=load_schema)


#if barfi_result:
   # st.write(barfi_result)