def time_to_seconds(time_str):
    """Convert a time string in the format 'MM:SS' to total seconds."""
    # 3:53:29
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours*60*60 + minutes * 60 + seconds


# Example usage
# time_in_seconds = time_to_seconds("3:35:32")

youtube_prefix_string = "https://youtu.be/HGOBQPFzWKo?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&t="
time_str = "3:53:29"
time_in_seconds = time_to_seconds(time_str)
print(time_in_seconds)
print(f"Youtube link: {youtube_prefix_string}{time_in_seconds}")
