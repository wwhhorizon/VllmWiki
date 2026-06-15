# vllm-project/vllm#27847: [Feature]: Support norm+quant & silu+quant fusion for block (group) quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#27847](https://github.com/vllm-project/vllm/issues/27847) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;torch.compile |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;frontend_api;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | activation;cuda;kernel;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support norm+quant & silu+quant fusion for block (group) quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, we use the CUDA quant kernel for group quant due to performance issues of the H100 kernel. However, that means that it cannot be automatically fused with preceeding RMSNorm and SiluMul. We should add support for group quant to RMSNorm+quant and SiluMul+quant fusion passes, as well as custom fused CUDA kernels to work around the issue for now and have an alternative when Inductor-generated code is slower. - [x] RMS + block quant fusion - [ ] SiluMul + block quant fusion ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#32996 Feature/silu block quant fusion v1

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: (group) quantization help wanted;good first issue;feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, we use the CUDA quant kernel for group quant due to performance issues of the H100 kerne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: h.compile ### 🚀 The feature, motivation and pitch Currently, we use the CUDA quant kernel for group quant due to performance issues of the H100 kernel. However, that means that it cannot be automatically fused with prec...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Feature]: Support norm+quant & silu+quant fusion for block (group) quantization help wanted;good first issue;feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, we use the CUDA quant kernel...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Support norm+quant & silu+quant fusion for block (group) quantization help wanted;good first issue;feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, we use the CUDA quant kernel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sion for block (group) quantization help wanted;good first issue;feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, we use the CUDA quant kernel for group quant due to performance issues of...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32996](https://github.com/vllm-project/vllm/pull/32996) | mentioned | 0.6 | Feature/silu block quant fusion v1 | nd pattern matching for Fused SiluMul+Groupwise FP8-Quantization. For #27847 #### Test Result The experiments are done on NVIDIA GeForce RTX 4070 and CUDA Version: 13.0. Test fuse… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
