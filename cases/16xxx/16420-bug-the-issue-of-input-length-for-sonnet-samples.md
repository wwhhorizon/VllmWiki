# vllm-project/vllm#16420: [Bug]:The issue of input length for Sonnet samples

| 字段 | 值 |
| --- | --- |
| Issue | [#16420](https://github.com/vllm-project/vllm/issues/16420) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:The issue of input length for Sonnet samples

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug python3 benchmarks/benchmark_serving.py --backend vllm --model Qwen/Qwen2.5-7B-Instruct --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --request-rate 512 --num-prompts 128 --port 8090 --sonnet-input-len 1024 --sonnet-output-len 1024 --sonnet-prefix-len 100 prompt_len of produced samples greater then sonnet-input-len which causes: ERROR 04-07 12:31:21 serving_completion.py:110] File "/root/vllm-fork/vllm/entrypoints/openai/serving_engine.py", line 239, in _validate_input ERROR 04-07 12:31:21 serving_completion.py:110] raise ValueError( ERROR 04-07 12:31:21 serving_completion.py:110] ValueError: This model's maximum context length is 2048 tokens. However, you requested 2054 tokens (1030 in the messages, 1024 in the completion). Please reduce the length of the messages or completion. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: scribe the bug python3 benchmarks/benchmark_serving.py --backend vllm --model Qwen/Qwen2.5-7B-Instruct --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --request-rate 512 --num-prompts 128 --port 8090 --sonnet...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: les bug ### Your current environment ### 🐛 Describe the bug python3 benchmarks/benchmark_serving.py --backend vllm --model Qwen/Qwen2.5-7B-Instruct --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --request-ra...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nt ### 🐛 Describe the bug python3 benchmarks/benchmark_serving.py --backend vllm --model Qwen/Qwen2.5-7B-Instruct --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --request-rate 512 --num-prompts 128 --port 80...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 7B-Instruct --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --request-rate 512 --num-prompts 128 --port 8090 --sonnet-input-len 1024 --sonnet-output-len 1024 --sonnet-prefix-len 100 prompt_len of produced sam...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
