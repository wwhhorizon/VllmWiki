# vllm-project/vllm#33026: [Feature]: Support fused silu_mul and block-wise quantization Triton kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#33026](https://github.com/vllm-project/vllm/issues/33026) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;kernel;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support fused silu_mul and block-wise quantization Triton kernel

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Triton kernel for Fused SiluMul+Groupwise FP8-Quantization. This is a sub-task of the quantization fusion roadmap mentioned in [#27847.](https://github.com/vllm-project/vllm/issues/27847) The goal is to provide a high-performance alternative to the existing CUDA implementation and evaluate its performance against torch.compile (Inductor). **Action Items** - [x] Step 1: Read the Existing CUDA Implementation and Related Code [by @Mon](https://github.com/vllm-project/vllm/pull/32996) - [x] Step 2: Implement the code - [x] Step 3: Write unit tests - [x] Step 4: Conduct testing and benchmarking (Torch Inductor vs Triton Kernel) - [ ] Step 5: Submit a pull request ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: existing CUDA implementation and evaluate its performance against torch.compile (Inductor). **Action Items** - [x] Step 1: Read the Existing CUDA Implementation and Related Code [by @Mon](https://github.com/vllm-project...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Support fused silu_mul and block-wise quantization Triton kernel feature request;stale ### 🚀 The feature, motivation and pitch Triton kernel for Fused SiluMul+Groupwise FP8-Quantization. This is a sub-task of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e a high-performance alternative to the existing CUDA implementation and evaluate its performance against torch.compile (Inductor). **Action Items** - [x] Step 1: Read the Existing CUDA Implementation and Related Code [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ) The goal is to provide a high-performance alternative to the existing CUDA implementation and evaluate its performance against torch.compile (Inductor). **Action Items** - [x] Step 1: Read the Existing CUDA Implementa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Feature]: Support fused silu_mul and block-wise quantization Triton kernel feature request;stale ### 🚀 The feature, motivation and pitch Triton kernel for Fused SiluMul+Groupwise FP8-Quantization. This is a sub-task of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
