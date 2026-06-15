# vllm-project/vllm#29286: [Performance]: cache system prompt token ids

| 字段 | 值 |
| --- | --- |
| Issue | [#29286](https://github.com/vllm-project/vllm/issues/29286) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: cache system prompt token ids

### Issue 正文摘录

### Proposal to improve performance As system prompt can be very long now, tokenize the system prompt can be slow. Using H20, tokenize 5000 tokens cost about 10ms as below: ![Image](https://github.com/user-attachments/assets/e1b0dafa-6514-47e6-8531-db8eaea32cc7) System prompts are usually fixed and reusable, so cache the system prompt can be profitable. Specificly: 1. In **apply_hf_chat_template** method we can separate the system prompt from other prompts, we can use condition **cache_system_prompt = truncate_prompt_tokens is None and not tokenize and len(conversation) > 1 and conversation[0].get("role") == "system"** to judge when we should separate the system prompt. 2. In **_normalize_prompt_text_to_input** method we judge that whether system prompt is in the dict ({system prompt: token ids}) that we can reuse, then concat system prompt token ids and prompt token ids as the final input_ids. I am willing to contribute to this opt and looking forward to your suggestions! ### Report of performance regression The above cost can be profitable. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python c...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: opt and looking forward to your suggestions! ### Report of performance regression The above cost can be profitable. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is neces...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ly fixed and reusable, so cache the system prompt can be profitable. Specificly: 1. In **apply_hf_chat_template** method we can separate the system prompt from other prompts, we can use condition **cache_system_prompt =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: so cache the system prompt can be profitable. Specificly: 1. In **apply_hf_chat_template** method we can separate the system prompt from other prompts, we can use condition **cache_system_prompt = truncate_prompt_tokens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: cache system prompt token ids performance;stale ### Proposal to improve performance As system prompt can be very long now, tokenize the system prompt can be slow. Using H20, tokenize 5000 tokens cost abou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
