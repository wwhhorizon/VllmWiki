# vllm-project/vllm#37777: [Bug]: [OOM] DeepSeek-R1 Out of Memory

| 字段 | 值 |
| --- | --- |
| Issue | [#37777](https://github.com/vllm-project/vllm/issues/37777) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | crash;nan_inf;oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [OOM] DeepSeek-R1 Out of Memory

### Issue 正文摘录

### Your current environment 4xGB200, vllm nightly, cu130 ### 🐛 Describe the bug Likely caused by https://github.com/vllm-project/vllm/pull/37442#issuecomment-4104485267 Creating an issue in case someone is also searching for this ``` export VLLM_USE_FLASHINFER_MOE_FP4=1 export VLLM_USE_NCCL_SYMM_MEM=1 export NCCL_NVLS_ENABLE=1 export NCCL_CUMEM_ENABLE=1 python3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8000 \ --model nvidia/DeepSeek-R1-0528-NVFP4 \ --trust-remote-code --no-enable-prefix-caching \ --dtype auto --kv-cache-dtype fp8 \ --tensor-parallel-size 1 --data-parallel-size 4 \ --max-num-seqs 1024 --max-model-len 10240 \ --gpu-memory-utilization 0.9 \ --max-num-batched-tokens 8192 \ --enable-expert-parallel --async-scheduling \ --compilation_config.max_cudagraph_capture_size 2048 \ --compilation_config.cudagraph_mode FULL_DECODE_ONLY ``` ``` vllm bench serve \ --host localhost --port 8000 \ --tokenizer nvidia/DeepSeek-R1-0528-NVFP4 \ --trust-remote-code --dataset-name random \ --random-input-len 2000 --random-output-len 1000 \ --ignore-eos --max-concurrency 128 \ --request-rate inf --num-prompts 640 Server crashes with: MemoryError: CUDA out of memory. Trie...

## 现有链接修复摘要

#37805 [Fix] Share decode output buffer across MLA layers to reduce memory | #37815 [MLAAttention] Clear Cudagraph padded region of FI decode Attention kernel

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: meone is also searching for this ``` export VLLM_USE_FLASHINFER_MOE_FP4=1 export VLLM_USE_NCCL_SYMM_MEM=1 export NCCL_NVLS_ENABLE=1 export NCCL_CUMEM_ENABLE=1 python3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: g]: [OOM] DeepSeek-R1 Out of Memory bug ### Your current environment 4xGB200, vllm nightly, cu130 ### 🐛 Describe the bug Likely caused by https://github.com/vllm-project/vllm/pull/37442#issuecomment-4104485267 Creating...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: dagraph_capture_size 2048 \ --compilation_config.cudagraph_mode FULL_DECODE_ONLY ``` ``` vllm bench serve \ --host localhost --port 8000 \ --tokenizer nvidia/DeepSeek-R1-0528-NVFP4 \ --trust-remote-code --dataset-name r...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: [OOM] DeepSeek-R1 Out of Memory bug ### Your current environment 4xGB200, vllm nightly, cu130 ### 🐛 Describe the bug Likely caused by https://github.com/vllm-project/vllm/pull/37442#issuecomment-4104485267 Creati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8000 \ --model nvidia/DeepSeek-R1-0528-NVFP4 \ --trust-remote-code --no-enable-prefix-caching \ --dtype auto --kv-cache-dtype fp8 \ --tensor-parallel-size 1 --data...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37805](https://github.com/vllm-project/vllm/pull/37805) | closes_keyword | 0.95 | [Fix] Share decode output buffer across MLA layers to reduce memory | Fixes #37777 ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The |
| [#37815](https://github.com/vllm-project/vllm/pull/37815) | closes_keyword | 0.95 | [MLAAttention] Clear Cudagraph padded region of FI decode Attention kernel | Fixes : #37777 Flashinfer issue : https://github.com/flashinfer-ai/flashinfer/issues/2883 ## Test Plan Run `nvidia/DeepSeek-R1-0528-NVFP4-v2` in a wide-ep setup and run lm_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
