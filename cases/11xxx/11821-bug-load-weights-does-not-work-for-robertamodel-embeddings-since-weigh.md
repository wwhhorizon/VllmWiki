# vllm-project/vllm#11821: [Bug]: load_weights() does not work for RobertaModel embeddings since weights start with "roberta."

| 字段 | 值 |
| --- | --- |
| Issue | [#11821](https://github.com/vllm-project/vllm/issues/11821) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: load_weights() does not work for RobertaModel embeddings since weights start with "roberta."

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The RobertaEmbeddingModel here: https://github.com/vllm-project/vllm/blob/a4e2b268568b335d8fe37f8eaaa894cec3ba9397/vllm/model_executor/models/roberta.py#L151 just uses the base BertModel() class, so when model.load_weights() is called the param names don't match, leading to this stack trace: File "/home/ray/anaconda3/lib/python3.10/site-packages/vllm/model_executor/models/bert.py", line 448, in load_weights self.model.load_weights(weights) File "/home/ray/anaconda3/lib/python3.10/site-packages/vllm/model_executor/models/bert.py", line 394, in load_weights param = params_dict[name] KeyError: 'roberta.embeddings.LayerNorm.weight' I think it should be renaming the weights to remove the "roberta." bit similar to https://github.com/vllm-project/vllm/blob/a4e2b268568b335d8fe37f8eaaa894cec3ba9397/vllm/model_executor/models/roberta.py#L186 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 186 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: load_weights() does not work for RobertaModel embeddings since weights start with "roberta." bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The RobertaEmbeddingModel h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
