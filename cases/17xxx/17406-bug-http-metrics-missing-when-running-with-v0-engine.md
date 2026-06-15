# vllm-project/vllm#17406: [Bug]: `http*` metrics missing when running with V0 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#17406](https://github.com/vllm-project/vllm/issues/17406) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `http*` metrics missing when running with V0 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The [docs here](https://docs.vllm.ai/en/latest/design/v1/metrics.html#prometheus-client-library) state that `http_*` metrics should be available. But when I build and run `vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0` with the V0 engine from tip of main branch, these metrics aren't available. I think I've bisected the change in behavior on V0 to commit 340d7b1b217794c1b89e13936c66b920fd8d842d. On the parent commit 1bcbcbf, the `http_*` metrics are there. My `vllm serve` command falls back to V0 engine because I [built from source for CPU as described here](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html). I see `[arg_utils.py:1685] device type=cpu is not supported by the V1 Engine. Falling back to V0.` in the logs. Running `curl --silent localhost:8000/metrics | grep http` in another shell return nothing. But there are other metrics. ``` root@dxia-test-56b7668955-jlsch:/tmp/vllm# curl --silent localhost:8000/metrics | head # HELP vllm:cache_config_info Information of the LLMEngine CacheConfig # TYPE vllm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="Fa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ent-library) state that `http_*` metrics should be available. But when I build and run `vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0` with the V0 engine from tip of main branch, these metrics aren't available. I think...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: *` metrics should be available. But when I build and run `vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0` with the V0 engine from tip of main branch, these metrics aren't available. I think I've bisected the change in be...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cpu_kvcache_space_bytes="4294967296",cpu_offload_gb="0",enable_prefix_caching="None",gpu_memory_utilizati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e CacheConfig # TYPE vllm:cache_config_info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",calculate_kv_scales="False",cpu_kvcache_space_bytes="4294967296",cpu_offload_gb="0",enable_prefix_caching="None...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
