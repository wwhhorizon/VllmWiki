# vllm-project/vllm#29581: [Bug]: Batch Invariant didn't work with Qwen3-30B-A3B-Instruct-2507-AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#29581](https://github.com/vllm-project/vllm/issues/29581) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Batch Invariant didn't work with Qwen3-30B-A3B-Instruct-2507-AWQ

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To reproduce Use the vllm docker image for 0.11.2 to serve model `ELVISIO/Qwen3-30B-A3B-Instruct-2507-AWQ` Make API calls to the server to test for determinism. Even with a specified seed or temperature of 0, the output is not consistent ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#38670 [Bugfix] Fix AWQ models batch invariance issues

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: 2507-AWQ bug ### Your current environment ### 🐛 Describe the bug To reproduce Use the vllm docker image for 0.11.2 to serve model `ELVISIO/Qwen3-30B-A3B-Instruct-2507-AWQ` Make API calls to the server to test for determ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: urrent environment ### 🐛 Describe the bug To reproduce Use the vllm docker image for 0.11.2 to serve model `ELVISIO/Qwen3-30B-A3B-Instruct-2507-AWQ` Make API calls to the server to test for determinism. Even with a spec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 3B-Instruct-2507-AWQ` Make API calls to the server to test for determinism. Even with a specified seed or temperature of 0, the output is not consistent ### Before submitting a new issue... - [x] Make sure you already s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Batch Invariant didn't work with Qwen3-30B-A3B-Instruct-2507-AWQ bug ### Your current environment ### 🐛 Describe the bug To reproduce Use the vllm docker image for 0.11.2 to serve model `ELVISIO/Qwen3-30B-A3B-Ins...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: LVISIO/Qwen3-30B-A3B-Instruct-2507-AWQ` Make API calls to the server to test for determinism. Even with a specified seed or temperature of 0, the output is not consistent ### Before submitting a new issue... - [x] Make...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38670](https://github.com/vllm-project/vllm/pull/38670) | closes_keyword | 0.95 | [Bugfix] Fix AWQ models batch invariance issues | Fixes #29581 AWQ models currently fail batch invariance because vLLM auto-converts AWQ to the Marlin CUDA kernel, which bypasses the batch-invariant Triton matmul override. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
