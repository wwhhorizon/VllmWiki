# vllm-project/vllm#40256: [Bug]: Inaccurate available memory for KV cache when sleep mode is enabled likely due to custom allocators

| 字段 | 值 |
| --- | --- |
| Issue | [#40256](https://github.com/vllm-project/vllm/issues/40256) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inaccurate available memory for KV cache when sleep mode is enabled likely due to custom allocators

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Key Problem When sleep mode is enabled (and therefore custom CUDA allocators become part of the memory storage pathway), VLLM incorrectly estimates the amount of memory available for the KV cache and this can lead to OOM. ## Reproduction steps 1. Install/configure vllm (e.g., from commit bfde49e28) 2. Run the launch script below (on a dual-4090 system; may need to adapt the script to a single GPU, and, if so, use a smaller model that will fit in VRAM) 3. Observe out of memory error occurs and that launch reports "Available KV cache memory: 5.16 GiB" prior to crash" (**This estimate is incorrect and the root cause of the crash.**) 4. Run the same launch script without `--enable-sleep-mode` 5. Observe it loads correctly and that launch reports "Available KV cache memory: 3.17 GiB" (this is correct). Launch script: ```bash VLLM_SERVER_DEV_MODE=1 python -m vllm.entrypoints.openai.api_server \ --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \ --tensor-parallel-size 2 \ --dtype half \ --quantization awq_marlin \ --kv-cache-dtype fp8 \ --max-model-len 36000 \ --max-num-seqs 1 \ --gpu-memory-utilization 0.97 \ --host 0.0.0...

## 现有链接修复摘要

#40258 [Bugfix] Corrects estimate of torch memory use causing OOM due to incorrect KV cache space estimation when sleep mode on (Fixes #402…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ble for the KV cache and this can lead to OOM. ## Reproduction steps 1. Install/configure vllm (e.g., from commit bfde49e28) 2. Run the launch script below (on a dual-4090 system; may need to adapt the script to a singl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _MODE=1 python -m vllm.entrypoints.openai.api_server \ --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \ --tensor-parallel-size 2 \ --dtype half \ --quantization awq_marlin \ --kv-cache-dtype fp8 \ --max-mod...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: Inaccurate available memory for KV cache when sleep mode is enabled likely due to custom allocators bug ### Your current environment ### 🐛 Describe the bug ## Key Problem When sleep mode is enabled (and therefore...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the bug ## Key Problem When sleep mode is enabled (and therefore custom CUDA allocators become part of the memory storage pathway), VLLM incorrectly estimates the amount of memory available for the KV cache and this can...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the KV cache and this can lead to OOM. ## Reproduction steps 1. Install/configure vllm (e.g., from commit bfde49e28) 2. Run the launch script below (on a dual-4090 system; may need to adapt the script to a single GPU, a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40258](https://github.com/vllm-project/vllm/pull/40258) | closes_keyword | 0.95 | [Bugfix] Corrects estimate of torch memory use causing OOM due to incorrect KV cache space estimation when sleep mode on (Fixes #40256) | fixes issue #40256. To calculate how much memory is available for the KV cache vLLM profiles memory usage (gpu_worker.py calling mem_utils.py's measure() function). The strat |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
