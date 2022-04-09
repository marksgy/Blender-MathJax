import subprocess

def getOutput(latex):
    retcode = subprocess.check_output(["node","-r", "esm", "MathJax2SVG.js",latex ])
    with open('./sssvg.svg', 'w') as f:
        f.write(retcode.decode('utf8').strip())
    

if __name__ == '__main__':
    getOutput("\sum_{i=1}^n a_i+b_i")