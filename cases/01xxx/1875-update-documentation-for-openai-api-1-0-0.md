# vllm-project/vllm#1875: Update documentation for OpenAI API > 1.0.0

| 字段 | 值 |
| --- | --- |
| Issue | [#1875](https://github.com/vllm-project/vllm/issues/1875) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Update documentation for OpenAI API > 1.0.0

### Issue 正文摘录

Hi, I'd like to use vllm with the openAI python API, so I can switch between VLLM and OpenAI just by changing the URL. I have `openai` version 1.3.5. [Here are the docs ](https://docs.vllm.ai/en/latest/getting_started/quickstart.html#using-openai-chat-api-with-vllm): ```python import openai # Set OpenAI's API key and API base to use vLLM's API server. openai.api_key = "EMPTY" openai.api_base = "http://localhost:8000/v1" chat_response = openai.ChatCompletion.create( model="facebook/opt-125m", messages=[ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Tell me a joke."}, ] ) print("Chat response:", chat_response) ``` This results in the following error: ```bash openai.lib._old_api.APIRemovedInV1: You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API. You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28` A detailed migration guide is available here: https://github.com/openai/openai-python/discussi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: switch between VLLM and OpenAI just by changing the URL. I have `openai` version 1.3.5. [Here are the docs ](https://docs.vllm.ai/en/latest/getting_started/quickstart.html#using-openai-chat-api-with-vllm): ```python imp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: p://localhost:8000/v1" chat_response = openai.ChatCompletion.create( model="facebook/opt-125m", messages=[ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Tell me a joke."}, ]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: `openai` version 1.3.5. [Here are the docs ](https://docs.vllm.ai/en/latest/getting_started/quickstart.html#using-openai-chat-api-with-vllm): ```python import openai # Set OpenAI's API key and API base to use vLLM's API...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
