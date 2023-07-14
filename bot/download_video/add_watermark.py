import glob
import os

import moviepy.editor as mp


def input_video_path() -> str:
    file_pattern = 'today/*.mp4'
    matching_files = glob.glob(file_pattern)

    for file_path in matching_files:
        relative_path = os.path.relpath(file_path, start='today')
        return relative_path


def add_watermark(input_video: str, watermark: str, output_video: str):
    video = mp.VideoFileClip(input_video)

    logo = (mp.ImageClip(watermark)
            .set_duration(video.duration)
            # .resize(height=50)  # if you need to resize...
            .margin(right=8, top=8, opacity=0)
            .set_pos(("right", "top")))

    final = mp.CompositeVideoClip([video, logo])
    final.write_videofile(output_video)


# Example usage
input_video_path = 'today/' + input_video_path()
watermark_path = "watermark.png"
output_video_path = "video/watermark_video.mp4"

add_watermark(input_video_path, watermark_path, output_video_path)
