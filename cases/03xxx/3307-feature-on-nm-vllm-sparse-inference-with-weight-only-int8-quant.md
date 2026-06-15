# vllm-project/vllm#3307: [feature on nm-vllm] Sparse Inference with weight only int8 quant

| 字段 | 值 |
| --- | --- |
| Issue | [#3307](https://github.com/vllm-project/vllm/issues/3307) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [feature on nm-vllm] Sparse Inference with weight only int8 quant

### Issue 正文摘录

Can sparsity and quantization be used simultaneously to further improve inference speed? Do you have any plans in this regard? Looking forward to your reply @robertgshaw2-neuralmagic

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [feature on nm-vllm] Sparse Inference with weight only int8 quant stale Can sparsity and quantization be used simultaneously to further improve inference speed? Do you have any plans in this regard? Looking forward to y...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [feature on nm-vllm] Sparse Inference with weight only int8 quant stale Can sparsity and quantization be used simultaneously to further improve inference speed? Do you have any plans in this regard? Looking forward to y...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
