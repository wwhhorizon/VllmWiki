# vllm-project/vllm#5228: [Feature]: Custom attention masks

| 字段 | 值 |
| --- | --- |
| Issue | [#5228](https://github.com/vllm-project/vllm/issues/5228) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Custom attention masks

### Issue 正文摘录

Inspired from [this paper](https://arxiv.org/abs/2405.14862), we're exploring ways to bootstrap a bidirectional-context LLM from a decoder-only Causal LLM (e.g. llama-3). This is very easy to do in huggingface transformers by passing a [custom attention mask](https://github.com/huggingface/transformers/pull/27539/commits). Looking for guidance on how to make this happen in vLLM? TLDR; 1. Compute bidirectional hidden states from prompt. 2. Use causal attention for decoding. Help appreciated!

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Custom attention masks feature request;stale Inspired from [this paper](https://arxiv.org/abs/2405.14862), we're exploring ways to bootstrap a bidirectional-context LLM from a decoder-only Causal LLM (e.g. ll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: otstrap a bidirectional-context LLM from a decoder-only Causal LLM (e.g. llama-3). This is very easy to do in huggingface transformers by passing a [custom attention mask](https://github.com/huggingface/transformers/pul...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: dden states from prompt. 2. Use causal attention for decoding. Help appreciated!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
