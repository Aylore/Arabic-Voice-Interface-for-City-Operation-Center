import os

HOME_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLE_SECRET_KEY = os.path.join(HOME_DIR, 'utils/google_model/google_secret_key.json')
SYNTHESIZED_AUDIO = os.path.join(HOME_DIR, "Interface/google_app/static/answer.wav")
AGENT_FACE = os.path.join(HOME_DIR, "src/wav2lip/videos/test-new.mp4")
WAV2LIP_MODEL = os.path.join(HOME_DIR, "src/wav2lip/checkpoints/wav2lip_gan.pth")
GENERATED_VIDEO = os.path.join(HOME_DIR, "Interface/google_app/static/result_voice.mp4")
ENHANCE_MODEL = os.path.join(HOME_DIR, "src/wav2lip/face_restoration/CodeFormer")
ENHANCED_GENERATED_VIDEO = os.path.join(HOME_DIR, "Interface/google_app/static/enhancement")
