# vllm-project/vllm#10847: [Bug]: benchmark random input-len inconsistent

| 字段 | 值 |
| --- | --- |
| Issue | [#10847](https://github.com/vllm-project/vllm/issues/10847) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: benchmark random input-len inconsistent

### Issue 正文摘录

### Your current environment vllm/vllm-openai:latest ### Model Input Dumps _No response_ ### 🐛 Describe the bug I test benchmark script and set the --random-input-len=8000 for Meta-Llama-3.1-8B-Instruct model，the server api shows that it gets more than 8000 input the input param ![image](https://github.com/user-attachments/assets/5c9a7624-7d3b-4693-ac01-a42453277fc8) the server log ![image](https://github.com/user-attachments/assets/1d200d7a-08ef-47fc-afa3-adcbcbe6b455) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ent bug;stale ### Your current environment vllm/vllm-openai:latest ### Model Input Dumps _No response_ ### 🐛 Describe the bug I test benchmark script and set the --random-input-len=8000 for Meta-Llama-3.1-8B-Instruct mo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: benchmark random input-len inconsistent bug;stale ### Your current environment vllm/vllm-openai:latest ### Model Input Dumps _No response_ ### 🐛 Describe the bug I test benchmark script and set the --random-input...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ![image](https://github.com/user-attachments/assets/1d200d7a-08ef-47fc-afa3-adcbcbe6b455) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 55) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: benchmark random input-len inconsistent bug;stale ### Your current environment vllm/vllm-openai:latest ### Model Input Dumps _No response_ ### 🐛 Describe the bug I test benchmark script and set the --random-input...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
