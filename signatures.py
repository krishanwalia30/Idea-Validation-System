import dspy

class GenerateKeywords(dspy.Signature):
  """
  Your work would be to suggest keywords that shall be used for performing market research on the topic.
  Also the keywords should be SEO friendly.

  You will be provided with a topic and the description of the topic.

  The keywords must be 2-3 words long.
  You have to fully analyze the topic and its description, and based on the analysis,
  you have to return a list of 3 important keywords related to the topic.

  The topics must be seperated by comma.
  """
  topic = dspy.InputField(desc="topic of the discussion")
  description = dspy.InputField(desc="description of the topic")
  keywords = dspy.OutputField(desc="list of 3 keywords")

class GenerateAnswer(dspy.Signature):
    """ You are market research specialist.

        You are provided with a collection of discussions related to the user's "topic" and "description".
        If the discussion provided is not related to the topic, then return not much market data is present.

        You have to critically analyze the discussions and extract the following key elements:

        Sentiment Analysis
        Determine the overall sentiment of the discussions (positive, negative, neutral).
        Identify patterns or trends in sentiment over time or across different topics.
        Key Themes and Topics

        Identify common themes and topics that frequently appear in the discussions.
        Group related discussions to see which topics are most prominent.
        User Pain Points and Complaints

        Extract and categorize frequent complaints and issues users face.
        Understand the severity and impact of these pain points.
        Feature Requests and Suggestions

        Identify specific features or improvements users request.
        Gauge the popularity and demand for these features.
        User Preferences and Behaviors

        Determine what users like or dislike about existing products or services.
        Extract information on how users interact with products, their usage patterns, and preferences.
        Competitive Analysis

        Track mentions of competitors and their products.
        Analyze how the discussed idea stacks up against the competition based on user feedback.
        Demographic Information

        Gather demographic data about the users participating in the discussions (e.g., age, location, interests).
        Ensure that the feedback aligns with the target audience.
        Engagement Metrics

        Measure the number of upvotes, downvotes, comments, and replies to gauge engagement.
        Understand how discussions evolve, including the flow and depth of conversations.
        Influential Users and Thought Leaders

        Identify influential users and thought leaders within the discussions.
        Note their contributions and the impact they have on the discussions.
        Actionable Insights

        Extract actionable insights that can be implemented quickly.
        Identify insights that inform long-term product development and marketing strategies.
        FAQs and Common Misconceptions

        Compile a list of frequently asked questions and common misconceptions.
        Identify areas where users need more information or clarity.
        Emotional Triggers

        Identify comments and discussions that evoke strong emotional responses.
        Understand the underlying motivations and emotions driving user behavior.
        Market Trends and Predictions

        Identify emerging trends and shifts in user preferences.
        Extract predictions and forecasts mentioned by users or influencers.


        Provide a comprehensive summary for each of these elements based on the provided discussions.
    """
    topic = dspy.InputField(desc="topic of the discussion")
    description = dspy.InputField(desc="description of the topic")
    discussion = dspy.InputField(desc="discussion data on topic")
    answer = dspy.OutputField(desc="Market research summary with all the points")

class GenerateMarketSummary(dspy.Signature):
  """
  You are provided with a list of all the keywords used for generating seperate market research summaries.
  You have to analyse all the summaries and based on that prepare a compiled final summary depicting market condition for the topic and description.
  You are given the ultimate topic of market research and a brief description of this topic.
  You are also provided with all the keywords used for preparing separate summaries.

  The format of the final generated summary should be like,-

  # Final Summary of Market Research

## Introduction
- Briefly introduce the purpose and scope of the research.
- Mention the four keywords/topics that were investigated.

## Summary of Findings

### Overview
- Provide a high-level summary of the overall findings from all the discussions.

### Individual Keyword Analysis
- Summarize the key points and insights for each keyword.
- Highlight common themes, trends, and significant differences among the keywords.

## Comparative Analysis
- Compare and contrast the findings from the discussions of the different keywords.
- Identify any overlapping themes or unique insights specific to each keyword.

## Market Trends and Insights
- Discuss the major trends observed across all keywords.
- Highlight any emerging patterns or shifts in the market.
- Mention any potential opportunities or threats based on the discussions.

## Customer Sentiments
- Summarize the general sentiment (positive, negative, neutral) towards each keyword.
- Identify any specific concerns, preferences, or expectations expressed by the audience.

## User Pain Points and Complaints
- Extract and categorize frequent complaints and issues users face.
- Understand the severity and impact of these pain points.

## Feature Requests and Suggestions
- Identify specific features or improvements users request.
- Gauge the popularity and demand for these features.

## Actionable Insights
- Extract actionable insights that can be implemented quickly.
- Identify insights that inform long-term product development and marketing strategies.

## FAQs and Common Misconceptions
- Compile a list of frequently asked questions and common misconceptions.
- Identify areas where users need more information or clarity.

## Recommendations
- Based on your findings, provide actionable recommendations for stakeholders.
- Suggest strategies or areas for further research and exploration.

## Conclusion
- Recap the main points of the final summary.
- Reiterate the significance of the research and its implications for the market.

  """
  topic = dspy.InputField(desc="topic of the discussion")
  description = dspy.InputField(desc="description of the topic")
  keywords = dspy.InputField(desc="list of 4 keywords")
  summaries = dspy.InputField(desc="list of all the summaries")

  final_answer = dspy.OutputField(desc="Final Market research summary with all the points")