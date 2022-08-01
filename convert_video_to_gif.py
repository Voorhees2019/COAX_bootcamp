import os.path
import uuid

from moviepy.editor import VideoFileClip


def convert_video_to_gif(video_url: str) -> str:
    """Convert video to .gif file and return filepath."""
    filename = str(uuid.uuid4()) + ".gif"  # generate random unique filename

    try:
        video_clip = VideoFileClip(video_url)
    except OSError:
        raise ValueError(
            "Video file was not found or could not be read, check the provided link and make sure"
            " the video is public"
        )

    video_clip.write_gif(filename)
    return os.path.abspath(filename)


if __name__ == "__main__":
    url = "https://v16-webapp.tiktok.com/ce6cc4281b15f87f2fc68d4694779a7d/62e838d5/video/tos/useast2a/tos-useast2a-pve-0068/6898f1d1f5bd4d1397e1d2c4594b0b2f/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1286&bt=643&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZRBc1we2Nl6eyl7Gb&mime_type=video_mp4&qs=0&rc=PGU3OmgzMzU4NzlpaTw6ZkBpM3A8OGU6ZjZlZDMzNzczM0A2XjIuM2JgXzAxLy9iXjIxYSM0cXAwcjRfbnBgLS1kMTZzcw%3D%3D&l=2022080114334501019205302306354DFD"  # noqa: E501
    print(convert_video_to_gif(url))
