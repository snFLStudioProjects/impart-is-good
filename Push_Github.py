import subprocess

def run_command(cmd :str):
    subprocess.call(cmd, shell = True)

### 开始上传
run_command('git add -A')
run_command('git commit -m Projects')
run_command('git push origin master')
