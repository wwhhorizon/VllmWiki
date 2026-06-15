# vllm-project/vllm#2653: IndexError when using Beam Search in Chat Completions

| 字段 | 值 |
| --- | --- |
| Issue | [#2653](https://github.com/vllm-project/vllm/issues/2653) |
| 状态 | closed |
| 标签 | bug;good first issue;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> IndexError when using Beam Search in Chat Completions

### Issue 正文摘录

I know this may not be supported given the added complexity, but I just wanted some clarification because I was surprised to see that I could pass these parameters to the server. Right now I non-deterministically hit an IndexError [here](https://github.com/vllm-project/vllm/blob/2e0b6e775756345aa1d39f772c186e00f8c29e92/vllm/entrypoints/openai/api_server.py#L336) Here is a simple client/server example. I am using v0.2.7 ``` python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-Instruct-v0.1 ``` ``` from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) chat_completion = client.chat.completions.create( messages=[{"role": "user", "content": "Hello, world!"}], model="mistralai/Mistral-7B-Instruct-v0.1", max_tokens=128, temperature=0, stream=True, extra_body={ "use_beam_search": True, "best_of": 3 } ) for chunk in chat_completion: if chunk.choices[0].delta.content: print(chunk.choices[0].delta.content, end="", flush=True) ```

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: sed to see that I could pass these parameters to the server. Right now I non-deterministically hit an IndexError [here](https://github.com/vllm-project/vllm/blob/2e0b6e775756345aa1d39f772c186e00f8c29e92/vllm/entrypoints...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: i_server --model mistralai/Mistral-7B-Instruct-v0.1 ``` ``` from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: IndexError when using Beam Search in Chat Completions bug;good first issue;stale I know this may not be supported given the added complexity, but I just wanted some clarification because I was surprised to see that I co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e. I am using v0.2.7 ``` python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-Instruct-v0.1 ``` ``` from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" cl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: dexError when using Beam Search in Chat Completions bug;good first issue;stale I know this may not be supported given the added complexity, but I just wanted some clarification because I was surprised to see that I coul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
