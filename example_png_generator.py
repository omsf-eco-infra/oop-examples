import os
import subprocess
from pathlib import Path


def list_examples(directory):
    """List all Python files in the examples directory"""
    examples = []
    for file in os.listdir(directory):
        if file.endswith(".py") and file != "__init__.py":
            examples.append(file)
    return examples


def generate_png(example_path, output_dir="."):
    """Generate PNG using freeze command (without line numbers)"""
    # Generate output filename (same name as example, .png extension)
    filename = Path(example_path).stem + ".png"
    output_path = Path(output_dir) / filename

    # Run freeze command - NO line numbers
    cmd = [
        "freeze",
        example_path,
        "-o",
        str(output_path),
        "-l",
        "python",  # Set language to Python
        # Note: --show-line-numbers is omitted as requested
    ]

    subprocess.run(cmd, check=True)
    return output_path


def main():
    examples_dir = "oop_basic_examples"
    examples = list_examples(examples_dir)

    print("Available examples:")
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example}")

    while True:
        try:
            selection = input(
                "\nSelect example number to freeze (or 'all' for all examples): "
            )
            if selection.lower() == "all":
                output_dir = "png_outputs"
                Path(output_dir).mkdir(exist_ok=True)
                for example in examples:
                    example_path = os.path.join(examples_dir, example)
                    print(f"Generating PNG for {example}...")
                    generate_png(example_path, output_dir)
                print(f"\nAll examples processed. PNGs saved to {output_dir}/")
                break
            else:
                selected_index = int(selection) - 1
                selected_example = examples[selected_index]
                example_path = os.path.join(examples_dir, selected_example)
                output_path = generate_png(example_path)
                print(f"\nPNG generated: {output_path}")
                break
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()
