Ethics and Sustainability Statement
Project: MVTec Bottle Defect Detection System

Date: March 2026

1. Safety and Reliability (The "False Negative" Risk)
In industrial manufacturing, the most significant ethical risk is a False Negative (Type II Error)—where the AI labels a dangerous defect (like a crack or glass shard) as "Good."

Risk: Over-reliance on automation could lead to contaminated products reaching consumers.

Mitigation: This system is designed as human-in-the-loop. We have configured the Reinforcement Learning (RL) agent with an asymmetric reward function that penalizes missed defects 10x more than false alarms. This ensures the system defaults to "Caution" and human review when uncertain.

2. Impact on the Workforce
The introduction of computer vision for Quality Control (QC) raises concerns regarding the displacement of human inspectors.

Perspective: Our goal is Augmentation, not replacement. Automated screening handles the repetitive task of filtering thousands of "Good" samples, reducing eye fatigue and mental strain for human workers. This allows inspectors to focus their specialized expertise on complex, ambiguous cases.

3. Transparency and Model Interpretability
AI "Black Boxes" are dangerous in manufacturing.

Risk: If the model fails, engineers need to know why it failed.

Mitigation: We are documenting the model's limitations via a Model Card. We acknowledge that the MVTec dataset is a controlled environment; therefore, the model is currently only certified for the specific lighting and bottle types found in that training set.

4. Environmental Sustainability
Training large deep learning models can be energy-intensive.

Strategy: We utilized a lightweight CNN architecture (BottleCNN) and targeted training (Transfer Learning principles) to minimize GPU compute time. This ensures the model can eventually run on low-power Edge AI devices directly on the factory floor, rather than requiring high-emission data centers.