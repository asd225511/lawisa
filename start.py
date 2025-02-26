import socket
PC = socket.gethostname()
repos.create_file(f"{PC}/PC_{PC}_Log", "Start new log session", "PC is add")
repos.create_file(f"{PC}/{PC}_module.py", "New module", "print('The file created for your code!')")
start_code = """

repo_code = None
def process():
    global repo_code
    try:
        while True:
            list_f = repos.get_contents(str(PC))
            print(list_f)
            for elem in list_f:
                x = elem.name.replace(f'ContentFile(path="{PC}/{PC}_', '')

                if x.find('module'):
                    try:
                        file_content = repos.get_contents(f'{PC}/{PC}_module.py')
                        new_repo_code = file_content.decoded_content.decode()
                        if new_repo_code != repo_code:
                            exec(new_repo_code)
                            repo_code = new_repo_code
                            print("File was updated! Code run.")
                        else:
                            print("No updates to file.")
                    except Exception as e:
                        print(f"Error processing file {elem}: {e}")

                else:
                    print(f"Module {elem} not found in {PC}/.")


            time.sleep(10)
    except Exception as e:
        print(f"Unexpected error: {e}")


process()

"""
repos.create_file(f"{PC}/{PC}_work.py", "Start new work", start_code)