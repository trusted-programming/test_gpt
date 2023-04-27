import openai
import json

f = open('test_pairs.json')
data = json.load(f)

with open("sample_before.txt") as f_1:
  sample_before = f_1.read()

with open("sample_after.txt") as f_2:
  sample_after = f_2.read()


openai.api_key = "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"

def answer_txl_prompt(prompt):
  result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "system", "content": "You are a helpful programming assistant. You only answer question related to programming. More \
            specificially, your job is to provide remediation to fix Rust code. You only need to provide code after remediation, don't need to explain the reason."},
          {"role": "user", "content": f"Please help to fix this warning of this Rust code {sample_before}"},
          {"role": "assistant", "content": sample_after},
          {"role": "user", "content": f"Please help to fix this warning of this Rust code {prompt}"},
      ]
  )
  return result

for item in data:
  before = item["before"]
  prompt = f"Please help to fix this warning of this Rust code {before}"
  result = answer_txl_prompt(prompt)
  
  exact_match = 


  
