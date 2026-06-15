# vllm-project/vllm#43884: [Bug]: EngineCore crash: AssertionError in offloading_connector during update_state_after_alloc

| 字段 | 值 |
| --- | --- |
| Issue | [#43884](https://github.com/vllm-project/vllm/issues/43884) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EngineCore crash: AssertionError in offloading_connector during update_state_after_alloc

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug During normal LLM inference, vllm occasionally experiences crash with kv offloading_connector. Deployment: ``` vllm serve google/gemma-4-31B-it \ --gpu-memory-utilization 0.7 \ --speculative-config '{"model": "google/gemma-4-31B-it-assistant","num_speculative_tokens": 4,"method": "mtp"}' \ --max-num-batched-tokens 4096 \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ --tensor-parallel-size 2 \ --default-chat-template-kwargs '{"enable_thinking": false}' \ --performance-mode interactivity \ --kv-offloading-size 200 \ --kv-offloading-backend native \ --enable-prefix-caching \ --enable-prompt-tokens-details \ --enable-force-include-usage ``` No particular usage pattern is observed that will definitely trigger. Just happens randomly sometimes. (APIServer pid=1) INFO 05-27 18:56:19 metrics.py:103] KV Transfer metrics: GPU_to_CPU_total_bytes=201850880, GPU_to_CPU_total_time=0.08097408032417297, CPU_to_GPU_total_bytes=57671680, CPU_to_GPU_total_time=0.006535071849822998 (APIServer pid=1) INFO 05-27 18:56:29 loggers.py:271] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: es crash with kv offloading_connector. Deployment: ``` vllm serve google/gemma-4-31B-it \ --gpu-memory-utilization 0.7 \ --speculative-config '{"model": "google/gemma-4-31B-it-assistant","num_speculative_tokens": 4,"met...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: vllm serve google/gemma-4-31B-it \ --gpu-memory-utilization 0.7 \ --speculative-config '{"model": "google/gemma-4-31B-it-assistant","num_speculative_tokens": 4,"method": "mtp"}' \ --max-num-batched-tokens 4096 \ --enabl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cache;...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: EngineCore crash: AssertionError in offloading_connector during update_state_after_alloc bug ### Your current environment ### 🐛 Describe the bug During normal LLM inference, vllm occasionally experiences crash wi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ance-mode interactivity \ --kv-offloading-size 200 \ --kv-offloading-backend native \ --enable-prefix-caching \ --enable-prompt-tokens-details \ --enable-force-include-usage ``` No particular usage pattern is observed t...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
