# Personalized Marketing Campaign Analysis

## Executive Summary

**Objective:** Determine if personalized marketing contents are more effective than control in subscribing users, and if so, what is their lift?

In this month-long campaign, two versions of marketing contents - control and personalized - were distributed across various channels, including Facebook, Instagram, email, push notification, and house ads. Personalized contents outperformed the control across most channels, with Instagram and push notification showing remarkable lifts of 451% and 408%, respectively. However, house ads exhibited a negative lift due to a bug that reset users' displayed language, leading to a mismatch with their preferred language. This bug resulted in a loss of approximately 32 subscribers. The analysis suggests the importance of presenting personalized marketing contents while ensuring consistent language display to maximize user subscriptions.

## 1. Import and Prepare Data

To begin the analysis, the dataset was imported and preprocessed. Data types were adjusted, converting categorical variables, and date columns to appropriate formats.

## 2. Comparison of Control and Personalized Contents

The analysis explored whether the number of users exposed to control and personalized contents differed across marketing channels. Except for house ads, personalized contents consistently had a higher user count. The differences were quantified, emphasizing the significance of disparities in Instagram and push notification channels.

## 3. Visualizing Conversion Rates

The conversion rates of control and personalized contents were visualized throughout the campaign for various marketing channels. Generally, personalized contents exhibited higher conversion rates, except for house ads, where control initially performed better but declined over time.

A function, `conversion_rate`, was introduced for calculating conversion rates across different categorical variables, facilitating the analysis.

## 4. Overall Lift and Statistical Significance

The overall lift was calculated for each marketing channel, highlighting the effectiveness of personalized contents. Statistical significance tests confirmed the significance of the differences, except for house ads, where further investigation was recommended.

## 5. Further Investigation on House Ads

An in-depth analysis of house ads revealed a sudden drop in conversion rates on January 11th. It was identified that a bug had reset users' displayed language, impacting non-English language users more significantly.

- **Language Matching Bug:** Users' displayed language did not match their preferred language after the bug.
- **Impact on Conversion Rates:** Non-English language users experienced a considerable drop in conversion rates after the bug.

## 6. Estimating Potential Subscribers Lost

The analysis estimated the number of potential subscribers lost due to the bug. By comparing conversion rates before and after the bug, it was found that about 32 subscribers may have been lost.

## 7. Conclusion and Recommendations

- **Effectiveness of Personalized Contents:** Personalized contents were highly effective, especially on Instagram and in push notifications.
- **Language Matching Bug:** A bug affecting non-English language users resulted in a negative lift for house ads.
- **Recommendations:**
  - Continue using personalized contents, ensuring displayed and preferred languages match.
  - Investigate and address the bug to prevent future disruptions.
  - Conduct further A/B testing within personalized contents to optimize subscription rates.

This comprehensive analysis provides valuable insights for refining marketing strategies and addressing technical issues to enhance user engagement and subscription rates.
