import sys , time, winsound
number_shape = 0                                 # defined

def update_progress(progress):
    barLength = int(number_shape)  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "Error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done!\r\n"
    block = int(round(barLength * progress))
    text = "\rPercentage completed: [{0}] {1}% {2}".format("#"
    *block + "-"*(barLength - block), round(progress * 100, 2), status)
    sys.stdout.write(text)
    sys.stdout.flush()


def beep_sound(times):
    frequency = 2500  # Set Frequency
    duration = 1000  # Set Duration  (1000 ms = 1 second)
    for i in range(int(times)):
        winsound.Beep(frequency, duration)
