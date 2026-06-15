# vllm-project/vllm#28566: [Usage]: pd disagg scenario , I discover in the decoder , also has the prefill operation, is it normal ?

| 字段 | 值 |
| --- | --- |
| Issue | [#28566](https://github.com/vllm-project/vllm/issues/28566) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: pd disagg scenario , I discover in the decoder , also has the prefill operation, is it normal ?

### Issue 正文摘录

### Your current environment when num_computed_tokens is less than num_prompt_tokens, it will enter prefill operation and i found, num_computed_tokens is possible less than num_prompt_tokens, because num_prompt_tokens is len(block_ids) * self.block_size, event num_prompt_tokens is just equal to num_prompt_tokens, it do num_computed_tokens -= 1, why ? this cause num_computed_tokens is never equal to num_prompt_tokens ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: pd disagg scenario , I discover in the decoder , also has the prefill operation, is it normal ? usage;stale ### Your current environment when num_computed_tokens is less than num_prompt_tokens, it will enter pr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s possible less than num_prompt_tokens, because num_prompt_tokens is len(block_ids) * self.block_size, event num_prompt_tokens is just equal to num_prompt_tokens, it do num_computed_tokens -= 1, why ? this cause num_com...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
