# vllm-project/vllm#9502: [Bug]: Phi-2 context extension does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#9502](https://github.com/vllm-project/vllm/issues/9502) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Phi-2 context extension does not work

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I evaluated my context-extended Phi-2 model (context size 32k instead of 2k, RoPE theta 500k instead of 10k), it produced garbage for input longer than 2k tokens. For input less than 2k tokens everything worked fine and it also worked fine if I ran inference using transformers. I found the error here: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/phi.py#L105 I changed ``` rope_theta = 10000 max_position_embeddings = getattr(config, "n_positions", 2048) ``` to ``` rope_theta = getattr(config, "rope_theta", 10000.0) max_position_embeddings = getattr(config, "max_position_embeddings", 2048) ``` which fixed the issue and produced the expected results. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: context extension does not work bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I evaluated my context-extended Phi-2 model (context size 32k instead of 2k, RoPE theta 50...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I evaluated my context-extended Phi-2 model (context size 32k instead of 2k, RoPE theta 500k instead of 10k), it produced garbage for input longer than 2k...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
