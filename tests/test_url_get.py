def test_info_page_cl():
  from app import app

  with app.test_client() as test_client:
      response = test_client.get('/info', query_string={
         "country_code":"cl"
      })
      data = response.get_data(as_text=True)

      assert response.status_code == 200
      
      assert "Nombre: Chile" in data
      assert "Capital: Santiago" in data
      assert "Moneda: CLP" in data

def test_info_page_co():
  from app import app

  with app.test_client() as test_client:
      response = test_client.get('/info', query_string={
         "country_code":"co"
      })
      data = response.get_data(as_text=True)

      assert response.status_code == 200

      assert "Nombre: Colombia" in data
      assert "Capital: Bogotá" in data
      assert "Moneda: COP" in data

def test_info_not_code_error():
   from app import app

   with app.test_client() as test_client:
      response = test_client.get('/info')
      data = response.get_data(as_text=True)

      assert response.status_code == 200

      assert "Error country_code is required in URL" in data
