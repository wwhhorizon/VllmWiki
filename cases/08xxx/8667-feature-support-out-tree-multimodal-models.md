# vllm-project/vllm#8667: [Feature]: support out tree multimodal models

| 字段 | 值 |
| --- | --- |
| Issue | [#8667](https://github.com/vllm-project/vllm/issues/8667) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support out tree multimodal models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vllm >= 0.6 doesn't support out tree defined multimodal models: ``` rank0]: File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/llm.py", line 177, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 535, in from_engine_args [rank0]: engine_config = engine_args.create_engine_config() [rank0]: File "/usr/local/lib/python3.8/dist-packages/vllm/engine/arg_utils.py", line 792, in create_engine_config [rank0]: model_config = ModelConfig( [rank0]: File "/usr/local/lib/python3.8/dist-packages/vllm/config.py", line 230, in __init__ [rank0]: self.multimodal_config = self._init_multimodal_config( [rank0]: File "/usr/local/lib/python3.8/dist-packages/vllm/config.py", line 251, in _init_multimodal_config [rank0]: raise ValueError( [rank0]: ValueError: limit_mm_per_prompt is only supported for multimodal models. ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docume...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: support out tree multimodal models feature request ### 🚀 The feature, motivation and pitch vllm >= 0.6 doesn't support out tree defined multimodal models: ``` rank0]: File "/usr/local/lib/python3.8/dist-packa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: support out tree multimodal models feature request ### 🚀 The feature, motivation and pitch vllm >= 0.6 doesn't support out tree defined multimodal models: ``` rank0]: File "/usr/local/lib/python3.8/dist-packa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
