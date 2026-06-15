# vllm-project/vllm#42846: [Bug][CI] NIXL + FlashInfer fails with Qwen3 MRV2 and --block-size 128

| 字段 | 值 |
| --- | --- |
| Issue | [#42846](https://github.com/vllm-project/vllm/issues/42846) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][CI] NIXL + FlashInfer fails with Qwen3 MRV2 and --block-size 128

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Environment vLLM commit: around `ae4f59f0e` / current main after that commit Model: `Qwen/Qwen3-0.6B` Backend: `FLASHINFER` KV connector: `NixlConnector` KV cache layout: `HND` Block size: `128` Model runner: V2 ### What happened The server fails during startup when running Qwen3 with Model Runner V2, FlashInfer, NIXL, and `--block-size 128`. The failure happens while registering KV caches in the NIXL worker: ```text AssertionError: All kv cache tensors must have the same number of blocks; layer=model.layers.0.self_attn.attn, expected_num_blocks=3626, cache_shape=(1813, 2, 128, 4, 128), cache_stride=(131072, 65536, 128, 16384, 1), layer_spec=FullAttentionSpec, backend=FLASHINFER, all_backends=['FLASHINFER'], kv_cache_layout=HND, blocks_first=True ``` ### Repro This does not require TP=2. A single CUDA GPU is enough because the failure happens during startup. Expected to fail with the default Qwen3 V2 Model Runner path: ```bash VLLM_KV_CACHE_LAYOUT=HND \ CUDA_VISIBLE_DEVICES=0 \ python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-0.6B \ --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' \...

## 现有链接修复摘要

#42872 [Bugfix][Model Runner v2] Fix MRV2 KV cache kernel block sizing.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][CI] NIXL + FlashInfer fails with Qwen3 MRV2 and --block-size 128 bug ### Your current environment ### 🐛 Describe the bug ### Environment vLLM commit: around `ae4f59f0e` / current main after that commit Model: `Qwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug][CI] NIXL + FlashInfer fails with Qwen3 MRV2 and --block-size 128 bug ### Your current environment ### 🐛 Describe the bug ### Environment vLLM commit: around `ae4f59f0e` / current main after that commit Model: `
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ocks_first=True ``` ### Repro This does not require TP=2. A single CUDA GPU is enough because the failure happens during startup. Expected to fail with the default Qwen3 V2 Model Runner path: ```bash VLLM_KV_CACHE_LAYOU...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug][CI] NIXL + FlashInfer fails with Qwen3 MRV2 and --block-size 128 bug ### Your current environment ### 🐛 Describe the bug ### Environment vLLM commit: around `ae4f59f0e` / current main after that commit Model: `Qwe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug][CI] NIXL + FlashInfer fails with Qwen3 MRV2 and --block-size 128 bug ### Your current environment ### 🐛 Describe the bug ### Environment vLLM commit: around `ae4f59f0e` / current main after that commit Model: `Qwe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42872](https://github.com/vllm-project/vllm/pull/42872) | closes_keyword | 0.95 | [Bugfix][Model Runner v2] Fix MRV2 KV cache kernel block sizing. | Closes #42846 ## Test Plan - Added a focused MRV2 block table regression test. - Verified the Qwen3 + FlashInfer + NIXL single-GPU startup repro. ## Test Result |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
