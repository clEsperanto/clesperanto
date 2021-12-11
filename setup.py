import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clesperanto",
    version="0.1.2",
    author="Robert Haase",
    author_email="robert.haase@tu-dresden.de",
    description="A graphical user interface for clesperanto based on napari",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clEsperanto/pyclesperanto_prototype",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy!=1.19.4",
        "pyopencl",
        "toolz",
        "scikit-image>=0.18.0",
        "matplotlib",
        "transforms3d",
        "napari[all]",
        "napari-pyclesperanto-assistant",
        "napari-accelerated-pixel-and-object-classification",
        "napari-brightness-contrast",
        "napari-mouse-controls",
        "napari-plot-profile",
        "napari-skimage-regionprops",
        "napari-segment-blobs-and-things-with-membranes",
        "napari-tabu",
        "napari-crop",
        "napari-layer-details-display"
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
    ],
    entry_points = {
        'console_scripts': ['cle=clesperanto:main'],
    }
)
