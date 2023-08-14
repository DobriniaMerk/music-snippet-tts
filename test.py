import subprocess

counter = 0
filename = 'I_Have_The_High_Ground_(Star_Wars_Song)'
wordc, start, end = 5, 10200, 10330
subprocess.run(f'sox {filename}.mp3 {counter}.mp3 trim {float(start) / 100} ={float(end) / 100}',
               shell=True)
