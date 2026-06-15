# vllm-project/vllm#8844: [Bug]: Assertion Error when inferencing with sample_n>1and occur preemption

| 字段 | 值 |
| --- | --- |
| Issue | [#8844](https://github.com/vllm-project/vllm/issues/8844) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Assertion Error when inferencing with sample_n>1and occur preemption

### Issue 正文摘录

### Your current environment The newest vllm 0.6.2 docker image without any change (released on 9.26) ### Model Input Dumps _No response_ ### 🐛 Describe the bug ![1](https://github.com/user-attachments/assets/8c51786b-407b-4bec-afba-b12b1986e193) ![2](https://github.com/user-attachments/assets/21e88013-1879-4fea-aeb2-e3c9a1c69c1a) ![3](https://github.com/user-attachments/assets/1be83d61-8732-40f6-a2d3-f59138880bd1) ![4](https://github.com/user-attachments/assets/5b42ad38-b664-4495-976b-888f9db64954) ![6](https://github.com/user-attachments/assets/c6b90e58-9587-41b2-ae65-1eaee9d71aa2) I use recompute method to deal with preemption, when the sample_n parameter=1, it works well.But when I increase the parameter to 3,5 or 10, such error will occur.Could you please help me solve the bug? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Assertion Error when inferencing with sample_n>1and occur preemption bug;stale ### Your current environment The newest vllm 0.6.2 docker image without any change (released on 9.26) ### Model Input Dumps _No respo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ug? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ewest vllm 0.6.2 docker image without any change (released on 9.26) ### Model Input Dumps _No response_ ### 🐛 Describe the bug ![1](https://github.com/user-attachments/assets/8c51786b-407b-4bec-afba-b12b1986e193) ![2](h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Assertion Error when inferencing with sample_n>1and occur preemption bug;stale ### Your current environment The newest vllm 0.6.2 docker image without any change (released on 9.26) ### Model Input Dumps _No response_ ##...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
