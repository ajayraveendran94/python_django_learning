#try except finally
#to dictate our code logic in case error
#open("{file_name}", "method(w/r)")
#try except help to handel error without blocking the code execution
try:
    data = open('sample_file/sample_file.txt', 'r', encoding='utf-8')
except:
    print("Error found")
else:
    print(f"{str(data.read())}")
    data.close()
finally:
    print("Execution Finished")
