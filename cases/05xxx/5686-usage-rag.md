# vllm-project/vllm#5686: [Usage]: RAG 

| 字段 | 值 |
| --- | --- |
| Issue | [#5686](https://github.com/vllm-project/vllm/issues/5686) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: RAG 

### Issue 正文摘录

### Your current environment vllm==0.4.0 ### How would you like to use vllm how can i pass the context for the llm so it can answer mt using only that context? currently i am trying something like this but it wont work: ```python import requests import json def ask_question(question): url = 'http://127.0.0.1:8000/v1/chat/completions' headers = { 'Content-Type': 'application/json' } # data = { # "model": "mistralai/Mistral-7B-v0.1", # "prompt": f"Answer the question in full sentence using only the context. If the context doesn't have the information, answer: I don't know. Context: Lionel Andres Messi was born on 24 Jun 1985. He is an Argentine professional football player. He played for Barcelona, Paris Saint-Germain. His current club is Inter Miami and he plays for the Argentine national team also. Until 2021, he had spent his entire professional career with Barcelona, where he won a club-record 34 trophies. Questions: {question}", # "max_tokens": 20, # "temperature": 0 # } data = { "model": "mistralai/Mistral-7B-v0.1", "messages": [ {"role": "system", "content": f"Use only the following context to answer the user questions. If the context doenst provide the information, say I don...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 'Content-Type': 'application/json' } # data = { # "model": "mistralai/Mistral-7B-v0.1", # "prompt": f"Answer the question in full sentence using only the context. If the context doesn't have the information, answer: I d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ? currently i am trying something like this but it wont work: ```python import requests import json def ask_question(question): url = 'http://127.0.0.1:8000/v1/chat/completions' headers = { 'Content-Type': 'application/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : answer = response.json() print('Answer:', answer) else: print('Failed to get a response:', response.status_code, response.text) if __name__ == '__main__': while True: question = input("Enter your question (or type 'ex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ntly i am trying something like this but it wont work: ```python import requests import json def ask_question(question): url = 'http://127.0.0.1:8000/v1/chat/completions' headers = { 'Content-Type': 'application/json' }...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
