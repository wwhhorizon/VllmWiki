# vllm-project/vllm#40435: [Bug]: v0.19.1 CUDA illegal memory access with --kv-cache-dtype fp8 + EP + EAGLE3 under concurrent load (Kimi-K2.5) - distinct from #40259

| 字段 | 值 |
| --- | --- |
| Issue | [#40435](https://github.com/vllm-project/vllm/issues/40435) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;gemm;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.19.1 CUDA illegal memory access with --kv-cache-dtype fp8 + EP + EAGLE3 under concurrent load (Kimi-K2.5) - distinct from #40259

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Bug Description When running Kimi-K2.5 with `--kv-cache-dtype fp8`, vLLM crashes with `CUDA error: an illegal memory access was encountered` **under concurrent request load** (20 concurrent requests). **Critical finding**: Removing `--kv-cache-dtype fp8` (using default `auto`) results in **100% success rate** (120/120 requests) under identical load, while with fp8 only ~25-56% succeed. This confirms a specific FP8 quantization bug, **distinct from #40259**. ### Environment - vLLM version: v0.19.1 (docker: vllm/vllm-openai:v0.19.1) - Hardware: 8× NVIDIA H20-3e (141GB) - Model: moonshot-ai/Kimi-K2.5 - Draft model: moonshot-ai/Kimi-K2.5-Eagle3 (EAGLE3 speculative decoding) ### Reproduction Commands **Server (failing case with fp8):** ```bash docker run --rm -it \ --gpus all \ --ipc=host \ --ulimit memlock=-1 \ --ulimit stack=67108864 \ -p 8000:8000 \ -v /ssd1:/model_files \ --shm-size=150gb \ vllm/vllm-openai:v0.19.1 \ --model /model_files/Kimi-K2.5 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --enable-ep-weight-filter \ --compilation-config '{"pass_config": {"fuse_allreduce_rms": true}}' \ --kv-cache-dtype fp8 \ --sp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: identical load, while with fp8 only ~25-56% succeed. This confirms a specific FP8 quantization bug, **distinct from #40259**. ### Environment - vLLM version: v0.19.1 (docker: vllm/vllm-openai:v0.19.1) - Hardware: 8× NVI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: CUDA error: an illegal memory access was encountered` **under concurrent request load** (20 concurrent requests). **Critical finding**: Removing `--kv-cache-dtype fp8` (using default `auto`) results in **100% success ra...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: v0.19.1 CUDA illegal memory access with --kv-cache-dtype fp8 + EP + EAGLE3 under concurrent load (Kimi-K2.5) - distinct from #40259 bug ### Your current environment ### 🐛 Describe the bug ### Bug Description When...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: v0.19.1 CUDA illegal memory access with --kv-cache-dtype fp8 + EP + EAGLE3 under concurrent load (Kimi-K2.5) - distinct from #40259 bug ### Your current environment ### 🐛 Describe the bug ### Bug Description When...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: /layers/attention/mla_attention.py", line 1733, in build common_attn_metadata.compute_num_computed_tokens().cpu() torch.AcceleratorError: CUDA error: an illegal memory access was encountered ``` ### Key Findings 1. **10...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
