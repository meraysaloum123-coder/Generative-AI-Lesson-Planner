from transformers import pipeline
import torch

# 1. إعداد النموذج (تم ضبطه ليعمل بكفاءة على جهازك)
print("Loading the model (this may take a few moments)...")
generator = pipeline(
    "text-generation", 
    model="google/gemma-3-1b-it",
    model_kwargs={"torch_dtype": torch.bfloat16}, 
    device_map="auto"
)

# 2. جمع المدخلات من المستخدم (يجب أن تأتي أولاً)
print("\n--- Please enter the lesson details ---")
subject = input("(Subject): ")
title = input("(Title): ")
method = input("(Method): ")
level = input("(Level): ")
objectives = input("(Objectives): ")

# 3. صياغة الـ Prompt (الآن المتغيرات معرفة وجاهزة للاستخدام)
# 3. صياغة الـ Prompt (تم التعديل لعدم إدراج معلومات الجمهور والوقت)
prompt = f"""<start_of_turn>user
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
"""

# 4. توليد النتيجة
print("\n--- جاري توليد خطة الدرس (قد يستغرق هذا وقتاً)... ---\n")
result = generator(
    prompt, 
    max_new_tokens=4500,
    do_sample=True,
    temperature=0.7,
    repetition_penalty=1.2
)

# 5. عرض النتيجة
print("-" * 50)
# استخراج النص الناتج فقط دون تكرار الـ prompt
print(result[0]["generated_text"].split("<start_of_turn>model")[-1])
print("-" * 50)