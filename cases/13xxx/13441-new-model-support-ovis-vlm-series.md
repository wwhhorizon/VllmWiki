# vllm-project/vllm#13441: [New Model]: support Ovis VLM series

| 字段 | 值 |
| --- | --- |
| Issue | [#13441](https://github.com/vllm-project/vllm/issues/13441) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: support Ovis VLM series

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi there i can't load AIDC-AI/Ovis2-34B model https://huggingface.co/AIDC-AI/Ovis2-34B this model outperform even Qwen 2.5 VL 72B in benchmarks Currently i get this ERROR 02-17 19:45:45 engine.py:389] ValueError: Ovis has no vLLM implementation and the Transformers implementation is not compatible with vLLM. DEBUG 02-17 19:45:45 client.py:256] Shutting down MQLLMEngineClient output handler. can we add support this model, please best regards ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: support Ovis VLM series new-model ### 🚀 The feature, motivation and pitch Hi there i can't load AIDC-AI/Ovis2-34B model https://huggingface.co/AIDC-AI/Ovis2-34B this model outperform even Qwen 2.5 VL 72B in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: gface.co/AIDC-AI/Ovis2-34B this model outperform even Qwen 2.5 VL 72B in benchmarks Currently i get this ERROR 02-17 19:45:45 engine.py:389] ValueError: Ovis has no vLLM implementation and the Transformers implementatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
