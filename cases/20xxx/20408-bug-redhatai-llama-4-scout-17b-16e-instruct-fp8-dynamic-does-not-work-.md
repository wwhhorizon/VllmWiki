# vllm-project/vllm#20408: [Bug]: RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic does not work with VLLM_ALL2ALL_BACKEND="deepep_high_throughput"

| 字段 | 值 |
| --- | --- |
| Issue | [#20408](https://github.com/vllm-project/vllm/issues/20408) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic does not work with VLLM_ALL2ALL_BACKEND="deepep_high_throughput"

### Issue 正文摘录

### Your current environment [env.txt](https://github.com/user-attachments/files/21028197/env.txt) ### 🐛 Describe the bug The scout model doesn't seem to be working with the DeepEP HT backend. ``` #!/bin/bash export VLLM_ALL2ALL_BACKEND="deepep_high_throughput" PORT=9011 MODEL="RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic" echo "lm_eval --model local-completions --tasks gsm8k --model_args model=${MODEL},base_url=http://127.0.0.1:${PORT}/v1/completions,num_concurrent=1,max_retries=3,tokenized_requests=False --limit 100" vllm serve ${MODEL} --trust-remote-code --port ${PORT} --enforce-eager --data-parallel-size 4 --tensor-parallel-size 1 --enable-expert-parallel --max-model-len 8192 ``` cc @tlrmchlsmth , @varun-sundar-rabindranath ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: nstruct-FP8-dynamic does not work with VLLM_ALL2ALL_BACKEND="deepep_high_throughput" bug;stale ### Your current environment [env.txt](https://github.com/user-attachments/files/21028197/env.txt) ### 🐛 Describe the bug Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -Instruct-FP8-dynamic" echo "lm_eval --model local-completions --tasks gsm8k --model_args model=${MODEL},base_url=http://127.0.0.1:${PORT}/v1/completions,num_concurrent=1,max_retries=3,tokenized_requests=False --limit 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic does not work with VLLM_ALL2ALL_BACKEND="deepep_high_throughput" bug;stale ### Your current environment [env.txt](https://github.com/user-attachments/files/2102...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: mic does not work with VLLM_ALL2ALL_BACKEND="deepep_high_throughput" bug;stale ### Your current environment [env.txt](https://github.com/user-attachments/files/21028197/env.txt) ### 🐛 Describe the bug The scout model do...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ama-4-Scout-17B-16E-Instruct-FP8-dynamic does not work with VLLM_ALL2ALL_BACKEND="deepep_high_throughput" bug;stale ### Your current environment [env.txt](https://github.com/user-attachments/files/21028197/env.txt) ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
