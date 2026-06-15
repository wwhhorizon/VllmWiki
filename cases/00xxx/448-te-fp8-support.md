# vllm-project/vllm#448: TE FP8 support?

| 字段 | 值 |
| --- | --- |
| Issue | [#448](https://github.com/vllm-project/vllm/issues/448) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TE FP8 support?

### Issue 正文摘录

Hi! Is adding FP8 transformer engine (H100) speedup to inference planned? If not, could you please give me an outline of what needs to be done in order for me to work on that? Thank you!

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: TE FP8 support? feature request;unstale Hi! Is adding FP8 transformer engine (H100) speedup to inference planned? If not, could you please give me an outline of what needs to be done in order for me to work on that? Tha...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: TE FP8 support? feature request;unstale Hi! Is adding FP8 transformer engine (H100) speedup to inference planned? If not, could you please give me an outline of what needs to be done in order for me to work on that? Tha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 8 support? feature request;unstale Hi! Is adding FP8 transformer engine (H100) speedup to inference planned? If not, could you please give me an outline of what needs to be done in order for me to work on that? Thank yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
