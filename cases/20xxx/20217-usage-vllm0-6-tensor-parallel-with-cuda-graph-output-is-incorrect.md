# vllm-project/vllm#20217: [Usage]: vllm0.6 tensor parallel with cuda graph output is incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#20217](https://github.com/vllm-project/vllm/issues/20217) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm0.6 tensor parallel with cuda graph output is incorrect

### Issue 正文摘录

### Your current environment Due to project requirements, I'm currently still using vLLM version 0.6.3. I noticed that when using CUDA Graph, the output is correct with TP=1, but becomes garbled with TP=2. Has anyone encountered this issue? Are there any related issues that have addressed and resolved it? Thank you very much! ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: environment Due to project requirements, I'm currently still using vLLM version 0.6.3. I noticed that when using CUDA Graph, the output is correct with TP=1, but becomes garbled with TP=2. Has anyone encountered this is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: vllm0.6 tensor parallel with cuda graph output is incorrect usage ### Your current environment Due to project requirements, I'm currently still using vLLM version 0.6.3. I noticed that when using CUDA Graph, th...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tly asked questions. correctness distributed_parallel;model_support cuda mismatch Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. correctness distributed_parallel;model_support cuda mismatch Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
