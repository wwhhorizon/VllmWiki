# vllm-project/vllm#20711: [Feature]: Use `QuantFp8` `CustomOp`-abstraction for MoE layers

| 字段 | 值 |
| --- | --- |
| Issue | [#20711](https://github.com/vllm-project/vllm/issues/20711) |
| 状态 | closed |
| 标签 | good first issue;feature request;torch.compile;keep-open |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;moe;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Use `QuantFp8` `CustomOp`-abstraction for MoE layers

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #19830 added `QuantFp8`, which uses the `CustomOp` abstraction to implement fp8 quantization in both CUDA and torch, allowing Inductor to achieve superior performance over the CUDA ops (which are unoptimized and also do not fuse by default). However, the class has to be instantiated during init, and MoE uses are currently in util free functions many levels deep. Those need to be mildly rearchitected to take advantage of the new abstraction. The use to be rearchitected is here: https://github.com/vllm-project/vllm/blob/c7a00e6e6716f45db09e39cb21a8f91f741f10b9/vllm/model_executor/layers/fused_moe/utils.py#L37-L40 The free functions should be converted to class instances with separate init and forward steps. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#19830 [Perf][fp8] Use CustomOp abstraction for fp8 quant for better perf | #20879 implement issue #20711 | #23463 [#20711] Use QuantFp8 CustomOp-abstraction for MoE layers

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tomOp`-abstraction for MoE layers good first issue;feature request;torch.compile;keep-open ### 🚀 The feature, motivation and pitch #19830 added `QuantFp8`, which uses the `CustomOp` abstraction to implement fp8 quantiza...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Use `QuantFp8` `CustomOp`-abstraction for MoE layers good first issue;feature request;torch.compile;keep-open ### 🚀 The feature, motivation and pitch #19830 added `QuantFp8`, which uses the `CustomOp` abstrac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ch uses the `CustomOp` abstraction to implement fp8 quantization in both CUDA and torch, allowing Inductor to achieve superior performance over the CUDA ops (which are unoptimized and also do not fuse by default). Howev...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/c7a00e6e6716f45db09e39cb21a8f91f741f10b9/vllm/model_executor/layers/fused_moe/utils.py#L37-L40 The free functions should be converted to class instances with separate init and forward steps. #...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Use `QuantFp8` `CustomOp`-abstraction for MoE layers good first issue;feature request;torch.compile;keep-open ### 🚀 The feature, motivation and pitch #19830 added `QuantFp8`, which uses the `CustomOp` abstrac...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#19830](https://github.com/vllm-project/vllm/pull/19830) | mentioned | 0.45 | [Perf][fp8] Use CustomOp abstraction for fp8 quant for better perf | `-abstraction for moe layers ### 🚀 the feature, motivation and pitch #19830 added `quantfp8`, which uses the `customop` abstraction to implement fp8 quantization in both cuda and… |
| [#20879](https://github.com/vllm-project/vllm/pull/20879) | mentioned | 0.6 | implement issue #20711 | ions. Specifically, this change addresses the TODO outlined in issue #20711 by replacing the generic `ops.scaled_fp8_quant` function previously used in the MoE layer with a dedica… |
| [#23463](https://github.com/vllm-project/vllm/pull/23463) | mentioned | 0.6 | [#20711] Use QuantFp8 CustomOp-abstraction for MoE layers | [#20711] Use QuantFp8 CustomOp-abstraction for MoE layers ## Purpose Refactor MoE FP8 activation quantization to use |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
