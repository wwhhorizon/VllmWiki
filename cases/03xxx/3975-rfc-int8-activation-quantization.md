# vllm-project/vllm#3975: [RFC]: Int8 Activation Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#3975](https://github.com/vllm-project/vllm/issues/3975) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;gemm_linear;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;gemm;kernel;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Int8 Activation Quantization

### Issue 正文摘录

# Summary * We (engineering at @neuralmagic) are working on support for int8 quantized activations. * This RFC is proposing an _incremental_ approach to quantization, where the initial support for quantization will make _minimal_ and _local_ changes to the PyTorch model definitions. We propose swapping out Linear and Attention modules with their quantized counterparts without modifying the graphs around them. The upside to this will be quicker support for quantized models. The downside is that we will be quantizing the activations on the fly prior to computation. * To reduce the additional data movement from quantizing the activations on the fly, the activations will need to remain quantized throughout the graph, requiring more extensive and nonlocal modifications to the model definitions. We will be working on abstractions for the quantized model definitions to make adding support for new models as easy as possible. * Activation quantization will introduce additional elementwise operations to the model. To reduce the additional data movement of the activations from these operations, operator fusion will be needed. Rather than manually writing fused kernels for these, this RFC pro...

## 现有链接修复摘要

#5560 [Kernel] Adding bias epilogue support for `cutlass_scaled_mm`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: writing fused kernels for these, this RFC proposes committing to a torch.compile-based solution, to be explored in a future RFC. # Motivation and Scope The high-level goal of this RFC is to speed up Prefill by increasin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [RFC]: Int8 Activation Quantization RFC # Summary * We (engineering at @neuralmagic) are working on support for int8 quantized activations. * This RFC is proposing an _incremental_ approach to quantization, where the in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: a zero point. There are several cases to consider, with performance and accuracy tradeoffs in each case. * **Static vs dynamic quantization.** The scales and zero points may be known ahead of time, or may instead be det...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: # Motivation and Scope The high-level goal of this RFC is to speed up Prefill by increasing the rate of computation by using int8 tensor cores. We don't anticipate improving decode performance except for very large batc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pe;env_dependency;shape #5560 [Kernel] Adding bias epilogue support for `cutlass_scaled_mm` Summary

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5560](https://github.com/vllm-project/vllm/pull/5560) | mentioned | 0.6 | [Kernel] Adding bias epilogue support for `cutlass_scaled_mm` | ogue infrastructure from #5391. This is a part of the AQ kernel push (#3975) we're working on at Neural Magic. In future PRs, we will add support for asymmetric activation quantiz… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
