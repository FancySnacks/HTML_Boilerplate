import os

# --- Variables

path = os.path.abspath(os.path.dirname('HTML_Boiler.py'))
directory_name = "HMTL_Boiler"
folders_to_create = ['css', 'js', 'img']

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <title>HTML Page</title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/main.css">
</head>
<body>
    <p>Page has been successfully created!</p>
    <script src="./js/main.js" async defer></script>
</body>
</html>'''

css_content = '''body
{
    margin: 0;
}'''


# --- Functions

def create_directory(path):
    path = os.path.join(path, directory_name)
    os.mkdir(path)
    create_folders()
    create_file(os.path.join(path + "/index.html"), html_content)
    create_file(os.path.join(path + "/css/main.css"), css_content)
    create_file(os.path.join(path + "/js/main.js"), "")

def create_folders():
    for folder in folders_to_create:
        new_folder = os.path.join(path, directory_name + "/" + folder)
        os.mkdir(new_folder)

def create_file(name, content):
    try:
        file = open(name, "x")
    except FileExistsError:
        pass
    finally:
        file = open(name, "w")
        file.write(content)
        print(f'{name} has been created.')
    file.close()


# Begin script
if __name__ == '__main__':
    create_directory(path)
    print("HMTL Boilerplate is ready!")