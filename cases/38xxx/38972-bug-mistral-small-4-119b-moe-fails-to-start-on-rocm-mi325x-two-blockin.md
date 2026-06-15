# vllm-project/vllm#38972: [Bug]: Mistral Small 4 (119B MoE) fails to start on ROCm MI325X - two blocking issues

| 字段 | 值 |
| --- | --- |
| Issue | [#38972](https://github.com/vllm-project/vllm/issues/38972) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;fp8;kernel;moe |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral Small 4 (119B MoE) fails to start on ROCm MI325X - two blocking issues

### Issue 正文摘录

### Your current environment - GPU: 8x AMD Instinct MI325X (256GB HBM3e each) - CPU: AMD EPYC 9575F - vLLM image: vllm/vllm-openai-rocm@sha256:cdea9cf61b3415bfdb4214ff56253f68645b0820d713a1745a21f0addeef4bd9 - mistral-common: 1.11.0 - ROCm: bundled in image ### 🐛 Describe the bug ## Summary Mistral Small 4 [(mistralai/Mistral-Small-4-119B-2603)](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) can't load on AMD MI325X GPUs with the current vLLM ROCm image. Two separate issues are currently preventing startup. I have listed them below with greater detail. Keen to try and work on the solution, unless I am doing something incorrectly? Please let me know if that is the case! ### Environment - GPU: 8x AMD Instinct MI325X (256GB VRAM each) - vLLM image: vllm/vllm-openai-rocm@sha256:cdea9cf61b3415bfdb4214ff56253f68645b0820d713a1745a21f0addeef4bd9 - ROCm: (bundled in image) - Model: mistralai/Mistral-Small-4-119B-2603 (119B MoE, 128 experts, 4 active, 32 attention heads) - mistral-common: upgraded to 1.11.0 (required for v15 tokenizer) - Tensor parallelism: TP=2 across 2x MI325X For context, I used: ```bash python3 -m vllm.entrypoints.openai.api_server \ --model mistralai/Mistr...

## 现有链接修复摘要

#39830 [ROCm][MLA] validate AITER head counts during selection

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: artup timeout: The 128-expert FP8 MoE kernels take 15-20+ minutes to JIT compile on MI325X. vLLM's engine startup times out before compilation finishes, even with `VLLM_ENGINE_READY_TIMEOUT_S=1800.` ### Issue 1: AITER M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Mistral Small 4 (119B MoE) fails to start on ROCm MI325X - two blocking issues bug;rocm ### Your current environment - GPU: 8x AMD Instinct MI325X (256GB HBM3e each) - CPU: AMD EPYC 9575F - vLLM image: vllm/vllm-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: uired. 2. MoE kernel compilation exceeds startup timeout: The 128-expert FP8 MoE kernels take 15-20+ minutes to JIT compile on MI325X. vLLM's engine startup times out before compilation finishes, even with `VLLM_ENGINE_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ## Issues **TLDR:** 1. Hard assertion blocks 32 attention heads: `rocm_aiter_mla.py:214` only allows 16 or 128 heads. Mistral Small 4 has 32. TP=2 works around it but shouldn't be required. 2. MoE kernel compilation exc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Summary Mistral Small 4 [(mistralai/Mistral-Small-4-119B-2603)](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) can't load on AMD MI325X GPUs with the current vLLM ROCm image. Two separate issues are current...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39830](https://github.com/vllm-project/vllm/pull/39830) | mentioned | 0.6 | [ROCm][MLA] validate AITER head counts during selection | eviewed the final diff and test results before opening this PR. Refs #38972. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
