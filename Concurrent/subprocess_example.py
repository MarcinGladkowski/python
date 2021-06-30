import subprocess, time, os

result = subprocess.run(
    ['echo', 'Welcome from child process!'],
    capture_output=True,
    encoding='utf-8'
)

result.check_returncode()
print(result.stdout)

proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('Working...')

# execute when process is finished
print('Exit code', proc.poll())


start = time.time()
sleep_procs = []
for _ in range(10):
    proc = subprocess.Popen(['sleep', '1'])
    sleep_procs.append(proc)


for proc in sleep_procs:
    proc.communicate()


end = time.time()
delta = end - start
print(f'Finished in time {delta:.3f} seconds')


def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'dasdasddqwq/wqeqwe/weqwe'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc


procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_encrypt(data)
    procs.append(proc)


for proc in procs:
    out, _ = proc.communicate()
    print(out[-10:])
