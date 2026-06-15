# vllm-project/vllm#24184: [Bug]: responses api - no way to tell if finish reason is length

| 字段 | 值 |
| --- | --- |
| Issue | [#24184](https://github.com/vllm-project/vllm/issues/24184) |
| 状态 | closed |
| 标签 | bug;gpt-oss |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: responses api - no way to tell if finish reason is length

### Issue 正文摘录

### Your current environment vLLM v0.10.1.1 ### 🐛 Describe the bug I expected the following to give some kind of indication that the finish reason is token exhaustion. If I don't set `max_tokens` there is no way of knowing what the default is, otherwise maybe I could compare to usage counts. ```python import openai import os client = openai.OpenAI( api_key=os.environ["VLLM_API_KEY"], base_url='http://localhost:8000/v1', ) client.responses.create( input='What is 2+2?', max_output_tokens=1 ) ``` Response: ```python Response(id='resp_ad19788ca7754eeea9bc3a2dc6c722a4', created_at=1756918602.0, error=None, incomplete_details=None, instructions=None, metadata=None, model='openai/gpt-oss-20b', object='response', output=[], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[], top_p=1.0, background=False, conversation=None, max_output_tokens=1, max_tool_calls=None, previous_response_id=None, prompt=None, prompt_cache_key=None, reasoning=None, safety_identifier=None, service_tier='auto', status='completed', text=None, top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=0, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=0, outpu...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: at=1756918602.0, error=None, incomplete_details=None, instructions=None, metadata=None, model='openai/gpt-oss-20b', object='response', output=[], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[],...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: responses api - no way to tell if finish reason is length bug;gpt-oss ### Your current environment vLLM v0.10.1.1 ### 🐛 Describe the bug I expected the following to give some kind of indication that the finish re...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: default is, otherwise maybe I could compare to usage counts. ```python import openai import os client = openai.OpenAI( api_key=os.environ["VLLM_API_KEY"], base_url='http://localhost:8000/v1', ) client.responses.create(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
