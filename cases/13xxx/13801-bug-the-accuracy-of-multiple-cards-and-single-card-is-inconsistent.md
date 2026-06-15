# vllm-project/vllm#13801: [Bug]: The accuracy of multiple cards and single card is inconsistent

| 字段 | 值 |
| --- | --- |
| Issue | [#13801](https://github.com/vllm-project/vllm/issues/13801) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The accuracy of multiple cards and single card is inconsistent

### Issue 正文摘录

### Your current environment vllm 0.7.1 torch 2.5.1 transformers 4.48.3 ### 🐛 Describe the bug I find the accuracy is inconsistent when I use tensor-parallel-size=2 compare with tensor-parallel-size=1 the commands are as follows: CUDA_VISIBLE_DEVICES=5 python -m vllm.entrypoints.openai.api_server --model ./ --port 7863 --tensor-parallel-size=1 CUDA_VISIBLE_DEVICES=5,6 python -m vllm.entrypoints.openai.api_server --model ./ --port 7863 --tensor-parallel-size=2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: size=2 compare with tensor-parallel-size=1 the commands are as follows: CUDA_VISIBLE_DEVICES=5 python -m vllm.entrypoints.openai.api_server --model ./ --port 7863 --tensor-parallel-size=1 CUDA_VISIBLE_DEVICES=5,6 python...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: The accuracy of multiple cards and single card is inconsistent bug;stale ### Your current environment vllm 0.7.1 torch 2.5.1 transformers 4.48.3 ### 🐛 Describe the bug I find the accuracy is inconsistent when I u...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: The accuracy of multiple cards and single card is inconsistent bug;stale ### Your current environment vllm 0.7.1 torch 2.5.1 transformers 4.48.3 ### 🐛 Describe the bug I find the accuracy is inconsistent when I u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: : CUDA_VISIBLE_DEVICES=5 python -m vllm.entrypoints.openai.api_server --model ./ --port 7863 --tensor-parallel-size=1 CUDA_VISIBLE_DEVICES=5,6 python -m vllm.entrypoints.openai.api_server --model ./ --port 7863 --tensor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Bug]: The accuracy of multiple cards and single card is inconsistent bug;stale ### Your current environment vllm 0.7.1 torch 2.5.1 transformers 4.48.3 ### 🐛 Describe the bug I find the accuracy is inconsistent when I us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
