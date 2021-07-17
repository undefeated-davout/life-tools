import subprocess
import re

if __name__ == '__main__':
    args = ["sudo", "-S", "tmutil", "listlocalsnapshots", "/"]
    try:
        tmutil = subprocess.check_output(args)
        print("tmutil", str(tmutil))
        tm_list = re.findall(r'\d{4}-\d{2}-\d{2}-\d{6}', str(tmutil))

        for tm in tm_list:
            print('tm', tm)
            args = ['tmutil', "deletelocalsnapshots", tm]
            res = subprocess.check_call(args)
            print('deletelocalsnapshots', res)
        print('success')
    except Exception as e:
        print("Error", e)
