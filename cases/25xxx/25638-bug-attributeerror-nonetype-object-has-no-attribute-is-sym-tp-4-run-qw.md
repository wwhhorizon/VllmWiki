# vllm-project/vllm#25638: [Bug]: AttributeError: 'NoneType' object has no attribute 'is_sym' -tp 4 run Qwen3-Next-80B-A3B-Instruct-int4-AutoRound

| 字段 | 值 |
| --- | --- |
| Issue | [#25638](https://github.com/vllm-project/vllm/issues/25638) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'NoneType' object has no attribute 'is_sym' -tp 4 run Qwen3-Next-80B-A3B-Instruct-int4-AutoRound

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm 0.10.2版本四卡-tp 4运行fp16模型都正常，双卡-tp 2运行量化模型也正常。但是四卡-tp 4运行量化模型报错：AttributeError: 'NoneType' object has no attribute 'is_sym'。 运行的参数：vllm serve /gpt/models/Intel/Qwen3-Next-80B-A3B-Instruct-int4-AutoRound -tp 4 --served-model-name AI-models --api-key ldy168168 --gpu-memory-utilization 0.95 --max-model-len 128068 --max-num-seqs 3 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ]: AttributeError: 'NoneType' object has no attribute 'is_sym' -tp 4 run Qwen3-Next-80B-A3B-Instruct-int4-AutoRound bug;stale ### Your current environment ### 🐛 Describe the bug vllm 0.10.2版本四卡-tp 4运行fp16模型都正常，双卡-tp 2运行...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ' object has no attribute 'is_sym' -tp 4 run Qwen3-Next-80B-A3B-Instruct-int4-AutoRound bug;stale ### Your current environment ### 🐛 Describe the bug vllm 0.10.2版本四卡-tp 4运行fp16模型都正常，双卡-tp 2运行量化模型也正常。但是四卡-tp 4运行量化模型报错：At...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s 3 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ribute 'is_sym' -tp 4 run Qwen3-Next-80B-A3B-Instruct-int4-AutoRound bug;stale ### Your current environment ### 🐛 Describe the bug vllm 0.10.2版本四卡-tp 4运行fp16模型都正常，双卡-tp 2运行量化模型也正常。但是四卡-tp 4运行量化模型报错：AttributeError: 'None...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
