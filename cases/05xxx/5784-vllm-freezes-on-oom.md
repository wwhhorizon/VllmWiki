# vllm-project/vllm#5784: vLLM freezes on OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#5784](https://github.com/vllm-project/vllm/issues/5784) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM freezes on OOM

### Issue 正文摘录

### Anything you want to discuss about vllm. When the model crashes due to OOM, it is no longer able to accept new requests (it is not restored) and at the same time, 1 request is constantly running in monitoring. vLLM v0.4.3 Are there ways to automatically restore health and display information on charts in prometheus?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ezes on OOM stale ### Anything you want to discuss about vllm. When the model crashes due to OOM, it is no longer able to accept new requests (it is not restored) and at the same time, 1 request is constantly running in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: vLLM freezes on OOM stale ### Anything you want to discuss about vllm. When the model crashes due to OOM, it is no longer able to accept new requests (it is not restored) and at the same time, 1 request is constantly ru...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: vLLM freezes on OOM stale ### Anything you want to discuss about vllm. When the model crashes due to OOM, it is no longer able to accept new requests (it is not restored) and at the same time, 1 request is constantly ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
