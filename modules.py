import dspy
from signatures import GenerateAnswer, GenerateKeywords, GenerateMarketSummary

# The KeywordGenerator class
class KeywordGenerator(dspy.Module):
  # The constructor
  def __init__(self):
    super().__init__()
    self.generate_keyword = dspy.ChainOfThought(GenerateKeywords)

  # The method used for calling the model.
  def forward(self, topic, description):
    prediction = self.generate_keyword(topic=topic, description=description);

    return dspy.Prediction(topic=topic, description=description, keywords=prediction.keywords)


# The CoT class
class CoT(dspy.Module):
  # The constructor
  def __init__(self):
    super().__init__()
    self.generate_summary = dspy.ChainOfThought(GenerateAnswer)

  # The method used for calling the model.
  def forward(self, topic, description, discussion):
    prediction = self.generate_summary(topic=topic, description=description, discussion=discussion);

    return dspy.Prediction(topic=topic, description=description, answer=prediction.answer)


# The FinalAnswerBot class
class FinalAnswerBot(dspy.Module):
  # The constructor
  def __init__(self):
    super().__init__()
    self.generate_finalsummary = dspy.ChainOfThought(GenerateMarketSummary)

  # The method used for calling the model.
  def forward(self, topic, description, keywords, summaries):
    prediction = self.generate_finalsummary(topic=topic, description=description, keywords=keywords, summaries=summaries);

    return dspy.Prediction(topic=topic, description=description, answer=prediction.final_answer)