# vllm-project/vllm#29014: [Bug]: stride mismatch when using torch compile on graphs with splitting_ops and non-standard tensor dimensions

| 字段 | 值 |
| --- | --- |
| Issue | [#29014](https://github.com/vllm-project/vllm/issues/29014) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | edge_case |
| Operator 关键词 | activation;attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: stride mismatch when using torch compile on graphs with splitting_ops and non-standard tensor dimensions

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description **Stride mismatch error when using torch.compile with graph splitting custom ops, when the subgraph after the custom op receives as input a tensor view of a tensor from the subgraph before the custom op.** When compiling a model with vLLM's compilation backend that: 1. Uses splitting_ops to partition the computation graph at custom ops 2. Passes tensor views created by torch.split() or indexing a tensor created in the subgraph before the custom op, to the subgraph after the custom op 3. Uses non-standard tensor dimensions (I _think_ non-multiples of 32) The compilation fails with an assertion error about mismatched strides. See reproduction script. It seems the error occurs because torch Inductor applies memory padding/alignment for optimization (for the case in the reproduction script, the stride of `y` becomes 1056 instead of 1048, likely aligned to a memory boundary). However, when graph partitioning occurs at the custom op boundary, the compiled code of the next subgraph, which gets a view of a tensor created in the subgraph before the split, expects an unpadded stride. It doesn't know about the padding optimiz...

## 现有链接修复摘要

#28587 [Hybrid][torch.compile] Refactor mamba2 forward to avoid obscuring linear projections under custom op

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: stride mismatch when using torch compile on graphs with splitting_ops and non-standard tensor dimensions bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug ## Description **Stride mismatc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: stride mismatch when using torch compile on graphs with splitting_ops and non-standard tensor dimensions bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug ## Description **Stride mismatc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: stride mismatch when using torch compile on graphs with splitting_ops and non-standard tensor dimensions bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug ## Description **Stride mismatch
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: of a tensor from the subgraph before the custom op.** When compiling a model with vLLM's compilation backend that: 1. Uses splitting_ops to partition the computation graph at custom ops 2. Passes tensor views created by...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: before the custom op.** When compiling a model with vLLM's compilation backend that: 1. Uses splitting_ops to partition the computation graph at custom ops 2. Passes tensor views created by torch.split() or indexing a t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28587](https://github.com/vllm-project/vllm/pull/28587) | mentioned | 0.45 | [Hybrid][torch.compile] Refactor mamba2 forward to avoid obscuring linear projections under custom op | ny](https://huggingface.co/ibm-granite/granite-4.0-h-tiny). in pr [pr #28587](https://github.com/vllm-project/vllm/pull/28587), i worked around this by extracting `hidden_states_b… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
