# vllm-project/vllm#41402: [Bug]: DeepSeek-V4-Flash MTP hangs with `vllm bench serve` when concurrency > 1 on vLLM v0.20.0

| 字段 | 值 |
| --- | --- |
| Issue | [#41402](https://github.com/vllm-project/vllm/issues/41402) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V4-Flash MTP hangs with `vllm bench serve` when concurrency > 1 on vLLM v0.20.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On official vLLM v0.20.0, DeepSeek-V4-Flash with MTP (`num_speculative_tokens=2`) makes progress at serving benchmark concurrency 1, but appears to hang at concurrency 4. The benchmark remains at `0/32`; the server stays alive with 4 running requests, generation throughput drops to 0, and the engine later reports repeated `No available shared memory broadcast block found in 60 seconds` messages. This was reproduced with the official vLLM v0.20.0 installed package restored, before applying any local MTP draft-probability patches. ### Minimal reproduction This uses only vLLM's built-in random benchmark dataset, so no external dataset is required. The model weights still need to be available from Hugging Face or local cache. Terminal 1: ```bash export HF_HOME=/workspace/.hf_home export CUDA_VISIBLE_DEVICES=0,1,2,3 export VLLM_LOGGING_LEVEL=DEBUG export VLLM_TRACE_FUNCTION=1 vllm serve deepseek-ai/DeepSeek-V4-Flash \ --host 127.0.0.1 \ --port 8080 \ --served-model-name deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --tensor-parallel-size 4 \ --enable-expert-parallel \ --max-model-len 4...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ribe the bug On official vLLM v0.20.0, DeepSeek-V4-Flash with MTP (`num_speculative_tokens=2`) makes progress at serving benchmark concurrency 1, but appears to hang at concurrency 4. The benchmark remains at `0/32`; th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 20.0 bug ### Your current environment ### 🐛 Describe the bug On official vLLM v0.20.0, DeepSeek-V4-Flash with MTP (`num_speculative_tokens=2`) makes progress at serving benchmark concurrency 1, but appears to hang at co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ame deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --tensor-parallel-size 4 \ --enable-expert-parallel \ --max-model-len 4096 \ --gpu-memory-utilization 0.88 \ --speculat...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: d-model-name deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --tensor-parallel-size 4 \ --enable-expert-parallel \ --max-model-len 4096 \ --gpu-memory-utilization 0.88 \ -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ilt-in random benchmark dataset, so no external dataset is required. The model weights still need to be available from Hugging Face or local cache. Terminal 1: ```bash export HF_HOME=/workspace/.hf_home export CUDA_VISI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
