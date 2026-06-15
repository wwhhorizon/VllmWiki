# vllm-project/vllm#23436: [Bug]: There are no CI tests for chunked prefill for pooling models.

| 字段 | 值 |
| --- | --- |
| Issue | [#23436](https://github.com/vllm-project/vllm/issues/23436) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: There are no CI tests for chunked prefill for pooling models.

### Issue 正文摘录

### 🐛 Describe the bug There are decoder embedding models with "last" pooling such as `BAAI/bge-multilingual-gemma2`. These models can run with prefix caching and chunked prefill. The lack of tests caused PR https://github.com/vllm-project/vllm/pull/19912 to be merged without checking for this case causing issues https://github.com/vllm-project/vllm/issues/23381 and https://github.com/vllm-project/vllm/issues/23223 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: There are no CI tests for chunked prefill for pooling models. bug ### 🐛 Describe the bug There are decoder embedding models with "last" pooling such as `BAAI/bge-multilingual-gemma2`. These models can run with pr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: There are no CI tests for chunked prefill for pooling models. bug ### 🐛 Describe the bug There are decoder embedding models with "last" pooling such as `BAAI/bge-multilingual-gemma2`. These models can run with pr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: There are no CI tests for chunked prefill for pooling models. bug ### 🐛 Describe the bug There are decoder embedding models with "last" pooling such as `BAAI/bge-multilingual-gemma2`. These models can run with pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 223 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: oder embedding models with "last" pooling such as `BAAI/bge-multilingual-gemma2`. These models can run with prefix caching and chunked prefill. The lack of tests caused PR https://github.com/vllm-project/vllm/pull/19912...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
