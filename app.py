import tkinter as tk
from tkinter import filedialog
import os


class ImageToPdfconverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []