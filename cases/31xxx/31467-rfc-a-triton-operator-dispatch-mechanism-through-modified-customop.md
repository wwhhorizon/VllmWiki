# vllm-project/vllm#31467: [RFC]: A Triton operator dispatch mechanism through modified `CustomOp`

| 字段 | 值 |
| --- | --- |
| Issue | [#31467](https://github.com/vllm-project/vllm/issues/31467) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;gemm_linear;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: A Triton operator dispatch mechanism through modified `CustomOp`

### Issue 正文摘录

### Motivation. Triton is becoming increasingly important in vLLM, and we've noticed its use in many models, quantization processes, and general workflows. Meanwhile, vLLM supports various backends. Typically, to achieve high performance, **different implementations of the Triton kernels** are used on different hardware, such as Ascend NPU. However, we've observed that vLLM currently lacks an effective operator dispatch mechanism for Triton to ensure that various backends can implement their own Triton kernels, which are then uniformly called by vLLM. There are 3 ways of calling triton function now: #### Through Attention Backend Triton functions are called in `Attention` layer when the attention backend is specified as `TRITON_ATTN` or `TRITON_MLA`. ```python current_platform.get_attn_backend_cls(...) ``` #### Through CustomOp Some triton functions are included in other customops's forward pipeline, and they are put into `forward_cuda`, e.g., `causal_conv1d_fn` and `causal_conv1d_update` in `ShortConv`. ```python class op1(CustomOp): def forward_cuda(kwargs): triton_fn(**kwargs) ``` #### Directly call And there are others directly call triton functions in the normal pipeline. - s...

## 现有链接修复摘要

#31521 [Triton][CustomOp] A Triton operator dispatch mechanism through modified CustomOp

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [RFC]: A Triton operator dispatch mechanism through modified `CustomOp` RFC ### Motivation. Triton is becoming increasingly important in vLLM, and we've noticed its use in many models, quantization processes, and genera...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [RFC]: A Triton operator dispatch mechanism through modified `CustomOp` RFC ### Motivation. Triton is becoming increasingly important in vLLM, and we've noticed its use in many models, quantization processes, and genera...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: modified `CustomOp` RFC ### Motivation. Triton is becoming increasingly important in vLLM, and we've noticed its use in many models, quantization processes, and general workflows. Meanwhile, vLLM supports various backen...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: rd - Qwen3-Next - Kimi-Linear - ... - modelrunner v2 - block table - input batch Also, I notice that the implements are different form rocm and nvidia, algouth they are both cuda-alike platform. ```python if current_pla...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ncreasingly important in vLLM, and we've noticed its use in many models, quantization processes, and general workflows. Meanwhile, vLLM supports various backends. Typically, to achieve high performance, **different impl...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31521](https://github.com/vllm-project/vllm/pull/31521) | mentioned | 0.6 | [Triton][CustomOp] A Triton operator dispatch mechanism through modified CustomOp | s://github.com/vllm-project/vllm/issues/31467 This is the first pr of #31467, introducing the triton dispatch machenism into vLLM and making the new triton kernel usage in Qwen3-N… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
