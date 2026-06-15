# vllm-project/vllm#18376: [Bug]: decoding output parsing error

| 字段 | 值 |
| --- | --- |
| Issue | [#18376](https://github.com/vllm-project/vllm/issues/18376) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: decoding output parsing error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Why is the following an incorrect request format? It works with OpenAI gpt-4o but when using `google/gemma-3-27b-it` (and likely other models too) on vLLM, it fails. ``` {'method': 'post', 'url': '/chat/completions', 'headers': {'X-Stainless-Helper-Method': 'beta.chat.completions.parse'}, 'files': None, 'idempotency_key': 'stainless-python-retry-42a16cd2-93af-4312-90d1-567a3acf2f8a', 'post_parser': .parser at 0x7f12b471dbc0>, 'json_data': {'messages': [{'role': 'system', 'content': 'You are a mathematical assistant.'}, {'role': 'user', 'content': 'Calculate 10 raised to the power of 7.'}], 'model': 'google/gemma-3-27b-it', 'frequency_penalty': 0.0, 'max_tokens': 2000, 'response_format': {'type': 'json_schema', 'json_schema': {'schema': {'properties': {'explanation': {'description': 'Explanation of the answer. If you cannot answer the question, please return null.', 'title': 'Explanation', 'type': 'string'}, 'answer': {'description': 'Only the final mathematical solution to the question without any explanation. Put your final answer within \\boxed{}. If you cannot answer the question, please return null.', 'title': 'Answer', 'type...

## 现有链接修复摘要

#19565 [V1] Resolve failed concurrent structred output requests

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: d: ``` ERROR 05-20 02:34:53 [backend_xgrammar.py:167] Failed to advance FSM for request chatcmpl-38e0c975fd1e45c2b01973993919c150 for tokens 0. Please file an issue. ``` And with `guidance` backend: ``` [backend_guidanc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nt ### 🐛 Describe the bug Why is the following an incorrect request format? It works with OpenAI gpt-4o but when using `google/gemma-3-27b-it` (and likely other models too) on vLLM, it fails. ``` {'method': 'post', 'url...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: :8000/v1/chat/completions ``` I get the following error with `xgrammar` backend: ``` ERROR 05-20 02:34:53 [backend_xgrammar.py:167] Failed to advance FSM for request chatcmpl-38e0c975fd1e45c2b01973993919c150 for tokens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nvironment ### 🐛 Describe the bug Why is the following an incorrect request format? It works with OpenAI gpt-4o but when using `google/gemma-3-27b-it` (and likely other models too) on vLLM, it fails. ``` {'method': 'pos...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#19565](https://github.com/vllm-project/vllm/pull/19565) | closes_keyword | 0.95 | [V1] Resolve failed concurrent structred output requests | Closes #18376 Related to #18780 Several people have noticed errors when using both the `xgrammar` and `guidance` backends where we would start generating invalid tokens for a requ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
