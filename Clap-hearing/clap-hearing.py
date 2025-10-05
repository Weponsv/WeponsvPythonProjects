import pyaudio
import numpy as np
import os
import time

def simple_clap_detector():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    THRESHOLD = 500  # Start with a lower threshold
    
    p = pyaudio.PyAudio()
    
    try:
        stream = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)
        
        print("Calibrating... Please be quiet for 2 seconds.")
        time.sleep(2)
        
        # Calibrate background noise
        background_levels = []
        for _ in range(10):
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.int16)
            level = np.abs(audio_data).mean()
            background_levels.append(level)
        
        avg_background = np.mean(background_levels)
        dynamic_threshold = avg_background * 25  # 25x background noise
        THRESHOLD = max(500, dynamic_threshold)  # Use whichever is higher
        
        print(f"Background noise level: {avg_background:.1f}")
        print(f"Dynamic threshold set to: {THRESHOLD:.1f}")
        print("Listening for claps... (Press Ctrl+C to stop)")
        
        last_clap = 0
        
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.int16)
            
            # Simple peak detection instead of RMS
            peak = np.max(np.abs(audio_data))
            
            current_time = time.time()
            if peak > THRESHOLD and (current_time - last_clap) > 0.5:
                print(f"Clap! Peak: {peak}")
                last_clap = current_time
                #os.system('gnome-terminal')
                
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    simple_clap_detector()
