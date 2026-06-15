# vllm-project/vllm#20092: [Doc]: error in retrieval_augmented_generation_with_langchain.py

| 字段 | 值 |
| --- | --- |
| Issue | [#20092](https://github.com/vllm-project/vllm/issues/20092) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: error in retrieval_augmented_generation_with_langchain.py

### Issue 正文摘录

### 📚 The doc issue Hello, I've encountered an error after running the example of RAG with langchain: ``` raise MilvusException( pymilvus.exceptions.MilvusException: ``` ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Doc]: error in retrieval_augmented_generation_with_langchain.py documentation ### 📚 The doc issue Hello, I've encountered an error after running the example of RAG with langchain: ``` raise MilvusException( pymilvus.ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
