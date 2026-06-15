# vllm-project/vllm#42340: [Bug]: Gemma 4 31B random drops in performance on H200 and B200 with 2 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#42340](https://github.com/vllm-project/vllm/issues/42340) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 31B random drops in performance on H200 and B200 with 2 GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gemma 4 seems to perform really well and then randomly will drop in t/ when running on b200 or h200 with 2 GPUs ``` vllm serve google/gemma-4-31B-it --served-model-name google/gemma-4-31B-it --kv-cache-dtype fp8 --max-model-len 200000 --dtype auto --async-scheduling --tensor-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.90 --enable-chunked-prefill --enable-auto-tool-choice --reasoning-parser gemma4 --tool-call-parser gemma4 --limit-mm-per-prompt '{"image": 2, "audio": 1}' --chat-template examples/tool_chat_template_gemma4.jinja --max-num-seqs 64 ``` using vllm v0.20.0. Issue exists in v0.19.1 and v0.20.1 Log Snippet ``` (APIServer pid=434) INFO 05-11 17:46:04 [loggers.py:271] Engine 000: Avg prompt throughput: 145.1 tokens/s, Avg generation throughput: 133.7 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.3%, Prefix cache hit rate: 89.3%, MM cache hit rate: 76.6% (APIServer pid=434) INFO: 10.129.3.35:52484 - "POST /v1/chat/completions HTTP/1.1" 200 OK (APIServer pid=434) INFO: 10.129.3.35:34950 - "GET /v1/models HTTP/1.1" 200 OK (APIServer pid=434) INFO: 10.129.3.35:34960 - "GET /v1/models HTTP/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ize 2 --trust-remote-code --gpu-memory-utilization 0.90 --enable-chunked-prefill --enable-auto-tool-choice --reasoning-parser gemma4 --tool-call-parser gemma4 --limit-mm-per-prompt '{"image": 2, "audio": 1}' --chat-temp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ogle/gemma-4-31B-it --served-model-name google/gemma-4-31B-it --kv-cache-dtype fp8 --max-model-len 200000 --dtype auto --async-scheduling --tensor-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.90 --enab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Gemma 4 31B random drops in performance on H200 and B200 with 2 GPUs bug ### Your current environment ### 🐛 Describe the bug Gemma 4 seems to perform really well and then randomly will drop in t/ when running on...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: serve google/gemma-4-31B-it --served-model-name google/gemma-4-31B-it --kv-cache-dtype fp8 --max-model-len 200000 --dtype auto --async-scheduling --tensor-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.9...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
