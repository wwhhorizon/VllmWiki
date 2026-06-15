# vllm-project/vllm#39025: [Bug]: CUDA illegal memory access with CUDA graphs enabled under high concurrency (Qwen3.5-35B-A3B, tp=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#39025](https://github.com/vllm-project/vllm/issues/39025) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access with CUDA graphs enabled under high concurrency (Qwen3.5-35B-A3B, tp=2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM crashes with `torch.AcceleratorError: CUDA error: an illegal memory access was encountered` when serving `Qwen/Qwen3.5-35B-A3B` with `--tensor-parallel-size 2` and hitting it with 100 concurrent requests. The crash occurs during the decode phase after all 100 requests have completed prefill. **This is a regression** — vLLM `0.19.0` (pip release) does NOT crash under identical conditions. ### Reproduction steps **1. Install vLLM from main (crashes):** ```bash uv venv --python 3.12 source .venv/bin/activate uv pip install vllm # or install from source at main ``` **2. Start the server:** ```bash vllm serve Qwen/Qwen3.5-35B-A3B \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.8 \ --port 8001 ``` **3. Send 100 concurrent requests using vllm bench:** ```bash vllm bench serve \ --model Qwen/Qwen3.5-35B-A3B \ --port 8001 \ --dataset-name random \ --random-input-len 512 \ --random-output-len 128 \ --num-prompts 100 \ --request-rate inf ``` The server crashes during the decode phase with: ``` torch.AcceleratorError: CUDA error: an illegal memory access was encountered ``` At the time of the crash, the scheduler state shows: -...

## 现有链接修复摘要

#39064 [Bugfix] Fix GDN FLA kernel crashes with NULL_BLOCK_ID=0 CUDA graph padding

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: does NOT crash under identical conditions. ### Reproduction steps **1. Install vLLM from main (crashes):** ```bash uv venv --python 3.12 source .venv/bin/activate uv pip install vllm # or install from source at main ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA illegal memory access with CUDA graphs enabled under high concurrency (Qwen3.5-35B-A3B, tp=2) ### Your current environment ### 🐛 Describe the bug vLLM crashes with `torch.AcceleratorError: CUDA error: an ill...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: -A3B` with `--tensor-parallel-size 2` and hitting it with 100 concurrent requests. The crash occurs during the decode phase after all 100 requests have completed prefill. **This is a regression** — vLLM `0.19.0` (pip re...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: f the crash, the scheduler state shows: - `kv_cache_usage = ~11.5%` (not OOM) - `num_running_reqs = 100`, all with `num_scheduled_tokens: 1` (decode phase) - KV cache has 920,832 tokens available **4. Verify with vLLM 0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: A illegal memory access with CUDA graphs enabled under high concurrency (Qwen3.5-35B-A3B, tp=2) ### Your current environment ### 🐛 Describe the bug vLLM crashes with `torch.AcceleratorError: CUDA error: an illegal memor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39064](https://github.com/vllm-project/vllm/pull/39064) | closes_keyword | 0.95 | [Bugfix] Fix GDN FLA kernel crashes with NULL_BLOCK_ID=0 CUDA graph padding | Fixes #39025 — GDN (Gated Delta Network) hybrid models crash with IMA (Illegal Memory Access) errors under CUDA graphs + TP>1 on Blackwell GPUs. **Root cause**: Commit `bcc6f6744` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
