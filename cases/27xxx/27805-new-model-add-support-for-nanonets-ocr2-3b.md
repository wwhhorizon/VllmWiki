# vllm-project/vllm#27805: [New Model]: Add support for Nanonets-OCR2-3B

| 字段 | 值 |
| --- | --- |
| Issue | [#27805](https://github.com/vllm-project/vllm/issues/27805) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Add support for Nanonets-OCR2-3B

### Issue 正文摘录

### The model to consider. Model:nanonets/Nanonets-OCR2-3B link: https://huggingface.co/nanonets/Nanonets-OCR2-3B ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Add support for Nanonets-OCR2-3B new-model;stale ### The model to consider. Model:nanonets/Nanonets-OCR2-3B link: https://huggingface.co/nanonets/Nanonets-OCR2-3B ### The closest model vllm already supports...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -model;stale ### The model to consider. Model:nanonets/Nanonets-OCR2-3B link: https://huggingface.co/nanonets/Nanonets-OCR2-3B ### The closest model vllm already supports. _No response_ ### What's your difficulty of sup...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Add support for Nanonets-OCR2-3B new-model;stale ### The model to consider. Model:nanonets/Nanonets-OCR2-3B link: https://huggingface.co/nanonets/Nanonets-OCR2-3B ### The closest model vllm already supports...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
