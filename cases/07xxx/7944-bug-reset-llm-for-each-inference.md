# vllm-project/vllm#7944: [Bug]:reset LLM for each inference

| 字段 | 值 |
| --- | --- |
| Issue | [#7944](https://github.com/vllm-project/vllm/issues/7944) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:reset LLM for each inference

### Issue 正文摘录

### Your current environment vllm 0.5.4 pytorch 2.4.0+cu121 ### 🐛 Describe the bug Hello, I am using the LLM for offline line inference. I have two models that share the same lower layers but different upper layers. So typically it has two different CUDA graphs. However, every time when I tried to inference on the first model and then run the inference on the second model. They continue to give the results for the first model. Is anyway that I can reset and run the second model successfully? I have tried enforce-eager and torch.cuda.empty_cache(). Thank you ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: wer layers but different upper layers. So typically it has two different CUDA graphs. However, every time when I tried to inference on the first model and then run the inference on the second model. They continue to giv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: bug Hello, I am using the LLM for offline line inference. I have two models that share the same lower layers but different upper layers. So typically it has two different CUDA graphs. However, every time when I tried to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
