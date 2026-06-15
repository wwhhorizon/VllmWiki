# vllm-project/vllm#17889: [Bug]: Qwen/QwQ-32B crashed，but sglang work good!  occurs an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#17889](https://github.com/vllm-project/vllm/issues/17889) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen/QwQ-32B crashed，but sglang work good!  occurs an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When we do a High-Concurrency Stress Testing, ​CUDA error: an illegal memory access was encountered, Compile with TORCH_USE_CUDA_DSA to enable device-side assertions. But, I have try this work below: ​ --- 1. Suspected OOM (Out of Memory) error due to insufficient GPU VRAM When switching to 8 GPUs with all other configurations unchanged, the system still crashed under high load. 2. Suspected model-specific instability Tested with a 14B parameter model under identical conditions, and no crashes occurred. 3. Verified with equivalent-sized alternative model Switched to DeepSeek-R1-Distill-32B (same parameter count as the original model) with unchanged configurations, and the system remained stable. 4. Suspected vLLM version (v0.7.3) bug Upgraded to vLLM v0.8.5.post1, but crashes persisted under the same test conditions. 5. Input pattern dependency identified Changed test data to continuous story generation prompts (e.g., "Write me a story"), and no crashes were observed. 6. Framework version compatibility fix **Resolved crashes by running QWQ-32B with sglang v0.4.6.post2-cu124 under identical parameters.** **But sglang work well, th...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: tress Testing, ​CUDA error: an illegal memory access was encountered, Compile with TORCH_USE_CUDA_DSA to enable device-side assertions. But, I have try this work below: ​ --- 1. Suspected OOM (Out of Memory) error due t...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: e-side assertions. But, I have try this work below: ​ --- 1. Suspected OOM (Out of Memory) error due to insufficient GPU VRAM When switching to 8 GPUs with all other configurations unchanged, the system still crashed un...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen/QwQ-32B crashed，but sglang work good! occurs an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug When we do a High-Concurrency Stress Testing, ​CUDA error:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: t sglang work good! occurs an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug When we do a High-Concurrency Stress Testing, ​CUDA error: an illegal memory access was e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: --gpu-memory-utilization - "0.9" - --guided-decoding-backend - outlines - --kv-cache-dtype - auto - --load-format - auto - --max-logprobs - "20" - --max-model-len - "8192" -

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 0x94ac3 (0x7f237cee3ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #4: clone + 0x44 (0x7f237cf74bf4 in /usr/lib/x86_64-linux-gnu/libc.so.6) ``` ### before submitting a new issu… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f233202c61d in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0x145c0 (0x7f237c6985c0 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorc… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
