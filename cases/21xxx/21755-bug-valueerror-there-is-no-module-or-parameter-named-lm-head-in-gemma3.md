# vllm-project/vllm#21755: [Bug]: ValueError: There is no module or parameter named 'lm_head' in Gemma3nForConditionalGeneration

| 字段 | 值 |
| --- | --- |
| Issue | [#21755](https://github.com/vllm-project/vllm/issues/21755) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: There is no module or parameter named 'lm_head' in Gemma3nForConditionalGeneration

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have fine-tuned gemma3n-e4b-it model on my own dataset using https://github.com/huggingface/trl Now I want to run checkpoint using vLLM and I got the next message `ValueError: There is no module or parameter named 'lm_head' in Gemma3nForConditionalGeneration` vLLM Version is 0.10.0 python Version is 3.10 transformers Version is 4.54.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ValueError: There is no module or parameter named 'lm_head' in Gemma3nForConditionalGeneration bug;stale ### Your current environment ### 🐛 Describe the bug I have fine-tuned gemma3n-e4b-it model on my own datase...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e or parameter named 'lm_head' in Gemma3nForConditionalGeneration` vLLM Version is 0.10.0 python Version is 3.10 transformers Version is 4.54.0 ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 4.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: ValueError: There is no module or parameter named 'lm_head' in Gemma3nForConditionalGeneration bug;stale ### Your current environment ### 🐛 Describe the bug I have fine-tuned gemma3n-e4b-it model on my own datase...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: dule or parameter named 'lm_head' in Gemma3nForConditionalGeneration bug;stale ### Your current environment ### 🐛 Describe the bug I have fine-tuned gemma3n-e4b-it model on my own dataset using https://github.com/huggin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
