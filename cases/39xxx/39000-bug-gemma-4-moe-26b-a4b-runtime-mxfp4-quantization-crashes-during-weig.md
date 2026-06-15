# vllm-project/vllm#39000: [Bug]: Gemma 4 MoE (26B-A4B) — runtime MXFP4 quantization crashes during weight loading in fused MoE layer

| 字段 | 值 |
| --- | --- |
| Issue | [#39000](https://github.com/vllm-project/vllm/issues/39000) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;moe;quantization |
| 症状 | crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 MoE (26B-A4B) — runtime MXFP4 quantization crashes during weight loading in fused MoE layer

### Issue 正文摘录

### Your current environment - vLLM version: v0.19.0 - GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB GDDR7, SM 12.0) - OS: Linux 5.15.0-171-generic - CUDA: 13.0 - Python: 3.12 - Docker image: `vllm/vllm-openai:v0.19.0-x86_64-cu130-ubuntu2404` (with `transformers>=5.5.0`) ## Model `google/gemma-4-26B-A4B-it` (MoE, 128 experts, 8 active per token) ## Command ```bash vllm serve google/gemma-4-26B-A4B-it \ --data-parallel-size 1 \ --quantization mxfp4 \ --max-model-len 25600 \ --max-num-seqs 32 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.92 \ --trust-remote-code ``` ### 🐛 Describe the bug Runtime MXFP4 quantization (`--quantization mxfp4`) crashes during weight loading for the Gemma 4 MoE model, even with `--data-parallel-size 1`. The fused MoE weight loader at `layer.py:1073` attempts to access `loaded_weight.shape[2]`, but the weight tensor is 2D, not 3D, causing an `IndexError`. This is effectively the same class of bug as #35329 and #35324, but specifically reproduced with `google/gemma-4-26B-A4B-it` (Gemma 4 MoE). Filing separately because: 1. Those issues focus on other MoE architectures (DeepSeek, Qwen, Mixtral). 2. Gemma 4 MoE is a new model with a unique exp...

## 现有链接修复摘要

#39067 [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Gemma 4 MoE (26B-A4B) — runtime MXFP4 quantization crashes during weight loading in fused MoE layer bug ### Your current environment - vLLM version: v0.19.0 - GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (96...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ight loading in fused MoE layer bug ### Your current environment - vLLM version: v0.19.0 - GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB GDDR7, SM 12.0) - OS: Linux 5.15.0-171-generic - CUDA: 13.0 - Python: 3....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: bug ### Your current environment - vLLM version: v0.19.0 - GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB GDDR7, SM 12.0) - OS: Linux 5.15.0-171-generic - CUDA: 13.0 - Python: 3.12 - Docker image: `vllm/vllm-op...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma 4 MoE (26B-A4B) — runtime MXFP4 quantization crashes during weight loading in fused MoE layer bug ### Your current environment - vLLM version: v0.19.0 - GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (96...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Gemma 4 MoE (26B-A4B) — runtime MXFP4 quantization crashes during weight loading in fused MoE layer bug ### Your current environment - vLLM version: v0.19.0 - GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (96...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39067](https://github.com/vllm-project/vllm/pull/39067) | mentioned | 0.6 | [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema | - #38999 — \`--data-parallel-size > 1\` crash in CUDA communicator - #39000 — MXFP4 quantization crash during weight loading ## Why not a duplicate Searched open issues and PRs fo… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
