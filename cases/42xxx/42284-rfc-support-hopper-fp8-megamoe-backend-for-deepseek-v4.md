# vllm-project/vllm#42284: [RFC]: support hopper FP8 MegaMoE backend for DeepSeek-V4

| 字段 | 值 |
| --- | --- |
| Issue | [#42284](https://github.com/vllm-project/vllm/issues/42284) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;kernel;moe;operator;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: support hopper FP8 MegaMoE backend for DeepSeek-V4

### Issue 正文摘录

### Motivation. DeepSeek-V4's fused MoE expert kernel ("MegaMoE") is wired into vLLM for Blackwell (sm_100) as `DeepseekV4MegaMoEExperts`, calling `deep_gemm.fp8_fp4_mega_moe`. On **Hopper (sm_90 — H20 / H100 / H800)** that path is unusable because Hopper has no FP4 tensor cores. [DeepGEMM PR #323](https://github.com/deepseek-ai/DeepGEMM/pull/323)has just landed an SM90 sibling, `fp8_mega_moe`, that fuses the same five steps and accepts block-(128, 128) MN-major `float32` weight SF tensors **directly** This RFC proposes wiring `deep_gemm.fp8_mega_moe` into vLLM as a sibling of the existing FP4 MegaMoE class so DeepSeek-V4 served on Hopper (especially H20) gets the fused kernel benefit Blackwell already enjoys. ### Proposed Change. ### Adaptation points One file changed | Where | What | | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | | `vllm/model_executor/models/deepseek_v4.py` | Add `DeepseekV4HopperMegaMoEExperts` (block-FP8 sibling of `DeepseekV4MegaMoEExperts`) + an SM90 input-staging Triton kernel + a custom op. | |...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [RFC]: support hopper FP8 MegaMoE backend for DeepSeek-V4 RFC ### Motivation. DeepSeek-V4's fused MoE expert kernel ("MegaMoE") is wired into vLLM for Blackwell (sm_100) as `DeepseekV4MegaMoEExperts`, calling `deep_gemm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [RFC]: support hopper FP8 MegaMoE backend for DeepSeek-V4 RFC ### Motivation. DeepSeek-V4's fused MoE expert kernel ("MegaMoE") is wired into vLLM for Blackwell (sm_100) as `DeepseekV4MegaMoEExperts`, calling `deep_gemm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g of the existing FP4 MegaMoE class so DeepSeek-V4 served on Hopper (especially H20) gets the fused kernel benefit Blackwell already enjoys. ### Proposed Change. ### Adaptation points One file changed | Where | What
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [RFC]: support hopper FP8 MegaMoE backend for DeepSeek-V4 RFC ### Motivation. DeepSeek-V4's fused MoE expert kernel ("MegaMoE") is wired into vLLM for Blackwell (sm_100) as `DeepseekV4MegaMoEExperts`, calling `deep_gemm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [RFC]: support hopper FP8 MegaMoE backend for DeepSeek-V4 RFC ### Motivation. DeepSeek-V4's fused MoE expert kernel ("MegaMoE") is wired into vLLM for Blackwell (sm_100) as `DeepseekV4MegaMoEExperts`, calling `deep_gemm...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
