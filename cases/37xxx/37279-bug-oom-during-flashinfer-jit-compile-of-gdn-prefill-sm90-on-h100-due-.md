# vllm-project/vllm#37279: [Bug]: OOM during FlashInfer JIT compile of gdn_prefill_sm90 on H100 due to many concurrent cicc processes

| 字段 | 值 |
| --- | --- |
| Issue | [#37279](https://github.com/vllm-project/vllm/issues/37279) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM during FlashInfer JIT compile of gdn_prefill_sm90 on H100 due to many concurrent cicc processes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On an H100 (sm90a), using vLLM 0.17.1, running inference against API after `vllm serve` triggers FlashInfer JIT compilation of: `~/.cache/flashinfer/0.6.6/90a/cached_ops/gdn_prefill_sm90/` During this step, many parallel nvcc jobs are launched, which fan out into many concurrent cicc processes. Each cicc process uses several GiB of host RAM, so total memory usage quickly grows until the host hits OOM. On a machine with 125 GiB RAM, memory reached about 117 GiB used during this compile burst. The OOM killer then started killing unrelated processes before inference could start. This looks like excessive JIT compile parallelism / memory usage in the FlashInfer gdn_prefill_sm90 path, rather than a generic CUDA initialization issue. **Environment** - vllm==0.17.1 - flashinfer-python==0.6.6 - CUDA 12.8 (/usr/local/cuda -> /usr/local/cuda-12.8, nvcc 12.8.93) - GCC/G++ 13.3.0 - Kernel 6.17.0-19-generic - GPU: H100 **Exact command used for vLLM serve** ``` CUDA_VISIBLE_DEVICES=0 \ vllm serve Qwen/Qwen3.5-2B \ --attention-backend FLASH_ATTN \ --enforce-eager \ --max-model-len 4096 \ --max-num-seqs 2 \ --swap-space 0 \ --gpu-memory-utilizat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: OOM during FlashInfer JIT compile of gdn_prefill_sm90 on H100 due to many concurrent cicc processes bug ### Your current environment ### 🐛 Describe the bug On an H100 (sm90a), using vLLM 0.17.1, running inference...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: OOM during FlashInfer JIT compile of gdn_prefill_sm90 on H100 due to many concurrent cicc processes bug ### Your current environment ### 🐛 Describe the bug On an H100 (sm90a), using vLLM 0.17.1, running inference...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: OOM during FlashInfer JIT compile of gdn_prefill_sm90 on H100 due to many concurrent cicc processes bug ### Your current environment ### 🐛 Describe the bug On an H100 (sm90a), using vLLM 0.17.1, running inference...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ct command used for vLLM serve** ``` CUDA_VISIBLE_DEVICES=0 \ vllm serve Qwen/Qwen3.5-2B \ --attention-backend FLASH_ATTN \ --enforce-eager \ --max-model-len 4096 \ --max-num-seqs 2 \ --swap-space 0 \ --gpu-memory-utili...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: OOM during FlashInfer JIT compile of gdn_prefill_sm90 on H100 due to many concurrent cicc processes bug ### Your current environment ### 🐛 Describe the bug On an H100 (sm90a), using vLLM 0.17.1, running inference...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
