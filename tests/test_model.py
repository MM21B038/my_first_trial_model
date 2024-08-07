import unittest
from your_model_package import YourModel

class TestYourModel(unittest.TestCase):
    def test_prediction(self):
        model = YourModel()
        model.train('path_to_train_data', 'path_to_val_data')  # Use dummy paths for testing
        output = model.predict('path_to_test_image')
        self.assertIn(output, ['Negative', 'Positive'])

if __name__ == '__main__':
    unittest.main()
