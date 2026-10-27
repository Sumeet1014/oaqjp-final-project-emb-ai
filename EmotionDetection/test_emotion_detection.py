import unittest
from unittest.mock import patch, Mock

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy_dominant(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.01,
                        "fear": 0.02,
                        "joy": 0.94,
                        "sadness": 0.02
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very happy today")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.94)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness_dominant(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.04,
                        "sadness": 0.90
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very sad")

        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_empty_input(self):
        result = emotion_detector("")

        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
