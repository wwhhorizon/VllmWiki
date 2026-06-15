# vllm-project/vllm#17923: [Bug]: engine core initialization

| 字段 | 值 |
| --- | --- |
| Issue | [#17923](https://github.com/vllm-project/vllm/issues/17923) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: engine core initialization

### Issue 正文摘录

### Your current environment Hello! I have tried pretty much all the fixes mentioned in the github repo from setting V1 to 0 to patching the fix for the multiproc_proces.py file. I am still not able to resolve this issue. If I set v1 engine as 0, i run into client socket issues, otherwise its a constant core initlisation issue. I am using 8x100s GPUs and for Qwen 2.5-VL-32B model. I am unsure on what to do. ### 🐛 Describe the bug ``` Engine core initialization failed and AttributeError: 'MultiprocExecutor' object has no attribute 'workers' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e its a constant core initlisation issue. I am using 8x100s GPUs and for Qwen 2.5-VL-32B model. I am unsure on what to do. ### 🐛 Describe the bug ``` Engine core initialization failed and AttributeError: 'MultiprocExecu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: engine core initialization bug;stale ### Your current environment Hello! I have tried pretty much all the fixes mentioned in the github repo from setting V1 to 0 to patching the fix for the multiproc_proces.py fi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
