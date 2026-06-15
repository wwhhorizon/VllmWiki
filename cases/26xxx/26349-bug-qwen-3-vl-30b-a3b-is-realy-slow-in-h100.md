# vllm-project/vllm#26349: [Bug]: Qwen-3-VL-30B-A3B... is realy slow.. in H100

| 字段 | 值 |
| --- | --- |
| Issue | [#26349](https://github.com/vllm-project/vllm/issues/26349) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen-3-VL-30B-A3B... is realy slow.. in H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.92 \ --max-num-seqs 128 \ --max-num-batched-tokens 16384 \ --limit-mm-per-prompt '{"image":3, "video":5}' \ --max-model-len 32768 \ --logprobs-mode processed_logprobs \ --host 0.0.0.0 \ --port 8002 \ 2>&1 | tee logs/vllm_$(date +%Y%m%d_%H%M%S).log ``` APIServer pid=19189) INFO 10-06 11:23:16 [chat_utils.py:560] Detected the chat template content format to be 'openai'. You can set `--chat-template-content-format` to override this. (APIServer pid=19189) INFO: 100.64.0.25:53030 - "POST /v1/chat/completions HTTP/1.1" 200 OK (APIServer pid=19189) INFO 10-06 11:23:31 [loggers.py:127] Engine 000: Avg prompt throughput: 474.7 tokens/s, Avg generation throughput: 9.8 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% (APIServer pid=19189) INFO: 100.64.0.29:54866 - "POST /v1/chat/completions HTTP/1.1" 200 OK (APIServer pid=19189) INFO 10-06 11:23:41 [loggers.py:127] Engine 000: Avg prompt throughput: 475.9 tokens/s, Avg generation throughput: 7.5 tokens/s, Running: 0 reqs, W...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Qwen-3-VL-30B-A3B... is realy slow.. in H100 bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --gpu-memor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cache;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 🐛 Describe the bug ``` vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.92 \ --max-num-seqs 128 \ --max-num-batched-tokens 16384 \ --limit-mm-per-promp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen-3-VL-30B-A3B... is realy slow.. in H100 bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --gpu-memor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen-3-VL-30B-A3B... is realy slow.. in H100 bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --gpu-me

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
