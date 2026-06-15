# vllm-project/vllm#432: ~50% GPU utilization of openai API server

| 字段 | 值 |
| --- | --- |
| Issue | [#432](https://github.com/vllm-project/vllm/issues/432) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ~50% GPU utilization of openai API server

### Issue 正文摘录

I run an openai API server with a LLaMA-based model and 128 parallel requests, but only about 50% GPU utilization (nvidia-smi). Is it normal? Or because of some overhead, such as tokenizer?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: % GPU utilization of openai API server I run an openai API server with a LLaMA-based model and 128 parallel requests, but only about 50% GPU utilization (nvidia-smi). Is it normal? Or because of some overhead, such as t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el and 128 parallel requests, but only about 50% GPU utilization (nvidia-smi). Is it normal? Or because of some overhead, such as tokenizer?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ver I run an openai API server with a LLaMA-based model and 128 parallel requests, but only about 50% GPU utilization (nvidia-smi). Is it normal? Or because of some overhead, such as tokenizer?

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
