# vllm-project/vllm#13333: [Bug]: benchmark_serving.py with random 4k input prompt & 512 output and ignore-eos, output length only has 43 token

| 字段 | 值 |
| --- | --- |
| Issue | [#13333](https://github.com/vllm-project/vllm/issues/13333) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: benchmark_serving.py with random 4k input prompt & 512 output and ignore-eos, output length only has 43 token

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm version is v0.6.3, vllm serving is based v0.6.2 python benchmark_serving.py --model DeepSeek-R1-Distill-Qwen-32B --host 10.238.154.81 --port 8001 --dataset-name random --trust_remote_code --ignore-eos --num_prompt 1 --random-input-len 4096 --random-output-len 512 ![Image](https://github.com/user-attachments/assets/b89e72f4-6766-4bf3-aca5-9d3ddac7891f) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on is v0.6.3, vllm serving is based v0.6.2 python benchmark_serving.py --model DeepSeek-R1-Distill-Qwen-32B --host 10.238.154.81 --port 8001 --dataset-name random --trust_remote_code --ignore-eos --num_prompt 1 --random...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: benchmark_serving.py with random 4k input prompt & 512 output and ignore-eos, output length only has 43 token bug;stale ### Your current environment ### 🐛 Describe the bug vllm version is v0.6.3, vllm serving is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bug;stale ### Your current environment ### 🐛 Describe the bug vllm version is v0.6.3, vllm serving is based v0.6.2 python benchmark_serving.py --model DeepSeek-R1-Distill-Qwen-32B --host 10.238.154.81 --port 8001 --data...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1f) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: prompt & 512 output and ignore-eos, output length only has 43 token bug;stale ### Your current environment ### 🐛 Describe the bug vllm version is v0.6.3, vllm serving is based v0.6.2 python benchmark_serving.py --model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
