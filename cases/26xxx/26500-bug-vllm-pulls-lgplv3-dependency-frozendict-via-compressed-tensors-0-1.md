# vllm-project/vllm#26500: [Bug]: vLLM pulls LGPLv3 dependency (frozendict) via compressed-tensors 0.11.0, breaking license allowlists in downstreams (e.g., KServe)

| 字段 | 值 |
| --- | --- |
| Issue | [#26500](https://github.com/vllm-project/vllm/issues/26500) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM pulls LGPLv3 dependency (frozendict) via compressed-tensors 0.11.0, breaking license allowlists in downstreams (e.g., KServe)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Summary After upgrading to **vLLM 0.10.2**, the dependency chain now includes `compressed-tensors 0.11.0`, which introduces a new runtime dependency on `frozendict`. `frozendict` is licensed under **LGPLv3**, which breaks license allowlists for many downstreams (e.g., KServe, Apache-2.0-only environments). https://github.com/neuralmagic/compressed-tensors/issues/468 ### Details - **vLLM version**: 0.10.2 - **compressed-tensors version**: 0.11.0 - **New dependency**: `frozendict` (LGPLv3) The dependency was introduced in the following PR on compressed-tensors: > [Transform: Construct on GPU, cache on CPU #352](https://github.com/neuralmagic/compressed-tensors/pull/352) Downstream projects that enforce strict license allowlists (e.g., Apache-2.0) now fail during compliance checks. Example (from KServe CI): ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: vLLM pulls LGPLv3 dependency (frozendict) via compressed-tensors 0.11.0, breaking license allowlists in downstreams (e.g., KServe) bug ### Your current environment ### 🐛 Describe the bug ### Summary After upgradi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: I): ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
