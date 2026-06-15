# vllm-project/vllm#16052: [RFC]: Extending VLLM towards native support of non text-generating models

| 字段 | 值 |
| --- | --- |
| Issue | [#16052](https://github.com/vllm-project/vllm/issues/16052) |
| 状态 | closed |
| 标签 | RFC;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Extending VLLM towards native support of non text-generating models

### Issue 正文摘录

### Motivation. This RFC proposes a set of changes for better supporting non text-generating models, ultimately making vLLM the engine of preference for multimodal input/output models. Also, the target for this is the v1 engine. This is a followup from a previous RFC [#11065](https://github.com/vllm-project/vllm/issues/11065) ,that led to the merging of `PrithviGeospatialMAE` model that by piggybacking the embedding model interface, it's the first model in vLLM that generates (raw) images instead of text. In a nutshell I want to start the discussion about proper support for models that generate output in various modalities. Specifically, the proposed changes would target: - vLLM interface and serving API - Generation of output data that is not text - Processing of models' input ### Proposed Change. ## vLLM interface and main loop The current vLLM entrypoit/interface LLM/LLMEngine/AsyncLLMEngine is clearly targeting language model: 1) a prompt (text/tokens) is always expected, while multi-modal data are optional; 2) the main engine assumes auto-regressive text generation. Supporting non text-generating models means enabling users on passing the input type required by their models,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: Extending VLLM towards native support of non text-generating models RFC;unstale ### Motivation. This RFC proposes a set of changes for better supporting non text-generating models, ultimately making vLLM the engi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: xtending VLLM towards native support of non text-generating models RFC;unstale ### Motivation. This RFC proposes a set of changes for better supporting non text-generating models, ultimately making vLLM the engine of pr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ishes when we run out of patches. This is an iterative process like auto-regression, but we know beforehand how many times to run inference on the model. I would like this behavior to be triggered starting from the inpu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: roper support for models that generate output in various modalities. Specifically, the proposed changes would target: - vLLM interface and serving API - Generation of output data that is not text - Processing of models'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
