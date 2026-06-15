# vllm-project/vllm#33333: [Bug]:  sm_120 -NvFp4 MoE backend 'FLASHINFER_CUTLASS' does not support the deployment configuration since kernel does not support current device.

| 字段 | 值 |
| --- | --- |
| Issue | [#33333](https://github.com/vllm-project/vllm/issues/33333) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  sm_120 -NvFp4 MoE backend 'FLASHINFER_CUTLASS' does not support the deployment configuration since kernel does not support current device.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I am running nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 on a machine with an NVIDIA RTX Pro 6000 Blackwell Max-Q. But I encountered the issue below: ``` ValueError: NvFp4 MoE backend 'FLASHINFER_CUTLASS' does not support the deployment configuration since kernel does not support current device. [rank0]:[W129 16:06:34.953918303 ProcessGroupNCCL.cpp:1524] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator()) (APISer ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#36453 fix: Add SM120 capability family check for FlashInfer NVFP4 MoE backends

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: sm_120 -NvFp4 MoE backend 'FLASHINFER_CUTLASS' does not support the deployment configuration since kernel does not support current device. bug ### Your current environment ### 🐛 Describe the bug Hello, I am runni...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: sm_120 -NvFp4 MoE backend 'FLASHINFER_CUTLASS' does not support the deployment configuration since kernel does not support current device. bug ### Your current environment ### 🐛 Describe the bug Hello, I am runni...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;k...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: sm_120 -NvFp4 MoE backend 'FLASHINFER_CUTLASS' does not support the deployment configuration since kernel does not support current device. bug ### Your current environment ### 🐛 Describe the bug Hello, I am runni...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -NvFp4 MoE backend 'FLASHINFER_CUTLASS' does not support the deployment configuration since kernel does not support current device. bug ### Your current environment ### 🐛 Describe the bug Hello, I am running nvidia/NVID...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36453](https://github.com/vllm-project/vllm/pull/36453) | closes_keyword | 0.95 | fix: Add SM120 capability family check for FlashInfer NVFP4 MoE backends | Closes #33416, #33333 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
