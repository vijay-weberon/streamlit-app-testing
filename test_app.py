from streamlit.testing.v1 import AppTest

def test_incorrect_password():
    at = AppTest.from_file("app.py").run()
    assert not at.exception

    at.secrets["PASSWORD"] = "Vijay"
    at.text_input("password").input("Vijawy").run()
    assert at.warning[0].value == "Sorry, the passwords didn't match"

def test_correct_password():
    at = AppTest.from_file("app.py").run()
    assert not at.exception

    at.secrets["PASSWORD"] = "Vijay"
    at.text_input("password").input("Vijay").run()
    assert any(msg.value == "Congrats! You can see the secret content" and msg.icon == "🎉" for msg in at.success[0])
    
