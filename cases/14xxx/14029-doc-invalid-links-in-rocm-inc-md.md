# vllm-project/vllm#14029: [Doc]: Invalid Links in rocm.inc.md

| 字段 | 值 |
| --- | --- |
| Issue | [#14029](https://github.com/vllm-project/vllm/issues/14029) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Invalid Links in rocm.inc.md

### Issue 正文摘录

### 📚 The doc issue The links of flash-attention in getting_started/installation/gpu/rocm.inc.md has been invalid: flash attention for ROCm: https://github.com/ROCm/flash-attention/tree/ck_tile ROCm/flash-attention: https://github.com/ROCm/flash-attention/tree/ck_tile#amd-gpurocm-support The branch ck_tile has been deleted, those links need to be changed. And the tile is amd-rocm-support now. ### Suggest a potential alternative/fix [flash attention for ROCm](https://github.com/ROCm/flash-attention) [ROCm/flash-attention](https://github.com/ROCm/flash-attention#amd-rocm-support) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Doc]: Invalid Links in rocm.inc.md documentation ### 📚 The doc issue The links of flash-attention in getting_started/installation/gpu/rocm.inc.md has been invalid: flash attention for ROCm: https://github.com/ROCm/flas...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Doc]: Invalid Links in rocm.inc.md documentation ### 📚 The doc issue The links of flash-attention in getting_started/installation/gpu/rocm.inc.md has been invalid: flash attention for ROCm: https://github.com/ROCm/flas...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tion in getting_started/installation/gpu/rocm.inc.md has been invalid: flash attention for ROCm: https://github.com/ROCm/flash-attention/tree/ck_tile ROCm/flash-attention: https://github.com/ROCm/flash-attention/tree/ck...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
