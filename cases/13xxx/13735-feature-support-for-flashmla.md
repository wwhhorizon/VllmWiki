# vllm-project/vllm#13735: [Feature]: Support for FlashMLA

| 字段 | 值 |
| --- | --- |
| Issue | [#13735](https://github.com/vllm-project/vllm/issues/13735) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support for FlashMLA

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://github.com/deepseek-ai/FlashMLA ``` Achieving up to 3000 GB/s in memory-bound configuration and 580 TFLOPS in computation-bound configuration on H800 SXM5, using CUDA 12.6. ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#13747 [Kernel] FlashMLA integration

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on and 580 TFLOPS in computation-bound configuration on H800 SXM5, using CUDA 12.6. ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you alread...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .com/deepseek-ai/FlashMLA ``` Achieving up to 3000 GB/s in memory-bound configuration and 580 TFLOPS in computation-bound configuration on H800 SXM5, using CUDA 12.6. ``` ### Alternatives _No response_ ### Additional co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support for FlashMLA feature request ### 🚀 The feature, motivation and pitch https://github.com/deepseek-ai/FlashMLA ``` Achieving up to 3000 GB/s in memory-bound configuration and 580 TFLOPS in computation-b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance frontend_api cuda #13747 [Kernel] FlashMLA integration 🚀 The feature, mot...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#13747](https://github.com/vllm-project/vllm/pull/13747) | closes_keyword | 0.95 | [Kernel] FlashMLA integration | Closes #13735 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
