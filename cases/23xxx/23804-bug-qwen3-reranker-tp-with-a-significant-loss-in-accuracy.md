# vllm-project/vllm#23804: [Bug]: Qwen3-Reranker + TP, with a significant loss in accuracy.

| 字段 | 值 |
| --- | --- |
| Issue | [#23804](https://github.com/vllm-project/vllm/issues/23804) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Reranker + TP, with a significant loss in accuracy.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug By continuously increasing the tp, I found that the test performance deteriorated as tp grew larger (since I have 4 cards, the maximum setting for tp was 4). Additionally, when testing with Qwen3-reranker-0.6B, I noticed that when tp was set to 4, the memory usage of one card could reach around 10G, and the total for 4 cards was close to 40G! I'm not quite sure what caused these two abnormal results. The test results are shown in the table below (all results have a dtype of "float32"). **1.The first row in the table (Online Inference + tp1)** **2.The second row in the table (Offline Inference + TP1)** **3.The third row in the table (Online Inference + TP2)** **4.The fourth row in the table (Offline Inference + TP2)** **5.The fifth row in the table (Online Inference + TP4)** **6.The sixth row in the table (Offline Inference + TP4)** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: sults. The test results are shown in the table below (all results have a dtype of "float32"). **1.The first row in the table (Online Inference + tp1)** **2.The second row in the table (Offline Inference + TP1)** **3.The...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Qwen3-Reranker + TP, with a significant loss in accuracy. bug ### Your current environment ### 🐛 Describe the bug By continuously increasing the tp, I found that the test performance deteriorated as tp grew large...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Qwen3-Reranker + TP, with a significant loss in accuracy. bug ### Your current environment ### 🐛 Describe the bug By continuously increasing the tp, I found that the test performance deteriorated as tp grew large...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen3-Reranker + TP, with a significant loss in accuracy. bug ### Your current environment ### 🐛 Describe the bug By continuously increasing the tp, I found that the test performance deteriorated as tp grew large...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
