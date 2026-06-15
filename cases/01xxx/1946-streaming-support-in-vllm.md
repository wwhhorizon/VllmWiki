# vllm-project/vllm#1946: Streaming support in VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#1946](https://github.com/vllm-project/vllm/issues/1946) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Streaming support in VLLM

### Issue 正文摘录

Hi Team, I tried using llama 7b for streaming using following code on Jupyter Notebook- llm = VLLM(model="meta-llama/Llama-2-7b-chat-hf", use_auth_token=token, max_new_tokens=128,temperature=0.1, top_p=1, num_beams=1,top_k=50, trust_remote_code=True, load_in_4bit=True, streaming=True, callbacks=[StreamingStdOutCallbackHandler()]) For getting tokens i tried - 1. llm("tell me a long story") 2. for chunk in llm.stream("Write me a song about sparkling water."): print(chunk, end="", flush=True) 3. llm.generate(["Write me a song about rain."]) I am getting the response but in one shot and not token wise. ![image](https://github.com/vllm-project/vllm/assets/35100919/e91ca21d-c183-44cb-a217-6d8ba4add2b2) ![image](https://github.com/vllm-project/vllm/assets/35100919/5aba3437-5788-4211-bba0-4ef1d4908fc4) ![image](https://github.com/vllm-project/vllm/assets/35100919/aeeb0e68-2d96-4259-9479-00ed5bd52b8b) How to i get proper streaming on Jupyter Notebook.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Streaming support in VLLM Hi Team, I tried using llama 7b for streaming using following code on Jupyter Notebook- llm = VLLM(model="meta-llama/Llama-2-7b-chat-hf", use_auth_token=token, max_new_tokens=128,temperature=0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
