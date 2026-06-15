# vllm-project/vllm#24185: [Feature]: Extend QuantFP8 to support per-token-group quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#24185](https://github.com/vllm-project/vllm/issues/24185) |
| 状态 | closed |
| 标签 | good first issue;feature request;torch.compile |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Extend QuantFP8 to support per-token-group quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, group quantization is handled by a `per_token_group_quant_fp8` custom CUDA kernel (with a Triton kernel fallback). We should fold this functionality into `QuantFP8` to allow easier dispatching between CUDA, Triton, and torch implementations, automatic Inductor fusion, and easier custom op fusion. ### Alternatives _No response_ ### Additional context This is related and complementary to #20711. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#24342 [FP8] Extend per-token-group quantization support to QuantFP8 | #27927 [feature] [compile] use quantfp8 customOp-abstraction for MoE layers

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: port per-token-group quantization good first issue;feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, group quantization is handled by a `per_token_group_quant_fp8` custom CUDA kernel (with...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: n is handled by a `per_token_group_quant_fp8` custom CUDA kernel (with a Triton kernel fallback). We should fold this functionality into `QuantFP8` to allow easier dispatching between CUDA, Triton, and torch implementat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Extend QuantFP8 to support per-token-group quantization good first issue;feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, group quantization is handled by a `per_token_group_qu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y, group quantization is handled by a `per_token_group_quant_fp8` custom CUDA kernel (with a Triton kernel fallback). We should fold this functionality into `QuantFP8` to allow easier dispatching between CUDA, Triton, a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ntFP8 | #27927 [feature] [compile] use quantfp8 customOp-abstraction for MoE layers 🚀 The feature, motivation and pitch

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24342](https://github.com/vllm-project/vllm/pull/24342) | mentioned | 0.6 | [FP8] Extend per-token-group quantization support to QuantFP8 | a torch implementation of the QuantFP8 group quantization. Addresses #24185 ## Changes - Add `is_per_tensor()`, `is_per_token()`, `is_per_group()` helper methods to `GroupShape` -… |
| [#27927](https://github.com/vllm-project/vllm/pull/27927) | mentioned | 0.6 | [feature] [compile] use quantfp8 customOp-abstraction for MoE layers | (https://github.com/vllm-project/vllm/issues/20711#issue-3217229635) [#24185](https://github.com/vllm-project/vllm/issues/24185) - doesn't properly refactor the parent functions i… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
