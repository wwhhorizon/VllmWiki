# vllm-project/vllm#7895: [Usage]: Does vLLM support prefix decoder / causal mask with prefix? 

| 字段 | 值 |
| --- | --- |
| Issue | [#7895](https://github.com/vllm-project/vllm/issues/7895) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vLLM support prefix decoder / causal mask with prefix? 

### Issue 正文摘录

### Your current environment ```text vLLM Version: 0.5.4@4db5176d9758b720b05460c50ace3c01026eb158 ``` ### How would you like to use vllm ![image](https://github.com/user-attachments/assets/aa642e06-95f0-4360-8029-67c8aef9f182) To my understanding, vLLM has supported "Causal Decoder" and "Encoder-Decoder". Does vLLM support prefix decoder? How can I add a prefix decoder model into vLLM? I want to run inference of a Text-To-Speech LLM [VALL-E](https://arxiv.org/abs/2301.02111), which input is text and outputs audio in an auto-regressive manner. I don't know how to implement non-causal (bidirectional) self-attentsion in vLLM. Any help is appreciated. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ask with prefix? usage;stale ### Your current environment ```text vLLM Version: 0.5.4@4db5176d9758b720b05460c50ace3c01026eb158 ``` ### How would you like to use vllm ![image](https://github.com/user-attachments/assets/a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Does vLLM support prefix decoder / causal mask with prefix? usage;stale ### Your current environment ```text vLLM Version: 0.5.4@4db5176d9758b720b05460c50ace3c01026eb158 ``` ### How would you like to use vllm !...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: coder". Does vLLM support prefix decoder? How can I add a prefix decoder model into vLLM? I want to run inference of a Text-To-Speech LLM [VALL-E](https://arxiv.org/abs/2301.02111), which input is text and outputs audio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
