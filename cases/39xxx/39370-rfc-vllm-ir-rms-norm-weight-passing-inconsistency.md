# vllm-project/vllm#39370: [RFC][vLLM IR] `rms_norm` weight passing inconsistency

| 字段 | 值 |
| --- | --- |
| Issue | [#39370](https://github.com/vllm-project/vllm/issues/39370) |
| 状态 | open |
| 标签 | RFC;vllm-ir |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | activation;cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC][vLLM IR] `rms_norm` weight passing inconsistency

### Issue 正文摘录

### Problem In some models, the `RMSNorm` layer is unweighted (`has_weight=True`), effectively the same as the `weight` tensor set to all 1s. This can also be implemented by not applying the weight tensor at all. However, some implementations (`vllm_c`, `aiter`) always require the weight tensor. While always passing the weight tensor does not seem to affect native implementation performance, it does break TPU support, because we don't pass weight as a parameter so the XLA/JAX tensor conversion doesn't port the tensor over to TPU. Passing the parameter makes torch.compile unit tests start doing backwards through the model, which we can mitigate by using `@torch.inference_mode` or `torch.no_grad()`. But this still has the issue of passing the weight where we know that weight is all ones and not needed. We cannot include weight in `supports_args` because we don't want an implementation to be skipped because it doesn't support `weight=None`. We also don't want to allocate as it might affect eager-mode performance. ### Possible solutions - Current solution: pass weight conditionally, knowing which implementation will get selected. This does not work for fused ops. Perhaps we can do thi...

## 现有链接修复摘要

#41431 fix(llama): use weightless RMSNorm for FlashNorm-folded checkpoints (has_weight=False)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rt, because we don't pass weight as a parameter so the XLA/JAX tensor conversion doesn't port the tensor over to TPU. Passing the parameter makes torch.compile unit tests start doing backwards through the model, which w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `rms_norm` weight passing inconsistency RFC;vllm-ir ### Problem In some models, the `RMSNorm` layer is unweighted (`has_weight=True`), effectively the same as the `weight` tensor set to all 1s. This can also be implemen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ying the weight tensor at all. However, some implementations (`vllm_c`, `aiter`) always require the weight tensor. While always passing the weight tensor does not seem to affect native implementation performance, it doe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: op: this would pollute the op in my opinion - Alternative 5: Rewrite the CUDA and AITER kernels to support weight=None. This would work but isn't scalable, what if we run into something similar for other kernels? I hone...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ring. But this would be the most long-term fix as workspaces are needed elsewhere as well. - Alternative 3: Just allocate weight in implementations that need it and eat the overhead. - Alternative 4: Add a `has_weight=b...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41431](https://github.com/vllm-project/vllm/pull/41431) | mentioned | 0.6 | fix(llama): use weightless RMSNorm for FlashNorm-folded checkpoints (has_weight=False) | dent): <https://github.com/vllm-project/vllm/pull/40117> - vLLM Issue #39370 (related RFC, orthogonal): <https://github.com/vllm-project/vllm/issues/39370> - llama.cpp Issue #2248… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
