# vllm-project/vllm#38470: [Bug]: When using the Sonnet dataset for benchmark testing, if the input length is too small, the CPU usage becomes abnormally high with no error logs, making it impossible to run the benchmark properly.

| 字段 | 值 |
| --- | --- |
| Issue | [#38470](https://github.com/vllm-project/vllm/issues/38470) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using the Sonnet dataset for benchmark testing, if the input length is too small, the CPU usage becomes abnormally high with no error logs, making it impossible to run the benchmark properly.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the Sonnet dataset for benchmark testing, if the input length is around 200 or less, the CPU usage becomes abnormally high with no error logs, and the benchmark cannot be started properly. such as : vllm bench serve \ --backend vllm \ --model Qwen/Qwen2-VL-7B-Instruct \ --dataset-name sonnet \ --dataset-path benchmarks/sonnet_4x.txt \ --sonnet-input-len 220 \ --sonnet-output-len 500 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ing the Sonnet dataset for benchmark testing, if the input length is too small, the CPU usage becomes abnormally high with no error logs, making it impossible to run the benchmark properly. bug ### Your current environm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: arted properly. such as : vllm bench serve \ --backend vllm \ --model Qwen/Qwen2-VL-7B-Instruct \ --dataset-name sonnet \ --dataset-path benchmarks/sonnet_4x.txt \ --sonnet-input-len 220 \ --sonnet-output-len 500 ### Be...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: When using the Sonnet dataset for benchmark testing, if the input length is too small, the CPU usage becomes abnormally high with no error logs, making it impossible to run the benchmark properly. bug ### Your cu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: enchmark cannot be started properly. such as : vllm bench serve \ --backend vllm \ --model Qwen/Qwen2-VL-7B-Instruct \ --dataset-name sonnet \ --dataset-path benchmarks/sonnet_4x.txt \ --sonnet-input-len 220 \ --sonnet-...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
