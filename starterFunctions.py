from alive_progress import alive_bar
import progressbar
from time import sleep
from progress.spinner import MoonSpinner

def animated_marker():
    with MoonSpinner('Loading…') as bar:
      for i in range(10):
          sleep(0.1)
          bar.next()
        
def levelLoad():
      
    widgets = ['Loading level: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(20):
        sleep(0.1)
        bar.update(i)

def healingAnimation():
      
    with alive_bar(20) as bar:   # default setting
      for i in range(20):
          sleep(0.03)
          bar() 