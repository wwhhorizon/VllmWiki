# vllm-project/vllm#38056: [Bug]: ImportError: flash_attn.ops.triton.rotary not found on older versions (< v2.1.2)

| 字段 | 值 |
| --- | --- |
| Issue | [#38056](https://github.com/vllm-project/vllm/issues/38056) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ImportError: flash_attn.ops.triton.rotary not found on older versions (< v2.1.2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve /home/xiongjie/run_vlm/Qwen/Qwen3.5-4B --port 19995 (APIServer pid=19) INFO 03-25 01:54:36 [utils.py:302] (APIServer pid=19) INFO 03-25 01:54:36 [utils.py:302] █ █ █▄ ▄█ (APIServer pid=19) INFO 03-25 01:54:36 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.1 (APIServer pid=19) INFO 03-25 01:54:36 [utils.py:302] █▄█▀ █ █ █ █ model /home/xiongjie/run_vlm/Qwen/Qwen3.5-4B (APIServer pid=19) INFO 03-25 01:54:36 [utils.py:302] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=19) INFO 03-25 01:54:36 [utils.py:302] (APIServer pid=19) INFO 03-25 01:54:36 [utils.py:238] non-default args: {'model_tag': '/home/xiongjie/run_vlm/Qwen/Qwen3.5-4B', 'port': 19995, 'model': '/home/xiongjie/run_vlm/Qwen/Qwen3.5-4B'} (APIServer pid=19) Unrecognized keys in `rope_parameters` for 'rope_type'='default': {'mrope_section', 'mrope_interleaved'} (APIServer pid=19) Unrecognized keys in `rope_parameters` for 'rope_type'='default': {'mrope_section', 'mrope_interleaved'} (APIServer pid=19) INFO 03-25 01:54:43 [model.py:531] Resolved architecture: Qwen3_5ForConditionalGeneration (APIServer pid=19) INFO 03-25 01:54:43 [model.py:1554] Using max model len 262144 (APISer...

## 现有链接修复摘要

#38091 [Bugfix] Fix ImportError for flash_attn < v2.1.2 missing triton rotary module

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: ImportError: flash_attn.ops.triton.rotary not found on older versions (< v2.1.2) bug ### Your current environment ### 🐛 Describe the bug vllm serve /home/xiongjie/run_vlm/Qwen/Qwen3.5-4B --port 19995 (APIServer p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: ImportError: flash_attn.ops.triton.rotary not found on older versions (< v2.1.2) bug ### Your current environment ### 🐛 Describe the bug vllm serve /home/xiongjie/run_vlm/Qwen/Qwen3.5-4B --port 19995 (APIServer p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: nt environment ### 🐛 Describe the bug vllm serve /home/xiongjie/run_vlm/Qwen/Qwen3.5-4B --port 19995 (APIServer pid=19) INFO 03-25 01:54:36 [utils.py:302] (APIServer pid=19) INFO 03-25 01:54:36 [utils.py:302] █ █ █▄ ▄█...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: (APIServer pid=19) INFO 03-25 01:54:43 [config.py:544] Setting attention block size to 528 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=19) INFO 03-25 01:54:43 [config.py:575] Padding...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38091](https://github.com/vllm-project/vllm/pull/38091) | closes_keyword | 0.95 | [Bugfix] Fix ImportError for flash_attn < v2.1.2 missing triton rotary module | Fixes #38056 ## Before / After <details> <summary>Before (old code — crashes)</summary> ``` === Before Fix: Old code path === find_spec("flash_attn"): ModuleSpec(name='flash_at |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
