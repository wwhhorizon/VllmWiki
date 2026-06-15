# vllm-project/vllm#10280: [Bug]: 因vllm的版本不同，启动的qwen2.5服务，对于相同的输入；0.6.1.post2 sse输出是正确的，但 0.6.3.post1是错误的？

| 字段 | 值 |
| --- | --- |
| Issue | [#10280](https://github.com/vllm-project/vllm/issues/10280) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 因vllm的版本不同，启动的qwen2.5服务，对于相同的输入；0.6.1.post2 sse输出是正确的，但 0.6.3.post1是错误的？

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 环境： Vllm==0.6.1.post2 torch==2.4.0 Transformers==4.45.1 Accelerate==0.30.1 Tiktoken==0.7.0 startup: python -m vllm.entrypoints.openai.api_server --model ./Qwen2.5-7B-Instruct --port 8009 --enable-auto-tool-choice --tool-call-parser hermes --max-seq-len-to-capture 2048 --uvicorn-log-level warning output: 版本： 0.6.3.post1 版本：0.6.1.post2 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 因vllm的版本不同，启动的qwen2.5服务，对于相同的输入；0.6.1.post2 sse输出是正确的，但 0.6.3.post1是错误的？ bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 环境： Vllm==0.6.1.post2 torch==2.4.0 Transf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: m的版本不同，启动的qwen2.5服务，对于相同的输入；0.6.1.post2 sse输出是正确的，但 0.6.3.post1是错误的？ bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 环境： Vllm==0.6.1.post2 torch==2.4.0 Transformers==4.4...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
