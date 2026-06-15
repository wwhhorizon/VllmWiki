# vllm-project/vllm#1183: Adding stop condition  - Generates garbage output

| 字段 | 值 |
| --- | --- |
| Issue | [#1183](https://github.com/vllm-project/vllm/issues/1183) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Adding stop condition  - Generates garbage output

### Issue 正文摘录

**Hi I am using HuggingFace/Starchat Model for inferencing** `python -m vllm.entrypoints.api_server --model HuggingFaceH4/starchat-alpha` **Here is request** `Received chat completion request: prompt=[{'role': 'user', 'content': 'can you write me python function for adding two numbers'}] model='HuggingFaceH4/starchat-alpha' temperature=0.0 top_p=1.0 n=1 max_tokens=1000 stop=[] stream=False presence_penalty=0.0 frequency_penalty=0.0 logit_bias=None user=None best_of=None top_k=-1 ignore_eos=False use_beam_search=False stop_token_ids=[] messages=[{'role': 'user', 'content': 'can you write me python function for adding two numbers'}]` **Output generated here is** `{ "id": "232de1f8-0ada-4bc6-9a7c-2da57d873557", "object": "chat.completion", "created": "20230926081001184846", "drafts": [ { "id": "cmpl-785e899e1d4c4c68b9a6ed80b5e0da1d", "object": "chat.completion", "created": 1695715776, "model": "HuggingFaceH4/starchat-alpha", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "Sure, here's an example of a Python function that adds two numbers:\n\n```python\ndef add(a, b):\n return a + b\n```\n\nYou can call this function like this:\n\n```python\nresult = add(1, 2)...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Adding stop condition - Generates garbage output **Hi I am using HuggingFace/Starchat Model for inferencing** `python -m vllm.entrypoints.api_server --model HuggingFaceH4/starchat-alpha` **Here is request** `Received ch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: .entrypoints.api_server --model HuggingFaceH4/starchat-alpha` **Here is request** `Received chat completion request: prompt=[{'role': 'user', 'content': 'can you write me python function for adding two numbers'}] model=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tes garbage output **Hi I am using HuggingFace/Starchat Model for inferencing** `python -m vllm.entrypoints.api_server --model HuggingFaceH4/starchat-alpha` **Here is request** `Received chat completion request: prompt=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: stop condition - Generates garbage output **Hi I am using HuggingFace/Starchat Model for inferencing** `python -m vllm.entrypoints.api_server --model HuggingFaceH4/starchat-alpha` **Here is request** `Received chat comp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: at-alpha' temperature=0.0 top_p=1.0 n=1 max_tokens=1000 stop=[] stream=False presence_penalty=0.0 frequency_penalty=0.0 logit_bias=None user=None best_of=None top_k=-1 ignore_eos=False use_beam_search=False stop_token_i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
