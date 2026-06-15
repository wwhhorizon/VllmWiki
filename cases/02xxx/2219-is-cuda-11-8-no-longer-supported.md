# vllm-project/vllm#2219: Is CUDA 11.8 no longer supported？

| 字段 | 值 |
| --- | --- |
| Issue | [#2219](https://github.com/vllm-project/vllm/issues/2219) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Is CUDA 11.8 no longer supported？

### Issue 正文摘录

``` The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1). Please make sure to use the same CUDA versions. [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. ERROR: Failed building wheel for vllm Failed to build vllm ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Is CUDA 11.8 no longer supported？ ``` The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1). Please make sure to use the same CUDA versions. [end of output] note: This error ori...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Is CUDA 11.8 no longer supported？ ``` The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1). Please make sure to use the same CUDA versions. [end of output] not
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: CUDA 11.8 no longer supported？ ``` The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1). Please make sure to use the same CUDA versions. [end of output] note: This error origin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
