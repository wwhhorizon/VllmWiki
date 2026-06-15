# vllm-project/vllm#27829: [Performance][torch.compile]: FlashInfer Attention + quant fusion performance issue with TP=4

| 字段 | 值 |
| --- | --- |
| Issue | [#27829](https://github.com/vllm-project/vllm/issues/27829) |
| 状态 | open |
| 标签 | performance;torch.compile;unstale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance][torch.compile]: FlashInfer Attention + quant fusion performance issue with TP=4

### Issue 正文摘录

As seen in #27080, attention+quant fusion on 4xB200 with the FlashInfer attn backend performs worse than unfused code. This should be resolved so that we can turn on this fusion by default. cc @nvpohanh @pavanimajety @zou3519 for visibility

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Performance][torch.compile]: FlashInfer Attention + quant fusion performance issue with TP=4 performance;torch.compile;unstale As seen in #27080, attention+quant fusion on 4xB200 with the FlashInfer attn backend perfor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Performance][torch.compile]: FlashInfer Attention + quant fusion performance issue with TP=4 performance;torch.compile;unstale As seen in #27080, attention+quant fusion on 4xB200 with the FlashInfer attn backend perfor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Performance][torch.compile]: FlashInfer Attention + quant fusion performance issue with TP=4 performance;torch.compile;unstale As seen in #27080, attention+quant fusion on 4xB200 with the FlashInfer attn backend perfor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nce;torch.compile;unstale As seen in #27080, attention+quant fusion on 4xB200 with the FlashInfer attn backend performs worse than unfused code. This should be resolved so that we can turn on this fusion by default. cc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n + quant fusion performance issue with TP=4 performance;torch.compile;unstale As seen in #27080, attention+quant fusion on 4xB200 with the FlashInfer attn backend performs worse than unfused code. This should be resolv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
