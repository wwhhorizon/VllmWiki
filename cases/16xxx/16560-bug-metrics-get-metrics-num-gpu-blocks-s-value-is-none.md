# vllm-project/vllm#16560: [Bug]: metrics: get metrics num_gpu_blocks's value is none.

| 字段 | 值 |
| --- | --- |
| Issue | [#16560](https://github.com/vllm-project/vllm/issues/16560) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: metrics: get metrics num_gpu_blocks's value is none.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` curl http://127.0.0.1:8000/metrics ...... # HELP vllm:cache_config_info Information of the LLMEngine CacheConfig # TYPE vllm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cpu_offload_gb="0",enable_prefix_caching="True",gpu_memory_utilization="0.85",is_attention_free="False",num_cpu_blocks="None", num_gpu_blocks="None", num_gpu_blocks_override="None",prefix_caching_hash_algo="builtin",sliding_window="None",swap_space_bytes="4294967296"} 1.0 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cpu_offload_gb="0",enable_prefix_caching="True",gpu_memory_utilization="0.85",is_attention_free="False",n...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: metrics: get metrics num_gpu_blocks's value is none. bug ### Your current environment ### 🐛 Describe the bug ``` curl http://127.0.0.1:8000/metrics ...... # HELP vllm:cache_config_info Information of the LLMEngin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the bug ``` curl http://127.0.0.1:8000/metrics ...... # HELP vllm:cache_config_info Information of the LLMEngine CacheConfig # TYPE vllm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: _info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cpu_offload_gb="0",enable_prefix_caching="True",gpu_memory_utilization="0.85",is_attention_free="False",num_cpu_blocks="None", num_gpu_blocks="None",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
