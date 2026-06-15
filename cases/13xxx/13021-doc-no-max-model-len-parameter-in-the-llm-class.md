# vllm-project/vllm#13021: [Doc]: No max_model_len parameter in the LLM class

| 字段 | 值 |
| --- | --- |
| Issue | [#13021](https://github.com/vllm-project/vllm/issues/13021) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: No max_model_len parameter in the LLM class

### Issue 正文摘录

### 📚 The doc issue In this url: https://docs.vllm.ai/en/latest/serving/offline_inference.html I see that there is no max_model_len parameter in the LLM class, but the documentation still says llm = LLM(model="adept/fuyu-8b", max_model_len=2048, max_num_seqs=2) Btw, I wonder how can I change the max_seq_len when I use offline_inference? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Doc]: No max_model_len parameter in the LLM class documentation ### 📚 The doc issue In this url: https://docs.vllm.ai/en/latest/serving/offline_inference.html I see that there is no max_model_len parameter in the LLM c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ocumentation ### 📚 The doc issue In this url: https://docs.vllm.ai/en/latest/serving/offline_inference.html I see that there is no max_model_len parameter in the LLM class, but the documentation still says llm = LLM(mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
