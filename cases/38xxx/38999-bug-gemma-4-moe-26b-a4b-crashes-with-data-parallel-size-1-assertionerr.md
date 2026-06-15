# vllm-project/vllm#38999: [Bug]: Gemma 4 MoE (26B-A4B) crashes with `--data-parallel-size > 1` — AssertionError in cuda_communicator all_gather

| 字段 | 值 |
| --- | --- |
| Issue | [#38999](https://github.com/vllm-project/vllm/issues/38999) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | shape_align |
| Operator 关键词 | cuda;fp8;moe;quantization |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 MoE (26B-A4B) crashes with `--data-parallel-size > 1` — AssertionError in cuda_communicator all_gather

### Issue 正文摘录

### Your current environment - vLLM version: v0.19.0 (also reproduced on `vllm/vllm-openai:gemma4-x86_64-cu130`) - GPU: 8x NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB GDDR7, SM 12.0) - OS: Linux 5.15.0-171-generic - CUDA: 13.0 - Python: 3.12 - Docker image: `vllm/vllm-openai:v0.19.0-x86_64-cu130-ubuntu2404` (with `transformers>=5.5.0` installed for Gemma 4 support) ## Model `google/gemma-4-26B-A4B-it` (Mixture-of-Experts, 25.2B total params, 3.8B active, 128 experts with 8 active per token) ## Command ```bash vllm serve google/gemma-4-26B-A4B-it \ --data-parallel-size 2 \ --quantization fp8 \ --max-model-len 25600 \ --max-num-seqs 32 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.92 \ --trust-remote-code ``` GPUs assigned: 2 GPUs (device IDs 6 and 7). ### 🐛 Describe the bug ## Description Gemma 4 MoE model crashes at runtime when `--data-parallel-size` is set to anything greater than 1. The model loads weights successfully, captures CUDA graphs, and starts API servers — but fails on the **first inference request** with an `AssertionError` inside the expert-parallel all-gather communication path. This was also reproduced with `--quantization mxfp4` (which crashes earlie...

## 现有链接修复摘要

#39067 [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: in cuda_communicator all_gather bug ### Your current environment - vLLM version: v0.19.0 (also reproduced on `vllm/vllm-openai:gemma4-x86_64-cu130`) - GPU: 8x NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB GDDR7, SM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: sh vllm serve google/gemma-4-26B-A4B-it \ --data-parallel-size 2 \ --quantization fp8 \ --max-model-len 25600 \ --max-num-seqs 32 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.92 \ --trust-remote-code ``` GPUs ass...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: oE (26B-A4B) crashes with `--data-parallel-size > 1` — AssertionError in cuda_communicator all_gather bug ### Your current environment - vLLM version: v0.19.0 (also reproduced on `vllm/vllm-openai:gemma4-x86_64-cu130`)...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Bug]: Gemma 4 MoE (26B-A4B) crashes with `--data-parallel-size > 1` — AssertionError in cuda_communicator all_gather bug ### Your current environment - vLLM version: v0.19.0 (also reproduced on `vllm/vllm-openai:gemma4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma 4 MoE (26B-A4B) crashes with `--data-parallel-size > 1` — AssertionError in cuda_communicator all_gather bug ### Your current environment - vLLM version: v0.19.0 (also reproduced on `vllm/vllm-openai:gemma4...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39067](https://github.com/vllm-project/vllm/pull/39067) | mentioned | 0.6 | [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema | Tensor kv_seqlens, " \`\`\` --- ## What this PR does NOT address - #38999 — \`--data-parallel-size > 1\` crash in CUDA communicator - #39000 — MXFP4 quantization crash during weig… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
