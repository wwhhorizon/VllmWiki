# vllm-project/vllm#3848: [Usage]: No attribute "get" error when running mixtral via vllm api server

| 字段 | 值 |
| --- | --- |
| Issue | [#3848](https://github.com/vllm-project/vllm/issues/3848) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: No attribute "get" error when running mixtral via vllm api server

### Issue 正文摘录

`###` Your current environment vllm: 0.3.3 openai: 1.14.3 ### How would you like to use vllm I want to run inference using Mixtral8x7b. When I run a vllm api server and query it i get the following error: Failed to fetch data for lvx_nova-lvx_nova-01-contimune-30-59 due to 'ChatCompletionChunk' object has no attribute 'get'. I query like this, it's an existing script where i want to use a self-deployed mixtral as drop-in replacement for gpt. ``` COMMENT override base url client = OpenAI( api_key=OPENAI_KEY, base_url=OPENAI_BASEURL, ) for retry in range(NUM_RETRIES): try: response_iterator = client.chat.completions.create( model=model, messages=messages, stream=True, timeout=60, ) response_chunks = [] for chunk in response_iterator: if not chunk.get("choices", []): continue if chunk["choices"][0]["finish_reason"] == "length": raise ValueError( "Model returned too much data before running out of available token space!" ) text = chunk["choices"][0]["delta"].get("content") if text: response_chunks.append(text) text = "".join(response_chunks) return prompt_helper.postprocess_response_text(text, query, uri) except Exception as e: last_exception = e time.sleep(2**retry) print(f"Failed to...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: response_iterator = client.chat.completions.create( model=model, messages=messages, stream=True, timeout=60, ) response_chunks = [] for chunk in response_iterator: if not chunk.get("choices", [

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
