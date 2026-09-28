from huggingface_hub import login
login(token="hf_ضع_التوكن_الذي_نسخته_هنا_مباشرة") # ضعي التوكن هنا للتجربة فقط
from transformers import AutoTokenizer
# حاولي فقط تحميل الـ tokenizer للنموذج
tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")
print("تم الاتصال بنجاح!")