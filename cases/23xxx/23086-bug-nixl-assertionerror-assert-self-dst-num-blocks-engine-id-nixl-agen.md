# vllm-project/vllm#23086: [Bug][NIXL]: AssertionError assert self.dst_num_blocks[engine_id] == nixl_agent_meta.num_blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#23086](https://github.com/vllm-project/vllm/issues/23086) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][NIXL]: AssertionError assert self.dst_num_blocks[engine_id] == nixl_agent_meta.num_blocks

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run Qwen3-32B with PD nixl connector（tp4）, where each card has the same vram capacity. Due to vLLM's KV cache blocks memory allocation mechanism, there is a high probability that the available KV cache memory differs among ranks within the same instance, resulting in varying num_blocks per rank. This ultimately leads to an assert error (assert self.dst_num_blocks[engine_id] == nixl_agent_meta.num_blocks). see https://github.com/vllm-project/vllm/pull/19532/files , Is there any other way to solve this problem? this is calculate the free kv cache memory code: ``` @torch.inference_mode() def determine_available_memory(self) -> int: """Profiles the peak memory usage of the model to determine how much memory can be used for KV cache without OOMs. The engine will first conduct a profiling of the existing memory usage. Then, it calculate the free memory that can be used for KV cache in bytes. Tip: You may limit the usage of GPU memory by adjusting the `gpu_memory_utilization` parameter. """ torch.cuda.empty_cache() torch.cuda.reset_peak_memory_stats() GiB = lambda b: b / GiB_bytes # Execute a forward pass with dummy inputs to profile...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: assert self.dst_num_blocks[engine_id] == nixl_agent_meta.num_blocks bug;stale ### Your current environment ### 🐛 Describe the bug I run Qwen3-32B with PD nixl connector（tp4）, where each card has the same vram capacity....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: onnector（tp4）, where each card has the same vram capacity. Due to vLLM's KV cache blocks memory allocation mechanism, there is a high probability that the available KV cache memory differs among ranks within the same in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 3-32B with PD nixl connector（tp4）, where each card has the same vram capacity. Due to vLLM's KV cache blocks memory allocation mechanism, there is a high probability that the available KV cache memory differs among rank...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: me vram capacity. Due to vLLM's KV cache blocks memory allocation mechanism, there is a high probability that the available KV cache memory differs among ranks within the same instance, resulting in varying num_blocks p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug][NIXL]: AssertionError assert self.dst_num_blocks[engine_id] == nixl_agent_meta.num_blocks bug;stale ### Your current environment ### 🐛 Describe the bug I run Qwen3-32B with PD nixl connector（tp4）, where each card...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
