from bs4 import BeautifulSoup

def test_login_page():
  from app import app

  with app.test_client() as test_client:
   response = test_client.get('/login')

   data = response.get_data(as_text=True)
   soup = BeautifulSoup(data, features="html.parser")
   
   form_html = soup.find('form', {'method': 'POST'})
   username_input = form_html.find('input', {'name': 'username'})
   password_input = form_html.find('input', {'name': 'password'})
   submit_button = form_html.find('button', {'type': 'submit'})

   assert form_html is not None
   assert username_input is not None
   assert password_input is not None
   assert submit_button is not None
