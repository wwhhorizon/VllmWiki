# vllm-project/vllm#1089: [v0.2.0] Release Tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#1089](https://github.com/vllm-project/vllm/issues/1089) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [v0.2.0] Release Tracker

### Issue 正文摘录

## Major changes * Up to 60% performance improvement by optimizing de-tokenization and sampler * Initial support for AWQ (performance not optimized) * Support for RoPE scaling and LongChat * Support for Mistral-7B ## PRs to be merged before the release - [x] Vectorized sampler: #1048, #820 - [x] LongChat: #555 - [x] `TORCH_CUDA_ARCH_LIST` build option: #1074 - [x] Support for Mistral-7B: #1196 - [x] #1198 - ~~[ ] FP32 RoPE kernel: #1061~~ (deferred to the next PR)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [x] Vectorized sampler: #1048, #820 - [x] LongChat: #555 - [x] `TORCH_CUDA_ARCH_LIST` build option: #1074 - [x] Support for Mistral-7B: #1196 - [x] #1198 - ~~[ ] FP32 RoPE kernel: #1061~~ (deferred to the next PR)
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sampler: #1048, #820 - [x] LongChat: #555 - [x] `TORCH_CUDA_ARCH_LIST` build option: #1074 - [x] Support for Mistral-7B: #1196 - [x] #1198 - ~~[ ] FP32 RoPE kernel: #1061~~ (deferred to the next PR)

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
