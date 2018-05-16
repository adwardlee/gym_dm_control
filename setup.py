import os
from setuptools import setup
from setuptools import find_packages

setup(
    name = "gym_dm_control",
    version = "0.1",
    description = ("OpenAI Gym Wrapper for DeepMind Control Suite"),
    license = "",
    keywords = "openai gym deepmind wrapper",
    packages=find_packages(),
    install_requires=[
        'gym',
        'dm_control',
    ],
)
