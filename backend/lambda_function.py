import sys
import subprocess
import io

def run_python(code):
    original_stdout = sys.stdout
    sys.stdout = output_capture = io.StringIO()
    
    try:
        exec(code)
        output = output_capture.getvalue()
        return {
            'statusCode': 200,
            'body': output
        }
    except Exception as e:
        return {
            'statusCode': 200,
            'body': str(e)
        }
    finally:
        sys.stdout = original_stdout


def run_java(code):
    try:
        with open('/tmp/Main.java', 'w') as f:
            f.write(code)
        subprocess.check_output(['javac', '/tmp/Main.java'])
        output = subprocess.check_output(['java', '-cp', '/tmp', 'Main'], stderr=subprocess.STDOUT)
        return {
            'statusCode': 200,
            'body': output.decode('utf-8')
        }
    except subprocess.CalledProcessError as e:
        return {
            'statusCode': 200,
            'body': e.output.decode('utf-8')
        }

def run_cpp(code):
    try:
        with open('/tmp/Main.cpp', 'w') as f:
            f.write(code)
        subprocess.check_output(['g++', '/tmp/Main.cpp', '-o', '/tmp/Main'])
        output = subprocess.check_output(['/tmp/Main'], stderr=subprocess.STDOUT)
        return {
            'statusCode': 200,
            'body': output.decode('utf-8')
        }
    except subprocess.CalledProcessError as e:
        return {
            'statusCode': 200,
            'body': e.output.decode('utf-8')
        }

def handler(event, context):
    language = event.get('language', 'python')
    code = event.get('code', '')
    
    if language == 'python':
        code = event.get('code', '')
        return run_python(code)
    elif language == 'java':
        code = event.get('code', '')
        return run_java(code)
    elif language == 'cpp':
        code = event.get('code', '')
        return run_cpp(code)
    else:
        return {
            'statusCode': 400,
            'body': 'Unsupported language' + language
        }



# if __name__ == '__main__':
#     print(handler({
#         'language': 'python',
#         'code': 'print("Hello, World!")'
#     }, None))
#     print(handler({
#         'language': 'java',
#         'code': 'public class Main { public static void main(String[] args) { System.out.println("Hello, World!"); } }'
#     }, None))
#     print(handler({
#         'language': 'cpp',
#         'code': '#include <iostream>\nint main() { std::cout << "Hello, World!" << std::endl; return 0; }'
#     }, None))




