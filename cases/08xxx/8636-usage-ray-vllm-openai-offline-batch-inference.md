# vllm-project/vllm#8636: [Usage]: Ray + vLLM OpenAI (offline) Batch Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#8636](https://github.com/vllm-project/vllm/issues/8636) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Ray + vLLM OpenAI (offline) Batch Inference

### Issue 正文摘录

### Your current environment None ### How would you like to use vllm I want to use the OpenAI library to do offline batch inference leveraging Ray (for scaling and scheduling) on top of vLLM. Context: The plan is to built a FastAPI service that closely mimicks OpenAI's batch API and allows to process a larger number of prompts (tens of thousands) in 24h. There are a few options of achieving this with vLLM but every one has some important drawback, but maybe I am missing something: - There is an existing guide that uses the `LLMClass` [in the docs](https://docs.vllm.ai/en/latest/getting_started/examples/offline_inference_distributed.html) with Ray. While the `LLMClass` shares the OpenAI [sampling parameters](https://docs.vllm.ai/en/v0.5.2/dev/offline_inference/llm.html), it does lack the important OpenAI prompt templating. - The `run_batch.py` entrypoint that was introduced [here](https://github.com/vllm-project/vllm/issues/8567) would be the simplest one. But it does not support Ray out of the box. - The third option would be to use the `AsyncLLMEngine` as done [here](https://github.com/vllm-project/vllm/issues/7904) and bundle it with [OpenAIServingChat](https://github.com/vllm-p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ere are a few options of achieving this with vLLM but every one has some important drawback, but maybe I am missing something: - There is an existing guide that uses the `LLMClass` [in the docs](https://docs.vllm.ai/en/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ty! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: serve/tutorials/vllm-example.html). But this would lack the OpenAI batch format and is – again – async. Maybe this helps other people as well. Would be super grateful for some feedback. 🙂 And thanks a ton for this very...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: g guide that uses the `LLMClass` [in the docs](https://docs.vllm.ai/en/latest/getting_started/examples/offline_inference_distributed.html) with Ray. While the `LLMClass` shares the OpenAI [sampling parameters](https://d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
