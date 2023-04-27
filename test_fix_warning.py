import openai
import json

f = open('test_pairs.json')
data = json.load(f)

with open("sample_before_1.txt") as f_before_1:
  sample_before_1 = f_before_1.read()

with open("sample_after_1.txt") as f_after_1:
  sample_after_1 = f_after_1.read()

with open("sample_before_2.txt") as f_before_2:
  sample_before_2 = f_before_2.read()

with open("sample_after_2.txt") as f_after_2:
  sample_after_2 = f_after_2.read()


# openai.api_key = "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"
openai.api_key = "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"

def answer_txl_prompt(prompt):
  result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "system", "content": "You are a helpful programming assistant. You only answer question related to programming. More \
            specificially, your job is to provide remediation to fix Rust code. You only need to provide code after remediation, don't need to explain the reason."},
          {"role": "user", "content": f"Please help to provide remediation of this Rust code {sample_before_1}"},
          {"role": "assistant", "content": sample_after_1},
           {"role": "user", "content": f"Please help to provide remediation  of this Rust code {sample_before_2}"},
          {"role": "assistant", "content": sample_after_2},
          {"role": "user", "content": f"Please help to provide remediation  of this Rust code {prompt}"},
      ]
  )
  return result["choices"][0]["message"]["content"]

# max_length = 4096
with open("prediction_results.txt", "w") as f_predict:
  for item in data:
    if len(item["before"].split()) < 100:
      before = item["before"]
      prompt = f"Please help to fix this warning of this Rust code {before}"
      result = answer_txl_prompt(prompt)
      
      # result = "".join(result.split())
      # print(item["after"])
      # print(result)
      # exact_match =
      ground_truth = item["after"]
      output = f"------------------ \n {result} \n **** {ground_truth} \n" 
      f_predict.write(output)



  
