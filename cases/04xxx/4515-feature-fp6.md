# vllm-project/vllm#4515: [Feature]: FP6

| 字段 | 值 |
| --- | --- |
| Issue | [#4515](https://github.com/vllm-project/vllm/issues/4515) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: FP6

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Fp6 allows for models such llama 70b to fit in a single a100 GPU. Also 6bit is often the sweet spot between performance and speed. This was a paper from deep speed and is integrated into deepspeed-mii. But they also have the code and kernels seperately https://github.com/usyd-fsalab/fp6_llm ### Alternatives _No response_ ### Additional context _No response_

## 现有链接修复摘要

#8751 [Kernel][Quantization] Custom Floating-Point Runtime Quantization

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: re request;stale ### 🚀 The feature, motivation and pitch Fp6 allows for models such llama 70b to fit in a single a100 GPU. Also 6bit is often the sweet spot between performance and speed. This was a paper from deep spee...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: FP6 feature request;stale ### 🚀 The feature, motivation and pitch Fp6 allows for models such llama 70b to fit in a single a100 GPU. Also 6bit is often the sweet spot between performance and speed. This was a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: al context _No response_ performance frontend_api kernel #8751 [Kernel][Quantization] Custom Floating-Point Runtime Quantization 🚀 The feature, motivation and pitch
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ation and pitch Fp6 allows for models such llama 70b to fit in a single a100 GPU. Also 6bit is often the sweet spot between performance and speed. This was a paper from deep speed and is integrated into deepspeed-mii. B...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8751](https://github.com/vllm-project/vllm/pull/8751) | closes_keyword | 0.95 | [Kernel][Quantization] Custom Floating-Point Runtime Quantization | FIX #4515 ## Usage ```sh vllm serve NousResearch/Meta-Llama-3.1-8B-Instruct -q fp6_weights ``` # TODO - [ ] Investigate issues with Qwen models - [ ] Implement Channel |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
