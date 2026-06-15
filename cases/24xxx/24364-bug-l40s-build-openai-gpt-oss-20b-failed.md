# vllm-project/vllm#24364: [Bug]: L40S build openai/gpt-oss-20b failed

| 字段 | 值 |
| --- | --- |
| Issue | [#24364](https://github.com/vllm-project/vllm/issues/24364) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: L40S build openai/gpt-oss-20b failed

### Issue 正文摘录

### Your current environment When loading `openai/gpt-oss-20b` model on Ada Lovelace GPUs (sm_89), the engine fails to start with: gpu: 5 L40S (maybe single is enough ) runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04 i guess cmakeList missing MARLIN_ARCHS 8.9 ### 🐛 Describe the bug vllm serve openai/gpt-oss-20b \ --dtype auto \ --max-model-len 8192 \ --enforce-eager \ --trust-remote-code failed detail: https://paste.ubuntu.com/p/XfXdYJM5kn/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vironment When loading `openai/gpt-oss-20b` model on Ada Lovelace GPUs (sm_89), the engine fails to start with: gpu: 5 L40S (maybe single is enough ) runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04 i gues...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: L40S build openai/gpt-oss-20b failed bug ### Your current environment When loading `openai/gpt-oss-20b` model on Ada Lovelace GPUs (sm_89), the engine fails to start with: gpu: 5 L40S (maybe single is enough ) ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: L40S build openai/gpt-oss-20b failed bug ### Your current environment When loading `openai/gpt-oss-20b` model on Ada Lovelace GPUs (sm_89), the engine fails to start with: gpu: 5 L40S (maybe single is enough ) ru...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: RCHS 8.9 ### 🐛 Describe the bug vllm serve openai/gpt-oss-20b \ --dtype auto \ --max-model-len 8192 \ --enforce-eager \ --trust-remote-code failed detail: https://paste.ubuntu.com/p/XfXdYJM5kn/ ### Before submitting a n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
