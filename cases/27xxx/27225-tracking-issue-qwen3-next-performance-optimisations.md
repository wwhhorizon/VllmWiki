# vllm-project/vllm#27225: [Tracking Issue]: Qwen3-next performance optimisations

| 字段 | 值 |
| --- | --- |
| Issue | [#27225](https://github.com/vllm-project/vllm/issues/27225) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking Issue]: Qwen3-next performance optimisations

### Issue 正文摘录

### Proposal to improve performance This is a tracking issue for performance optimization for Qwen3-next to keep all necessary things in one place. - [ ] Optimized GDN prefill: #33291 Hopper: #32846 Blackwell - [ ] Optimized GDN decode - [ ] GDN prefix cache #26807 - [ ] FP8 Blockwise GEMM: https://github.com/flashinfer-ai/flashinfer/issues/2146 - [x] `torch.compile` for GDN attn #27152 - [x] Full CudaGraph for TRT-LLM Gen attn (for MTP only) #28479 - [x] Enable TRT-LLM Gen MoE. FP16: #32954 FP8: #27492 FP4: DONE: https://github.com/flashinfer-ai/flashinfer/pull/1831 - [x] Moving of the gate / router op to be after the shared_experts execution. #27578 #26440 for reference. - [x] async-sched + spec-decoding (not Qwen3-next specific feature, but required) #24799 - [x] GDN speedup #31722 - [ ] not optimal `linear` for small batch sizes #27173 - [ ] GDN attn decrease CPU overhead #27222

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: sary things in one place. - [ ] Optimized GDN prefill: #33291 Hopper: #32846 Blackwell - [ ] Optimized GDN decode - [ ] GDN prefix cache #26807 - [ ] FP8 Blockwise GEMM: https://github.com/flashinfer-ai/flashinfer/issue...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ] Optimized GDN decode - [ ] GDN prefix cache #26807 - [ ] FP8 Blockwise GEMM: https://github.com/flashinfer-ai/flashinfer/issues/2146 - [x] `torch.compile` for GDN attn #27152 - [x] Full CudaGraph for TRT-LLM Gen attn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: MM: https://github.com/flashinfer-ai/flashinfer/issues/2146 - [x] `torch.compile` for GDN attn #27152 - [x] Full CudaGraph for TRT-LLM Gen attn (for MTP only) #28479 - [x] Enable TRT-LLM Gen MoE. FP16: #32954 FP8: #2749...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Blackwell - [ ] Optimized GDN decode - [ ] GDN prefix cache #26807 - [ ] FP8 Blockwise GEMM: https://github.com/flashinfer-ai/flashinfer/issues/2146 - [x] `torch.compile` for GDN attn #27152 - [x] Full CudaGraph for TRT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n3-next to keep all necessary things in one place. - [ ] Optimized GDN prefill: #33291 Hopper: #32846 Blackwell - [ ] Optimized GDN decode - [ ] GDN prefix cache #26807 - [ ] FP8 Blockwise GEMM: https://github.com/flash...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
