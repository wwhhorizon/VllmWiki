# vllm-project/vllm#41687: [Bug]: DeepEP MoE all-to-all backend integration is unusable on Blackwell (SM103 / GB300)

| 字段 | 值 |
| --- | --- |
| Issue | [#41687](https://github.com/vllm-project/vllm/issues/41687) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;kernel;moe |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepEP MoE all-to-all backend integration is unusable on Blackwell (SM103 / GB300)

### Issue 正文摘录

### Your current environment ### Summary vLLM's DeepEP MoE all-to-all backend is currently unusable in our long-context disaggregated serving stack on GB300 (SM103). Given that decode-side communication is the dominant remaining bottleneck after the prefill attention kernel work, restoring the DeepEP path is a critical decode-side optimization. In our profiling on GB300 NVL72 (DeepSeek-R1-0528-FP4, decode side): - Communication accounts for **~93% of decode kernel time** (NCCL Broadcast + AllGather + Reduce + ReduceScatter combined). - We have already evaluated `flashinfer_nvlink_one_sided` (mnnvl-1sided) at DEP8: **no additional benefit over AG_RS** at our EP size. NVLink 1-sided helps only at large EP. - The remaining win has to come from kernel-fused dispatch or combine, i.e. DeepEP, not from a different transport. ### Environment - vLLM v0.17.0 - Hardware: NVIDIA GB300 (sm103) NVL72 - Model: DeepSeek-R1-0528-FP4 (MoE) - Deployment: 2 decode nodes × 8 GPUs (DEP8), disaggregated via `NixlConnector` ### Reproduction ```bash # Should be runnable on a GB300 NVL72 node with the standard # DeepSeek-R1-FP4 weights. vllm serve \ --pipeline-parallel-size 1 \ --tensor-parallel-size 1 \ -...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: estoring the DeepEP path is a critical decode-side optimization. In our profiling on GB300 NVL72 (DeepSeek-R1-0528-FP4, decode side): - Communication accounts for **~93% of decode kernel time** (NCCL Broadcast + AllGath...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: DeepEP MoE all-to-all backend integration is unusable on Blackwell (SM103 / GB300) bug ### Your current environment ### Summary vLLM's DeepEP MoE all-to-all backend is currently unusable in our long-context disag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: DeepEP MoE all-to-all backend integration is unusable on Blackwell (SM103 / GB300) bug ### Your current environment ### Summary vLLM's DeepEP MoE all-to-all backend is currently unusable in our long-context disag...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: de-side optimization. In our profiling on GB300 NVL72 (DeepSeek-R1-0528-FP4, decode side): - Communication accounts for **~93% of decode kernel time** (NCCL Broadcast + AllGather + Reduce + ReduceScatter combined). - We...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: DeepEP MoE all-to-all backend integration is unusable on Blackwell (SM103 / GB300) bug ### Your current environment ### Summary vLLM's DeepEP MoE all-to-all backend is currently unusable in our long-context disag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
