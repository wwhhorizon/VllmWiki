# vllm-project/vllm#12146: [Usage]: vllm context length handling method

| 字段 | 值 |
| --- | --- |
| Issue | [#12146](https://github.com/vllm-project/vllm/issues/12146) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm context length handling method

### Issue 正文摘录

### Your current environment I am writing because I have a question during the test using vllm. I did RAG with gemma2 model using vllm in a100 40gb. We have seen here that the fragments of the document searched sometimes lead to prompts entering gemma2 going beyond the 8192 token max contextlength. But it still generates the answer. In this regard, may I know which function or method is responsible for handling max context length? ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on during the test using vllm. I did RAG with gemma2 model using vllm in a100 40gb. We have seen here that the fragments of the document searched sometimes lead to prompts entering gemma2 going beyond the 8192 token max...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing because I have a question during the test using vllm. I did RAG with gemma2 model using vllm in a100 40gb. We have seen here that the fragments of the document searched sometimes lead to prompts entering gemma2 goin...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ing because I have a question during the test using vllm. I did RAG with gemma2 model using vllm in a100 40gb. We have seen here that the fragments of the document searched sometimes lead to prompts entering gemma2 goin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm context length handling method usage;stale ### Your current environment I am writing because I have a question during the test using vllm. I did RAG with gemma2 model using vllm in a100 40gb. We have seen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: r current environment I am writing because I have a question during the test using vllm. I did RAG with gemma2 model using vllm in a100 40gb. We have seen here that the fragments of the document searched sometimes lead...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
