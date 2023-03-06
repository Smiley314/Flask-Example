from website import create_app

app = create_app()

# Run the server only if we want to, not if it is just imported
if __name__ == '__main__':
    # to debug during deveopment
    app.run(debug=True)