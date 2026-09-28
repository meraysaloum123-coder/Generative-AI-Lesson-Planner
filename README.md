# Generative-AI-Lesson-Planner

A powerful, structured AI prompt and framework designed for professional classroom teachers to generate full, ready-to-deliver science lesson scripts.

##  Project Overview
This repository contains a rigorously tested and refined Generative AI prompt framework. It ensures that generated lesson scripts focus strictly on **pure scientific facts, robust methodology, and dual hands-on activities** without unnecessary behavioral or non-scientific fluff.

---

##  The Approved Prompt Template

Use this exact prompt structure with your generative AI model:

```python
prompt = f\"\"\"<start_of_turn>user
You are a professional classroom teacher. Write a full, ready-to-deliver lesson script for {level} about {title}.
Subject: {subject}. Method: {method}. Objectives: {objectives}.

Requirements for the Lesson Script:
- Write the exact content the teacher will speak and the exact steps students will follow (Script format).
- Introduction: Write the exact 'hook' question and opening narrative.
- Direct Instruction: Write the scientific explanation in clear, simple language using 'Teacher Notes' in brackets for classroom management.
- TWO DISTINCT PRACTICAL ACTIVITIES: You MUST provide TWO different, fully detailed, hands-on activities. 
    - For Activity 1: Provide a step-by-step guide for a physical/visual modeling task.
    - For Activity 2: Provide a step-by-step guide for a simulation, data analysis, or interactive task that reinforces the scientific concepts.
- Assessments: Include 5 specific questions with their correct answers.
- Closure: Write the exact closing sentences.

Guidelines:
- Use encouraging, conversational, and pedagogical language.
- Use analogies for complex concepts.
- Start directly with the 'Teacher Script'. Do not include any metadata or headers.

Constraints:
- Focus strictly on scientific facts and the specified subject matter.
- Do NOT include any themes related to smartphones, social media, habit formation, or neuroplasticity.
- You MUST provide exactly TWO separate activities with full procedural steps.
- Use 'Teacher Notes' in brackets for classroom management tips or when to pause for interaction.<end_of_turn>
<start_of_turn>model
\"\"\"
