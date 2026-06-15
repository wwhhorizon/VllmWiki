# vllm-project/vllm#43235: [RFC] NSA is architecturally incompatible with NVIDIA consumer/workstation GPUs — MLA is the only viable sparse attention path

| 字段 | 值 |
| --- | --- |
| Issue | [#43235](https://github.com/vllm-project/vllm/issues/43235) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] NSA is architecturally incompatible with NVIDIA consumer/workstation GPUs — MLA is the only viable sparse attention path

### Issue 正文摘录

### Motivation. After extensive production testing on SM120 (RTX PRO 6000 Blackwell, 8×96GB, PCIe Gen5), NSA (Native Sparse Attention) cannot be made to work reliably for production serving on NVIDIA consumer/workstation GPUs. This is not a bug — it is an architectural incompatibility. The fundamental problems: 1. **NSA requires dynamic sparse index computation at every decode step.** This means per-layer, per-token topk selection over the full KV cache. On SM100 (datacenter Blackwell), dedicated FP8 block-scaled GEMM units handle this efficiently. On SM120, these units do not exist — the sparse indexer falls back to software paths that are both slow and correctness-problematic. 2. **PCIe topology makes NSA+MTP catastrophically unreliable.** The b12x PCIe oneshot allreduce has a buffer reuse race under CUDA graph/no-copy mode. The only known fix (a completion barrier in `pcie_oneshot.cu`) costs ~1 tok/s and still does not guarantee correctness under concurrent serving. MTP + TP>1 + concurrent>1 produces deadlocks (see #41402, #41404 — both closed without resolution). 3. **SM120 is not SM100.** FP8 block-scaled GEMM kernels written for SM100 crash or produce garbage on SM120 (#2621...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: ction over the full KV cache. On SM100 (datacenter Blackwell), dedicated FP8 block-scaled GEMM units handle this efficiently. On SM120, these units do not exist — the sparse indexer falls back to software paths that are...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [RFC] NSA is architecturally incompatible with NVIDIA consumer/workstation GPUs — MLA is the only viable sparse attention path RFC ### Motivation. After extensive production testing on SM120 (RTX PRO 6000 Blackwell, 8×9...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: extensive production testing on SM120 (RTX PRO 6000 Blackwell, 8×96GB, PCIe Gen5), NSA (Native Sparse Attention) cannot be made to work reliably for production serving on NVIDIA consumer/workstation GPUs. This is not a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: l problems: 1. **NSA requires dynamic sparse index computation at every decode step.** This means per-layer, per-token topk selection over the full KV cache. On SM100 (datacenter Blackwell), dedicated FP8 block-scaled G...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: n over the full KV cache. On SM100 (datacenter Blackwell), dedicated FP8 block-scaled GEMM units handle this efficiently. On SM120, these units do not exist — the sparse indexer falls back to software paths that are bot...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
