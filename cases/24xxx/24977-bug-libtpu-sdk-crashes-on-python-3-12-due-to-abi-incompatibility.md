# vllm-project/vllm#24977: [Bug]: libtpu.sdk crashes on Python 3.12 due to ABI incompatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#24977](https://github.com/vllm-project/vllm/issues/24977) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: libtpu.sdk crashes on Python 3.12 due to ABI incompatibility

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM's current TPU requirements file for building the tpu container has a critical compatibility issue with Python 3.12 due to ABI incompatibility in the libtpu dependency. ## Environment - **Python Version**: 3.12.x - **vLLM Version**: [current version] - **libtpu Version**: 0.0.18 - **Platform**: Linux x86_64 - **Hardware**: TPU v5lite-pod ## Root Cause Analysis The issue stems from incorrect wheel packaging in Google's libtpu distribution: **Wheel filename claims universal compatibility** **But contains Python 3.11-specific binary:** sdk.cpython-311-x86_64-linux-gnu.so ## Reproduction Steps ```python # This crashes immediately on Python 3.12: python3.12 -c "import libtpu.sdk" # Segmentation fault (core dumped) ``` the earliest version of libtpu with direct support for python 3.12 is libtpu-0.0.20 but this would require bumping jax to 0.7.0 as well ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ent ### 🐛 Describe the bug vLLM's current TPU requirements file for building the tpu container has a critical compatibility issue with Python 3.12 due to ABI incompatibility in the libtpu dependency. ## Environment - **...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ell ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: libtpu.sdk crashes on Python 3.12 due to ABI incompatibility bug;stale ### Your current environment ### 🐛 Describe the bug vLLM's current TPU requirements file for building the tpu container has a critical compat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;mismatch;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: its;speculative_decoding cuda;operator;sampling;triton build_error;crash;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
