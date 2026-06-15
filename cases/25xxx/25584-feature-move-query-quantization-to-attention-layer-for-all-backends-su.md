# vllm-project/vllm#25584: [Feature]: Move query quantization to attention layer for all backends supporting query quantization.

| 字段 | 值 |
| --- | --- |
| Issue | [#25584](https://github.com/vllm-project/vllm/issues/25584) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Move query quantization to attention layer for all backends supporting query quantization.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/pull/24914 moved the query quantization out of the FlashAttn backend into `attention/layer` such that it can be fused by torch compile AND included in the CUDA graph. #26534 moved it for Triton and FlashInfer. This should be done for all backends. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#26534 Move query quantization to attention layer for Flashinfer & Triton.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: shAttn backend into `attention/layer` such that it can be fused by torch compile AND included in the CUDA graph. #26534 moved it for Triton and FlashInfer. This should be done for all backends. ### Alternatives _No resp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Feature]: Move query quantization to attention layer for all backends supporting query quantization. help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch https://github.com/vllm-project/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on/layer` such that it can be fused by torch compile AND included in the CUDA graph. #26534 moved it for Triton and FlashInfer. This should be done for all backends. ### Alternatives _No response_ ### Additional context...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Move query quantization to attention layer for all backends supporting query quantization. help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch https://github.com/vllm-project/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ends supporting query quantization. help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/pull/24914 moved the query quantization out of the FlashAttn...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26534](https://github.com/vllm-project/vllm/pull/26534) | closes_keyword | 0.95 | Move query quantization to attention layer for Flashinfer & Triton. | resolves feature request [#25584](https://github.com/vllm-project/vllm/issues/25584) ### Test Plan Spin up server: Flashinfer: ``` VLLM_ATTENTION_BACKEND=FLASHINFER vllm serve m |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
