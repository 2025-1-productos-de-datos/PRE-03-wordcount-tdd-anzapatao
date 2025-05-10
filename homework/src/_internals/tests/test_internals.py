import subprocess

from ...wordcount import parse_args, read_all_lines


def test_parse_args():
    # Test the function directly with arguments
    input_folder, output_folder = parse_args(["data/input/", "data/output/"])
    assert input_folder == "data/input/"
    assert output_folder == "data/output/"

    # También puedes probar la ejecución completa del script si lo necesitas
    try:
        result = subprocess.run(
            ["python3", "-m", "homework", "data/input/", "data/output/"],
            check=True,
            capture_output=True,
            text=True,
        )
        # Puedes verificar la salida si es necesario
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")


##
def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )
