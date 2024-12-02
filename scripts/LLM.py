import openai

# 设置 API 密钥
openai.api_key = "your_openai_api_key"

# 使用新的接口
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is the capital city of France?"}
    ]
)

# 输出响应内容
print(response.choices[0].message["content"])
