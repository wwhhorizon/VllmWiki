# vllm-project/vllm#23926: [Bug]: Illegal memory access with 4 GPUS

| 字段 | 值 |
| --- | --- |
| Issue | [#23926](https://github.com/vllm-project/vllm/issues/23926) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Illegal memory access with 4 GPUS

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi I am trying to run vLLM on runpod with 4 gpus but I get his error that there was an illegal memory access. I am not sure if it is an issue in vLLM or the Runpod servers. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: s. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ns. correctness ci_build;distributed_parallel;frontend_api;model_support;quantization cuda;fp8;kernel build_error;crash;mismatch dtype #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;model_support;quantization cuda;fp8;kernel build_error;crash;mismatch dtype #23942 [CI] Add `aiter` to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: zation cuda;fp8;kernel build_error;crash;mismatch dtype #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: rontend_api;model_support;quantization cuda;fp8;kernel build_error;crash;mismatch dtype #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23934: Should have ROCm label: NO (0 matches) #23926: Should have ROCm label: NO (0 matches) #23925: Should have ROCm label: NO (0 matches) #23923: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
