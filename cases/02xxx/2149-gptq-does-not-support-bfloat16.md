# vllm-project/vllm#2149: GPTQ does not support bfloat16

| 字段 | 值 |
| --- | --- |
| Issue | [#2149](https://github.com/vllm-project/vllm/issues/2149) |
| 状态 | closed |
| 标签 | help wanted;feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPTQ does not support bfloat16

### Issue 正文摘录

Currently, our GPTQ kernels only support the float16 precision.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: GPTQ does not support bfloat16 help wanted;feature request;stale Currently, our GPTQ kernels only support the float16 precision.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: GPTQ does not support bfloat16 help wanted;feature request;stale Currently, our GPTQ kernels only support the float16 precision.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ature request;stale Currently, our GPTQ kernels only support the float16 precision.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: re request;stale Currently, our GPTQ kernels only support the float16 precision.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
