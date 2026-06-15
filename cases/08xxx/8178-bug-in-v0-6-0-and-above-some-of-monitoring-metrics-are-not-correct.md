# vllm-project/vllm#8178: [Bug]: In v0.6.0 and above, Some of monitoring metrics are not correct.

| 字段 | 值 |
| --- | --- |
| Issue | [#8178](https://github.com/vllm-project/vllm/issues/8178) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In v0.6.0 and above, Some of monitoring metrics are not correct.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` - args: - --model - /data/models/llama-65b-instruct - --tensor-parallel-size - "4" - --load-format - "auto" - --max-model-len - "8192" - --block-size - "32" - --gpu-memory-utilization - "0.95" - --num-scheduler-steps - "16" - --enable-prefix-caching - --uvicorn-log-level - warning - --disable-log-requests image: vllm/vllm-openai:v0.6.0 ``` If I call /metrics in v0.6.0, only the following metrics exist. ``` Information - vllm:cache_config_info Histogram - vllm:time_to_first_token_seconds - vllm:time_per_output_token_seconds Counter - vllm:num_preemptions_total - vllm:prompt_tokens_total - vllm:generation_tokens_total Gauge - vllm:num_requests_running - vllm:num_requests_swapped - vllm:num_requests_waiting - vllm:gpu_cache_usage_perc - vllm:cpu_cache_usage_perc - vllm:cpu_prefix_cache_hit_rate - vllm:gpu_prefix_cache_hit_rate - vllm:avg_prompt_throughput_toks_per_s - vllm:avg_generation_throughput_toks_per_s ``` **Other important metrics that were visible in v0.5.5 have disappeared, except for the ones shown above.** ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the cha...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: g]: In v0.6.0 and above, Some of monitoring metrics are not correct. bug;stale ### Your current environment ### 🐛 Describe the bug ``` - args: - --model - /data/models/llama-65b-instruct - --tensor-parallel-size - "4" -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: put_toks_per_s - vllm:avg_generation_throughput_toks_per_s ``` **Other important metrics that were visible in v0.5.5 have disappeared, except for the ones shown above.** ### Before submitting a new issue... - [X] Make s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ur current environment ### 🐛 Describe the bug ``` - args: - --model - /data/models/llama-65b-instruct - --tensor-parallel-size - "4" - --load-format - "auto" - --max-model-len - "8192" - --block-size - "32" - --gpu-memo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .** ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: d-format - "auto" - --max-model-len - "8192" - --block-size - "32" - --gpu-memory-utilization - "0.95" - --num-scheduler-steps - "16" - --enable-prefix-caching - --uvicorn-log-level - warning - --disable-log-request

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
