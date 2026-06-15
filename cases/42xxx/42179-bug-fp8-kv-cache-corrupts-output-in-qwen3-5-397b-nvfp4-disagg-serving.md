# vllm-project/vllm#42179: [Bug]: FP8 KV cache corrupts output in Qwen3.5-397B-NVFP4 Disagg serving

| 字段 | 值 |
| --- | --- |
| Issue | [#42179](https://github.com/vllm-project/vllm/issues/42179) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: FP8 KV cache corrupts output in Qwen3.5-397B-NVFP4 Disagg serving

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## IMPORTANT!!! Before reproducing this issue, Qwen3.5/GDN NIXL disagg support needs to be applied: - #41628: Support GDN conv-state splits for NIXL - #41869: PD disagg with NIXL Connector: GDN support (Qwen3.5) Without these patches, Qwen3.5 Disagg serving fails earlier because the GDN conv-state transfer path for NIXL is not fully implemented, so the FP8 KV cache correctness issue cannot be reached. ## Summary We found a correctness issue with Qwen3.5-397B-A17B-NVFP4 **Disagg** in vLLM when using `--kv-cache-dtype fp8`. The setup is a pure vLLM P/D disagg deployment using `vllm serve` with `NixlConnector`, without Dynamo. It was tested on **GB200** with: - Prefill: 1 GB200 node, 4 GPUs, `tensor-parallel-size=4`, expert parallel enabled - Decode: 1 GB200 node, 4 GPUs, `tensor-parallel-size=4`, expert parallel enabled - Model: `nvidia/Qwen3.5-397B-A17B-NVFP4` - vLLM: `0.19.2rc1.dev215+g32e45636e` (`git sha: 32e45636e`) With the same disaggregated setup, `--kv-cache-dtype bfloat16` works as the baseline. When switching only the KV cache dtype to `fp8`, the model starts successfully but produces incorrect outputs, including very si...

## 现有链接修复摘要

#41628 Support GDN conv-state splits for NIXL | #41869 PD disagg with NIXL Connector: GDN support (Qwen3.5)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: FP8 KV cache corrupts output in Qwen3.5-397B-NVFP4 Disagg serving bug ### Your current environment ### 🐛 Describe the bug ## IMPORTANT!!! Before reproducing this issue, Qwen3.5/GDN NIXL disagg support needs to be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: serving bug ### Your current environment ### 🐛 Describe the bug ## IMPORTANT!!! Before reproducing this issue, Qwen3.5/GDN NIXL disagg support needs to be applied: - #41628: Support GDN conv-state splits for NIXL - #418...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: g `vllm serve` with `NixlConnector`, without Dynamo. It was tested on **GB200** with: - Prefill: 1 GB200 node, 4 GPUs, `tensor-parallel-size=4`, expert parallel enabled - Decode: 1 GB200 node, 4 GPUs, `tensor-parallel-s...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: tarts successfully but produces incorrect outputs, including very simple deterministic prompts such as arithmetic. Example observed output with `temperature=0`: ```text Prompt: 2 + 2 = Expected: 4 Observed: 5 ``` ## Tes...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: FP8 KV cache corrupts output in Qwen3.5-397B-NVFP4 Disagg serving bug ### Your current environment ### 🐛 Describe the bug ## IMPORTANT!!! Before reproducing this issue, Qwen3.5/GDN NIXL disagg support needs to be...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41628](https://github.com/vllm-project/vllm/pull/41628) | mentioned | 0.45 | Support GDN conv-state splits for NIXL | g this issue, qwen3.5/gdn nixl disagg support needs to be applied: - #41628: support gdn conv-state splits for nixl - #41869: pd disagg with nixl connector: gdn support (qwen3.5)… |
| [#41869](https://github.com/vllm-project/vllm/pull/41869) | mentioned | 0.45 | PD disagg with NIXL Connector: GDN support (Qwen3.5) | ds to be applied: - #41628: support gdn conv-state splits for nixl - #41869: pd disagg with nixl connector: gdn support (qwen3.5) without these patches, qwen3.5 disagg serving fai… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
