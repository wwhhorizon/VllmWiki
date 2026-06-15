# vllm-project/vllm#27828: [Performance][torch.compile]: Inductor partition performance issues

| 字段 | 值 |
| --- | --- |
| Issue | [#27828](https://github.com/vllm-project/vllm/issues/27828) |
| 状态 | open |
| 标签 | performance |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance][torch.compile]: Inductor partition performance issues

### Issue 正文摘录

### Performance issues As seen in #27080, Inductor partition is not always faster than Dynamo partition or no partition. Those are two separate issues: - [x] On Blackwell, no partition is sometimes faster than Inductor partition (particularly TTFT with attention+quant fusion). This might just be attributable to the difference in performance between `FULL_AND_PIECEWISE` and `FULL_DECODE_ONLY` cudagraph modes. - [ ] On Hopper, Inductor partition seems to be slower than Dynamo partition, although we only have numbers for TP=4. We should try again with llama-8B TP=1. cc @zou3519 @BoyuanFeng

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ynamo partition or no partition. Those are two separate issues: - [x] On Blackwell, no partition is sometimes faster than Inductor partition (particularly TTFT with attention+quant fusion). This might just be attributab...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Performance][torch.compile]: Inductor partition performance issues performance ### Performance issues As seen in #27080, Inductor partition is not always faster than Dynamo partition or no partition. Those are two sepa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: metimes faster than Inductor partition (particularly TTFT with attention+quant fusion). This might just be attributable to the difference in performance between `FULL_AND_PIECEWISE` and `FULL_DECODE_ONLY` cudagraph mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tition, although we only have numbers for TP=4. We should try again with llama-8B TP=1. cc @zou3519 @BoyuanFeng
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: to the difference in performance between `FULL_AND_PIECEWISE` and `FULL_DECODE_ONLY` cudagraph modes. - [ ] On Hopper, Inductor partition seems to be slower than Dynamo partition, although we only have numbers for TP=4....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
