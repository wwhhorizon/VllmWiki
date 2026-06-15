# vllm-project/vllm#27173: [Performance]: non-optimal performance of `linear` for small batches

| 字段 | 值 |
| --- | --- |
| Issue | [#27173](https://github.com/vllm-project/vllm/issues/27173) |
| 状态 | open |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;gemm_linear |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: non-optimal performance of `linear` for small batches

### Issue 正文摘录

### Proposal to improve performance Originally found on Qwen3-next with small batch sizes but should be actual for another models. For batch sizes <= 32 torch's linear implementation isn't optimal. Below is comparison with implementation in FlashInfer. I used input/output features num from actual gemm inside GDN attn, Qwen3-next. B200 GPU. ``` batch=1 ============================================================================================================== SUMMARY COMPARISON ============================================================================================================== Variant Median (us) Std (us) GFLOPS BW (GB/s) Speedup -------------------------------------------------------------------------------------------------------------- 1. Original 11.857920 0.017042 1414.85 1415.89 1.00x 2. torch.compile() 11.852800 0.010392 1415.46 1416.50 1.00x 3. max-autotune ncg 4.402560 0.007621 3810.79 3813.58 2.69x 4. TGV GEMM pdl=False 6.794880 0.009877 2469.10 2470.91 1.75x 5. TGV GEMM pdl=True 6.135360 0.014390 2734.51 2736.51 1.93x batch=2 ============================================================================================================== SUMMARY COMPARISON =====...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 11.857920 0.017042 1414.85 1415.89 1.00x 2. torch.compile() 11.852800 0.010392 1415.46 1416.50 1.00x 3. max-autotune ncg 4.402560 0.007621 3810.79 3813.58 2.69x 4. TGV GEMM pdl=False
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: non-optimal performance of `linear` for small batches performance;stale ### Proposal to improve performance Originally found on Qwen3-next with small batch sizes but should be actual for another models. F...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 60 0.007621 3810.79 3813.58 2.69x 4. TGV GEMM pdl=False 6.794880 0.009877 2469.10 2470.91 1.75x 5. TGV GEMM pdl=True 6.135360 0.014390 2734.51 2736.51 1.93x batch=2 ===================================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rformance;stale ### Proposal to improve performance Originally found on Qwen3-next with small batch sizes but should be actual for another models. For batch sizes <= 32 torch's linear implementation isn't optimal. Below...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: implementation isn't optimal. Below is comparison with implementation in FlashInfer. I used input/output features num from actual gemm inside GDN attn, Qwen3-next. B200 GPU. ``` batch=1 =================================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
