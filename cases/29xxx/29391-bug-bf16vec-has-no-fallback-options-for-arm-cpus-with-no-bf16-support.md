# vllm-project/vllm#29391: [Bug]: BF16Vec has no fallback options for Arm CPUs with no BF16 support

| 字段 | 值 |
| --- | --- |
| Issue | [#29391](https://github.com/vllm-project/vllm/issues/29391) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: BF16Vec has no fallback options for Arm CPUs with no BF16 support

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug BF16Vec for Arm CPUs is defined here: https://github.com/vllm-project/vllm/blob/main/csrc/cpu/cpu_types_arm.hpp#L166 However it's guarded by the `ARM_BF16_SUPPORT` which means that everytime you want to initialize a `BF16Vec` you need an ifdef to handle Arm CPUs that doesn't support BF16, otherwise you'll get: `error: no type named 'BF16Vec16' in namespace 'vec_op'` For example see #28681 which fixes the issue above by guarding `BF16Vec` with `#ifdef ARM_BF16_SUPPORT`. Also see [this](https://github.com/vllm-project/vllm/pull/29193/files#:~:text=//%20These%20do,FP16Vec*%20for%20consistency.) where we couldn't use `BF16Vec` class to due to this limitation. Definitions for `BF16Vec` should not be guarded by `ARM_BF16_SUPPORT`, we should have reference/fallback implementations for any Arm CPUs that don't have BF16 support. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: BF16Vec has no fallback options for Arm CPUs with no BF16 support bug ### Your current environment ### 🐛 Describe the bug BF16Vec for Arm CPUs is defined here: https://github.com/vllm-project/vllm/blob/main/csrc/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: BF16Vec has no fallback options for Arm CPUs with no BF16 support bug ### Your current environment ### 🐛 Describe the bug BF16Vec for Arm CPUs is defined here: https://github.com/vllm-project/vllm/blob/main/csrc/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
