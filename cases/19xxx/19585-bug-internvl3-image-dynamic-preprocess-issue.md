# vllm-project/vllm#19585: [Bug]: InternVL3 image dynamic preprocess issue

| 字段 | 值 |
| --- | --- |
| Issue | [#19585](https://github.com/vllm-project/vllm/issues/19585) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: InternVL3 image dynamic preprocess issue

### Issue 正文摘录

### Your current environment v0.9.1 ### 🐛 Describe the bug original image ![Image](https://github.com/user-attachments/assets/97b24a64-07b7-4a55-9cb8-d9b575a5429a) lmdeploy serve api_server OpenGVLab/InternVL3-78B --chat-template internvl2_5 --server-port 23333 --tp 4 vllm serve OpenGVLab/InternVL3-78B --port 8000 --host 0.0.0.0 --tensor-parallel-size 4 --enforce-eager --limit-mm-per-prompt image=4,video=4 --gpu-memory-utilization 0.90 --max-model-len 8192 --trust-remote-code temperature=0.8, top_p=0.8 https://chat.intern-ai.org.cn/ ![Image](https://github.com/user-attachments/assets/f03527a4-786e-4b90-8cdd-d380d177edfa) @Isotr0py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: InternVL3 image dynamic preprocess issue bug;stale ### Your current environment v0.9.1 ### 🐛 Describe the bug original image ![Image](https://github.com/user-attachments/assets/97b24a64-07b7-4a55-9cb8-d9b575a5429...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: InternVL3 image dynamic preprocess issue bug;stale ### Your current environment v0.9.1 ### 🐛 Describe the bug original image ![Image](https://github.com/user-attachments/assets/97b24a64-07b7-4a55-9cb8-d9b575a5429...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
