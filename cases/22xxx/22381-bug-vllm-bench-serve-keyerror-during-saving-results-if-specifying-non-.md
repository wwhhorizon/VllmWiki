# vllm-project/vllm#22381: [Bug]: `vllm bench serve` KeyError during saving results, if specifying non-default `--percentile-metrics`

| 字段 | 值 |
| --- | --- |
| Issue | [#22381](https://github.com/vllm-project/vllm/issues/22381) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `vllm bench serve` KeyError during saving results, if specifying non-default `--percentile-metrics`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash vllm serve Qwen/Qwen2.5-0.5B vllm bench serve \ --model Qwen/Qwen2.5-0.5B \ --percentile-metrics ttft,tpot \ --save-results ``` exception ``` File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/benchmarks/serve.py", line 1086, in main save_to_pytorch_benchmark_format(args, result_json, file_name) File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/benchmarks/serve.py", line 630, in save_to_pytorch_benchmark_format metrics={k: [results[k]] ^^^^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/benchmarks/serve.py", line 630, in metrics={k: [results[k]] ~~~~~~~^^^ KeyError: 'median_itl_ms' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Your current environment ### 🐛 Describe the bug ```bash vllm serve Qwen/Qwen2.5-0.5B vllm bench serve \ --model Qwen/Qwen2.5-0.5B \ --percentile-metrics ttft,tpot \ --save-results ``` exception ``` File "/home/ray/anaco...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ch serve \ --model Qwen/Qwen2.5-0.5B \ --percentile-metrics ttft,tpot \ --save-results ``` exception ``` File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/benchmarks/serve.py", line 1086, in main save_to_pytor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: `vllm bench serve` KeyError during saving results, if specifying non-default `--percentile-metrics` bug ### Your current environment ### 🐛 Describe the bug ```bash vllm serve Qwen/Qwen2.5-0.5B vllm bench serve \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
