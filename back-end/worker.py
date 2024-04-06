import subprocess
import time
import psutil
import os

def run_python(filename, input_data, timeout, mem_lim):
    execution_process = subprocess.Popen(['python', filename], 
                                        stdout = subprocess.PIPE, 
                                        stderr = subprocess.PIPE, 
                                        stdin = subprocess.PIPE,
                                        bufsize = 256)
    psutil_process = psutil.Process(execution_process.pid)
    max_memory = 0
    start_time = time.time()
    output, errors = "".encode(), "".encode()
    time_taken = 0

    try:
        execution_process.communicate(bytes(input_data, 'utf-8'),timeout = 0)
    except Exception as e:
        pass    
    while True:
        try:
            current_memory = psutil_process.memory_info().rss
        except Exception as e:
            current_memory = current_memory
        max_memory = max(max_memory, current_memory)
        time_taken = time.time() - start_time
        if (time.time() - start_time) > timeout:
            execution_process.kill()
            break

        if max_memory > mem_lim:
            execution_process.kill()
            break

        if execution_process.poll() is not None:
            output, errors = execution_process.communicate()
            break

        time.sleep(0.001)
    
    if execution_process.returncode:
        global RE
        RE = True
    return output.decode(),time_taken,max_memory, errors.decode()


def run_cpp(filename, input_data, timeout, mem_lim):
    compilation_process = subprocess.Popen(['g++', filename, '-o', 'compiled_cpp'], 
                                           stderr = subprocess.PIPE)
    _, compilation_errors = compilation_process.communicate()
    if compilation_process.returncode:
        global CE 
        CE = True
        return '', 0, 0, compilation_errors.decode()
    time.sleep(1)
    execution_process = subprocess.Popen(['./compiled_cpp.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    psutil_process = psutil.Process(execution_process.pid)
    max_memory = 0
    start_time = time.time()
    output, errors = "".encode(), "".encode()
    time_taken = 0

    try:
        execution_process.communicate(bytes(input_data, 'utf-8'),timeout = 0)
    except Exception as e:
        pass    
    while True:
        try:
            current_memory = psutil_process.memory_info().rss
        except Exception as e:
            current_memory = current_memory
        max_memory = max(max_memory, current_memory)
        time_taken = time.time() - start_time
        if (time.time() - start_time) > timeout:
            execution_process.kill()
            break

        if max_memory > mem_lim:
            execution_process.kill()
            break

        if execution_process.poll() is not None:
            output, errors = execution_process.communicate()
            break

        time.sleep(0.001)
    
    if execution_process.returncode:
        global RE
        RE = True
    return output.decode(),time_taken,max_memory, errors.decode()


def run_code(filename, input_data, time_limit, mem_lim):
    if filename.endswith('.py'):
        return run_python(filename, input_data, time_limit, mem_lim)
    elif filename.endswith('.cpp'):
        return run_cpp(filename, input_data, time_limit, mem_lim)


def check_answer(answer, output):
    answer_array = answer.split()
    output_array = output.split()
    if answer_array == output_array:
        return True
    else:
        return False


def check_time(total_time, limit):
    if total_time > limit:
        return True
    else:
        return False
    
def check_mem(total_mem, limit):
    if total_mem > limit:
        return True
    else:
        return False


def worker(data):
    time_limit = data['tle']
    mem_limit = data['mle']
    global CE, RE
    RE = False
    CE = False

    code = data['code']
    source_code = 'code' + str(data['id'])

    if data['code_lang'] == 'C++':
        source_code += '.cpp'
    elif data['code_lang'] == "Python":
        source_code += '.py'
    else:
        data['runner_output'] = "Invalid Language"
        return data
    
    with open(source_code, 'w') as file:
        file.write(code)

    answer = data['answer']
    input_data = data['input']

    output, total_time, total_mem, errors = run_code(source_code, input_data, time_limit, mem_limit)
    data['runner_output'] = {
        'verdict': '', 
        'error': '',
        'time': total_time, 
        'memory': total_mem
    }

    if RE:
        data['runner_output']['verdict'] = "Runtime error"
        data['runner_output']['error'] = errors
    elif CE:
        data['runner_output']['error'] = errors
        data['runner_output']['verdict'] = "Compilation error"
        data['runner_output']['memory'] = 0
        data['runner_output']['time'] = 0
    elif check_time(total_time, time_limit):
        data['runner_output']['verdict'] = "Time Limit Exceeded"
    elif check_mem(total_mem, mem_limit):
        data['runner_output']['verdict'] = "Memory Limit Exceeded"
    elif check_answer(answer, output):
        data['runner_output']['verdict'] = "Accepted"
    else:
        data['runner_output']['verdict'] = "Wrong Answer"

    try:
        os.remove(source_code)
        if data['code_lang'] == 'C++':
            os.remove('compiled_cpp.exe')
    except OSError as e:
        print("Error removing the file")
    return data


data = {
    'id': 1,
    'created_at': '', 
    'code': 'print(3)', 
    'ex_status': '', 
    'runner_output': {}, 
    'code_lang': 'Python', 
    'user': None, 
    'problemID': None,
    'input': '',   
    'answer': '3', 
    'tle': 1,
    'mle': 256000000
} 

output = worker(data)
print(output['runner_output'])   