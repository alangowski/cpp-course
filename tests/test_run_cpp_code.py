import sys
import types
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Provide a minimal stub for the streamlit module so that main can be imported
st_stub = types.SimpleNamespace()
st_stub.set_page_config = lambda *a, **k: None
st_stub.title = lambda *a, **k: None
st_stub.sidebar = types.SimpleNamespace(selectbox=lambda *a, **k: None)
st_stub.subheader = lambda *a, **k: None
st_stub.markdown = lambda *a, **k: None
st_stub.video = lambda *a, **k: None
st_stub.code = lambda *a, **k: None
st_stub.write = lambda *a, **k: None
st_stub.header = lambda *a, **k: None
st_stub.info = lambda *a, **k: None
st_stub.success = lambda *a, **k: None
st_stub.error = lambda *a, **k: None
st_stub.radio = lambda *a, **k: None
st_stub.button = lambda *a, **k: False
st_stub.text_area = lambda *a, **k: ""
st_stub.session_state = {}

sys.modules.setdefault("streamlit", st_stub)

from main import run_cpp_code


def test_run_cpp_code_success():
    code = "#include <iostream>\nint main(){std::cout<<\"Hello\";return 0;}"
    output = run_cpp_code(code)
    assert output.strip() == "Hello"


def test_run_cpp_code_failure():
    bad_code = "int main() {"
    output = run_cpp_code(bad_code)
    assert "error" in output.lower()
