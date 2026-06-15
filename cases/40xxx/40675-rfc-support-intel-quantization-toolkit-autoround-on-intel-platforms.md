# vllm-project/vllm#40675: [RFC] Support Intel Quantization Toolkit AutoRound on Intel Platforms

| 字段 | 值 |
| --- | --- |
| Issue | [#40675](https://github.com/vllm-project/vllm/issues/40675) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | fp8;kernel;moe;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC] Support Intel Quantization Toolkit AutoRound on Intel Platforms

### Issue 正文摘录

## Summary Intel AutoRound is an advanced toolkit designed to support the quantization of LLMs on Intel platforms. This RFC proposes adopting this quantization toolkit for the supported AutoRound format on Intel platforms in vLLM. ## Motivation Integrating Intel AutoRound Toolkit natively into vLLM is motivated by two related needs: **1. An Advanced Toolkit specifically tailored for Intel AutoRound Quantization.** vLLM already supports generic quantization formats and vendor-owned quantization toolkits. For example, AMD QUARK provides the AMD ecosystem with a first-class vendor quantization toolkit to simplify and enhance the quantization in vLLM. Users deploying on Intel platforms require a comparable, seamless path for Intel's own quantization workflow, especially for checkpoints produced by Intel AutoRound. Intel AutoRound fills that exact role for Intel platforms, similar to how QUARK does for AMD. By providing unified computational kernels for quantized Linear and MoE layers, the AutoRound Toolkit establishes a seamless, end-to-end workflow from quantization to high-performance inference within vLLM. **2. Native Support for the AutoRound Format on Intel Platforms** While vLLM...

## 现有链接修复摘要

#39778 [Quantization][Autoround][Toolkit] Add W4A16 Support | #40601 [quant][autoround]Refactor INC quantization into package with INCScheme orchestrator

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nto vLLM is motivated by two related needs: **1. An Advanced Toolkit specifically tailored for Intel AutoRound Quantization.** vLLM already supports generic quantization formats and vendor-owned quantization toolkits. F...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [RFC] Support Intel Quantization Toolkit AutoRound on Intel Platforms RFC ## Summary Intel AutoRound is an advanced toolkit designed to support the quantization of LLMs on Intel platforms. This RFC proposes adopting thi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: proposes adopting this quantization toolkit for the supported AutoRound format on Intel platforms in vLLM. ## Motivation Integrating Intel AutoRound Toolkit natively into vLLM is motivated by two related needs: **1. An...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eight-Only Quantization (WOQ) inference support for AutoRound. ### Core Architecture Design: The API utilizes an object-oriented polymorphic design tailored for seamless weight initialization and highly efficient infere...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: (such as Compressed Tensors), Intel's native AutoRound format has unique layout and algorithmic characteristics designed to maximize performance on Intel hardware. Integrating this toolkit provides highly optimized kern...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39778](https://github.com/vllm-project/vllm/pull/39778) | mentioned | 0.45 | [Quantization][Autoround][Toolkit] Add W4A16 Support | m to support autoround w4a16 linear path by submitting the initial pr #39778. * add an official introduction of the autoround toolkit to vllm and update its [support matrix](https… |
| [#40601](https://github.com/vllm-project/vllm/pull/40601) | mentioned | 0.45 | [quant][autoround]Refactor INC quantization into package with INCScheme orchestrator | * phase 2: align with inc refactor track the upstream inc refactor in #40601 and adapt the autoround toolkit integration to align with the finalized modular package structure upon… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
