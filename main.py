from website import create_app
from website import templates

app = create_app()

if __name__ == '__main__':
	app.run(debug=True, port=8000, host='0.0.0.0')
