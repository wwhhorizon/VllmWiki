# vllm-project/vllm#36922: [Performance]: Flashinfer TRTLLM MoE for Qwen3.5

| 字段 | 值 |
| --- | --- |
| Issue | [#36922](https://github.com/vllm-project/vllm/issues/36922) |
| 状态 | open |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | hardware_porting;moe;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | fp8;moe;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Flashinfer TRTLLM MoE for Qwen3.5

### Issue 正文摘录

### Proposal to improve performance I noticed the following issues with respect to performance of Qwen3.5 Moe configurations - [ ] FlashInfer TRTLLM routed MoE FP4 has disabled autotuning https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/fused_moe/trtllm_moe.py#L178 - [ ] FlashInfer TRTLLM routed MoE FP8 has disabled autotuning (could be enabled after PR https://github.com/flashinfer-ai/flashinfer/pull/2640) - [ ] Autotuning of Flashinfer trtllm block scale fp4 with Qwen 3.5 sizes produces zero cached tuning results. Fallback strategy is selected. - [ ] Always selects fallback strategy instead of cached tuning result for Flashinfer TRTLLM BF16 MoE (due to recent change in main https://github.com/flashinfer-ai/flashinfer/pull/2594) - [ ] Always selects fallback strategy instead of cached tuning result for Flashinfer TRTLLM FP8 MoE (PR open https://github.com/flashinfer-ai/flashinfer/pull/2640) - [ ] Flashinfer TRTLLM BF16 MoE faster than block scale FP8 for larger number of tokens or higher EP. Could try MXFP8 MoE for Qwen 3.5. Benchmark on 1x NVIDIA Blackwell B200 with Qwen3.5 configuration: - num_experts = 512 - topk = 10 - intermediate_size = 1024 - hidde...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: rmance of Qwen3.5 Moe configurations - [ ] FlashInfer TRTLLM routed MoE FP4 has disabled autotuning https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/fused_moe/trtllm_moe.py#L178 - [ ] FlashInfer...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Performance]: Flashinfer TRTLLM MoE for Qwen3.5 performance ### Proposal to improve performance I noticed the following issues with respect to performance of Qwen3.5 Moe configurations - [ ] FlashInfer TRTLLM routed Mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Performance]: Flashinfer TRTLLM MoE for Qwen3.5 performance ### Proposal to improve performance I noticed the following issues with respect to performance of Qwen3.5 Moe configurations - [ ] FlashInfer TRTLLM routed Mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: or higher EP. Could try MXFP8 MoE for Qwen 3.5. Benchmark on 1x NVIDIA Blackwell B200 with Qwen3.5 configuration: - num_experts = 512 - topk = 10 - intermediate_size = 1024 - hidden_size = 4096 - routing_method_type = R...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: Flashinfer TRTLLM MoE for Qwen3.5 performance ### Proposal to improve performance I noticed the following issues with respect to performance of Qwen3.5 Moe configurations - [ ] FlashInfer TRTLLM routed Mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
