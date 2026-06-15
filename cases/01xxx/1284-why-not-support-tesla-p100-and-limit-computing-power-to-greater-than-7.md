# vllm-project/vllm#1284: Why not support Tesla P100 and limit computing power to greater than 7?

| 字段 | 值 |
| --- | --- |
| Issue | [#1284](https://github.com/vllm-project/vllm/issues/1284) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why not support Tesla P100 and limit computing power to greater than 7?

### Issue 正文摘录

Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla P100-PCIE-16GB GPU has compute capability 6.0. RuntimeError: GPUs with compute capability below 7.0 are not supported.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Why not support Tesla P100 and limit computing power to greater than 7? Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla P100-PCIE-16GB GPU has compute capability 6.0. RuntimeError:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ported on GPUs with compute capability of at least 8.0. Your Tesla P100-PCIE-16GB GPU has compute capability 6.0. RuntimeError: GPUs with compute capability below 7.0 are not supported.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: power to greater than 7? Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla P100-PCIE-16GB GPU has compute capability 6.0. RuntimeError: GPUs with compute capability below 7.0 are not...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
