import glob
import os

import moviepy.video.fx.resize
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip


def input_video_path() -> str:
    file_pattern = 'today/*.mp4'
    matching_files = glob.glob(file_pattern)

    for file_path in matching_files:
        relative_path = os.path.relpath(file_path, start='today')
        return relative_path


def add_watermark(input_video_path: str, watermark_path: str, output_video_path: str):
    # Load the video clip
    video = VideoFileClip(input_video_path)

    # Load the watermark image
    watermark = ImageClip(watermark_path)

    # Resize the watermark if necessary
    watermark = moviepy.video.fx.resize.resize(watermark, height=50)

    # Define the position of the watermark on the video
    watermark_position = (video.size[0] - watermark.size[0] - 10, 10)

    # Create a composite video clip with the watermark overlay
    video_with_watermark = CompositeVideoClip([
        video,
        watermark.set_position(watermark_position).set_duration(video.duration)
    ])

    # Save the processed video
    video_with_watermark.write_videofile(output_video_path, codec="libx264")


# Example usage
input_video_path = 'today/' + input_video_path()
watermark_path = "watermark.png"
output_video_path = "video/watermark_video.mp4"

add_watermark(input_video_path, watermark_path, output_video_path)
