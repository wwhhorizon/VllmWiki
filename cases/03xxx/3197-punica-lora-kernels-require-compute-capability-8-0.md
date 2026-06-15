# vllm-project/vllm#3197: punica LoRA kernels require compute capability >= 8.0

| 字段 | 值 |
| --- | --- |
| Issue | [#3197](https://github.com/vllm-project/vllm/issues/3197) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> punica LoRA kernels require compute capability >= 8.0

### Issue 正文摘录

I'm benchmarking the multiple lora feature on V100, compute capacity is SM 7.5. The code fails to run with this error. Is multiple lora supported on sm75 GPUs like V100?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: punica LoRA kernels require compute capability >= 8.0 I'm benchmarking the multiple lora feature on V100, compute capacity is SM 7.5. The code fails to run with this error. Is multiple lora supported on sm75 GPUs like V...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y >= 8.0 I'm benchmarking the multiple lora feature on V100, compute capacity is SM 7.5. The code fails to run with this error. Is multiple lora supported on sm75 GPUs like V100? development kernel I'm benchmarking the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: punica LoRA kernels require compute capability >= 8.0 I'm benchmarking the multiple lora feature on V100, compute capacity is SM 7.5. The code fails to run with this error. Is multiple lora supported on sm75 GPUs like V...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
