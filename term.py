import mss
from PIL import Image
import time
import os
import sys
import argparse

def render_image_to_terminal(img, term_width, term_height):
    if term_width <= 0 or term_height <= 0:
        return    
    resized_img = img.resize((term_width, term_height * 2), Image.Resampling.LANCZOS)
    output_buffer = []
    output_buffer.append("\033[H")
    for y in range(term_height):
        for x in range(term_width):
            top_r, top_g, top_b = resized_img.getpixel((x, y * 2))
            bottom_r, bottom_g, bottom_b = resized_img.getpixel((x, y * 2 + 1))
            output_buffer.append(f"\033[38;2;{top_r};{top_g};{top_b}m")
            output_buffer.append(f"\033[48;2;{bottom_r};{bottom_g};{bottom_b}m")
            output_buffer.append("▀")
        output_buffer.append("\033[0m")
        if y < term_height - 1:
            output_buffer.append("\n")
    sys.stdout.write("".join(output_buffer))
    sys.stdout.flush()


def main(monitor_num, interval):
    """Main function to capture and display the screen."""
    try:
        sys.stdout.write("\033[?25l")
        os.system('cls' if os.name == 'nt' else 'clear')

        with mss.mss() as sct:
            if monitor_num >= len(sct.monitors):
                print(f"Error: Monitor {monitor_num} not found.")
                available_monitors = len(sct.monitors) - 1
                print(f"There are only {available_monitors} monitor(s) available.")
                if available_monitors > 0:
                    print(f"Try running with '-m 1' for the primary monitor.")
                return

            monitor = sct.monitors[monitor_num]
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Capturing monitor {monitor_num}. Press Ctrl+C to exit.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')


            while True:
                frame_start_time = time.time()

                try:
                    term_cols, term_rows = os.get_terminal_size()
                except OSError:
                    term_cols, term_rows = 80, 24

                sct_img = sct.grab(monitor)
                img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

                if term_rows > 1:
                     render_image_to_terminal(img, term_cols, term_rows - 1)

                elapsed_time = time.time() - frame_start_time
                sleep_time = interval - elapsed_time
                if sleep_time > 0:
                    time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\nProgram interrupted. Cleaning up and exiting...")
    finally:
        sys.stdout.write("\033[?25h\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display a live feed of a monitor in the terminal.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-m", "--monitor", type=int, default=2,
        help=(
            "Monitor number to capture.\n"
            "  1 = Primary monitor\n"
            "  2 = Second monitor (if available)\n"
            "Default is 2."
        )
    )
    parser.add_argument(
        "-i", "--interval", type=float, default=1.0,
        help="Refresh interval in seconds. Smaller numbers mean faster updates.\nDefault is 1.0."
    )
    args = parser.parse_args()

    main(args.monitor, args.interval)

