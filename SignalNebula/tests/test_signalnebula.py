from signalnebula.engine import analyze

def test_analyze():
    result = analyze('data/sample_signal.csv')
    assert result['samples'] == 4