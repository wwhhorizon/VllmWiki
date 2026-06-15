# vllm-project/vllm#3040: Support of AMD consumer GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#3040](https://github.com/vllm-project/vllm/issues/3040) |
| 状态 | closed |
| 标签 | rocm;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;hardware_porting |
| 子分类 | runtime_err |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Support of AMD consumer GPUs

### Issue 正文摘录

Is there a technical reason, why only AMD MI200 GPUs or newer are supported? I get the error `RuntimeError: FlashAttention only supports AMD MI200 GPUs or newer.` when I try to run vllm on my RX 7900 XTX.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ly AMD MI200 GPUs or newer are supported? I get the error `RuntimeError: FlashAttention only supports AMD MI200 GPUs or newer.` when I try to run vllm on my RX 7900 XTX. development attention_kv_cache;hardware_porting a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Support of AMD consumer GPUs rocm;stale Is there a technical reason, why only AMD MI200 GPUs or newer are supported? I get the error `RuntimeError: FlashAttention only supports AMD MI200 GPUs or newer.` when I try to ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Support of AMD consumer GPUs rocm;stale Is there a technical reason, why only AMD MI200 GPUs or newer are supported? I get the error `RuntimeError: FlashAttention only supports AMD MI200 GPUs or newer.` when I try to ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
