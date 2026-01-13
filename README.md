# OOP Examples

A collection of basic Object-Oriented Programming examples demonstrating various OOP concepts in Python.

## Overview

This project contains Python examples that illustrate fundamental Object-Oriented Programming concepts including:

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Composition
- Multiple Inheritance
- Mixins
- Method Overriding
- Class and Static Methods
- Properties
- Duck Typing
- Object instances and classes

## Structure

- `example_png_generator.py`: Script to generate PNG images from Python examples
- `oop_basic_examples/`: Directory containing individual OOP concept examples

## Usage

To generate PNG images from the examples:

```bash
python example_png_generator.py
```

Select an example number or type "all" to generate PNGs for all examples.

## Examples

Each Python file in the `oop_basic_examples` directory demonstrates a specific OOP concept:

- `encapsulation.py`: Shows data hiding and access control
- `inheritance.py`: Demonstrates class inheritance
- `polymorphism.py`: Shows method overriding and polymorphic behavior
- `abstraction.py`: Illustrates abstract classes and methods
- `composition.py`: Demonstrates composition over inheritance
- `multiple_inheritance.py`: Shows multiple inheritance usage
- `mixins.py`: Example of mixin classes
- `method_overriding.py`: Demonstrates method overriding
- `class_static_methods.py`: Shows class and static methods
- `properties.py`: Illustrates property decorators
- `duck_typing.py`: Example of duck typing
- `object_instance_class.py`: Shows object instances and class relationships

## Requirements

- Python 3.x
- `freeze` command (for generating PNGs from code)
- Conda or Mamba package manager

## Environment Setup

This project includes an `environment.yml` file for creating a dedicated conda/mamba environment:

### Using Mamba (recommended for faster installs)

```bash
# Create environment with mamba
mamba env create -f environment.yml
mamba activate omsf-eco-infra-oop-examples

# Run the PNG generator
python example_png_generator.py
```

### Using Conda
```bash
# Create and activate the environment
conda env create -f environment.yml
conda activate omsf-eco-infra-oop-examples

# Deactivate when done
conda deactivate
```

The environment includes:
- Python
- [freeze](https://github.com/charmbracelet/freeze) (for generating PNGs from code)

After activating the environment, you can run the PNG generator or any of the example scripts.
