from unittest import TestCase
from api.models import RiskScore, RiskScoreResult, ScoreChoice

class UserScoreResultMappingTest(TestCase):
    def test_should_map_all_scores_from_result(self):
        score = RiskScore(auto=0, disability=1, life=3, home=1000)
        result = RiskScoreResult(score)
        
        self.assertEqual(result.auto, ScoreChoice.ECONOMIC)
        self.assertEqual(result.disability, ScoreChoice.REGULAR)
        self.assertEqual(result.life, ScoreChoice.RESPONSIBLE)
        self.assertEqual(result.home, ScoreChoice.INELEGIBLE)