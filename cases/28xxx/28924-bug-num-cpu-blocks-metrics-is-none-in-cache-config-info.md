# vllm-project/vllm#28924: [Bug]: num_cpu_blocks metrics is None in cache_config_info

| 字段 | 值 |
| --- | --- |
| Issue | [#28924](https://github.com/vllm-project/vllm/issues/28924) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: num_cpu_blocks metrics is None in cache_config_info

### Issue 正文摘录

### Your current environment env: vllm == 0.11.0 Enable CPU offloading implemented by #19854 with argument `kv-transfer-config '{"kv_connector":"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_config":{"num_cpu_blocks":41000}}'` ### 🐛 Describe the bug When querying `/metrics`, the `num_cpu_blocks` is always None ``` # TYPE vllm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cpu_kvcache_space_bytes="None",cpu_offload_gb="0.0",enable_prefix_caching="True",engine="0",gpu_memory_utilization="0.65",is_attention_free="False",kv_cache_memory_bytes="None",kv_sharing_fast_prefill="False",mamba_cache_dtype="auto",mamba_page_size_padded="None",mamba_ssm_cache_dtype="auto",num_cpu_blocks="None",num_gpu_blocks="9271",num_gpu_blocks_override="None",prefix_caching_hash_algo="sha256",sliding_window="None",swap_space="0.0",swap_space_bytes="0.0"} 1.0 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: num_cpu_blocks metrics is None in cache_config_info bug;stale ### Your current environment env: vllm == 0.11.0 Enable CPU offloading implemented by #19854 with argument `kv-transfer-config '{"kv_connector":"Offlo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cpu_kvcache_space_bytes="None",cpu_offload_gb="0.0",enable_prefix_caching="True",engine="0",gpu_memory_ut...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ll="False",mamba_cache_dtype="auto",mamba_page_size_padded="None",mamba_ssm_cache_dtype="auto",num_cpu_blocks="None",num_gpu_blocks="9271",num_gpu_blocks_override="None",prefix_caching_hash_algo="sha256",sliding_window=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: num_cpu_blocks metrics is None in cache_config_info bug;stale ### Your current environment env: vllm == 0.11.0 Enable CPU offloading implemented by #19854 with argument `kv-transfer-config '{"kv_connector":"Offlo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: bug;stale ### Your current environment env: vllm == 0.11.0 Enable CPU offloading implemented by #19854 with argument `kv-transfer-config '{"kv_connector":"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
