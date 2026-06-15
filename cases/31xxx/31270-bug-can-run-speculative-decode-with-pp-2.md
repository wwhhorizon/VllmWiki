# vllm-project/vllm#31270: [Bug]: Can run  Speculative decode with PP >2?

| 字段 | 值 |
| --- | --- |
| Issue | [#31270](https://github.com/vllm-project/vllm/issues/31270) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can run  Speculative decode with PP >2?

### Issue 正文摘录

### Your current environment vllm:0.12.0 ### 🐛 Describe the bug I run vllm:0.12.0 with start args like this: `python3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8080 --dtype bfloat16 --model /Qwen3-32B \ --pipeline-parallel-size 2 \ --gpu-memory-utilization 0.9 --max-model-len 32768 --max-num-batched-tokens 5120 \ --trust-remote-code --no-enable-prefix-caching \ --speculative_config '{"method": "ngram","num_speculative_tokens": 10,"prompt_lookup_max": 4, "enforce_eager": "True"}'` The server can start, but when use the interface of '/chat/completion', the vllm server will crash. ### Before submitting a new issue... - [ ] #31271

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: on3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8080 --dtype bfloat16 --model /Qwen3-32B \ --pipeline-parallel-size 2 \ --gpu-memory-utilization 0.9 --max-model-len 32768 --max-num-batched-tokens 5120...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: points.openai.api_server \ --host 0.0.0.0 --port 8080 --dtype bfloat16 --model /Qwen3-32B \ --pipeline-parallel-size 2 \ --gpu-memory-utilization 0.9 --max-model-len 32768 --max-num-batched-tokens 5120 \ --trust-remote-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Can run Speculative decode with PP >2? bug;stale ### Your current environment vllm:0.12.0 ### 🐛 Describe the bug I run vllm:0.12.0 with start args like this: `python3 -m vllm.entrypoints.openai.api_server \ --hos...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
