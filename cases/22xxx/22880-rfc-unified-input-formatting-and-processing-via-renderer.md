# vllm-project/vllm#22880: [RFC]: Unified Input Formatting and Processing via `Renderer`

| 字段 | 值 |
| --- | --- |
| Issue | [#22880](https://github.com/vllm-project/vllm/issues/22880) |
| 状态 | closed |
| 标签 | RFC;keep-open;multi-modality |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Unified Input Formatting and Processing via `Renderer`

### Issue 正文摘录

### Motivation. vLLM’s current input processing pipeline has grown complex and fragmented. Tokenization, chat template formatting, and multimodal input handling are scattered across multiple components (e.g. `Processor`, `InputPreprocessor`, `MultiModalContentParser`, etc). For online serving, prompt formatting, media fetching and tokenzation take place at the API server layer whereas multimodal input processing happens inside `AsyncLLM`. This requires handling of different input type combinations and therefore introduced unnecessary complexity. Another issue of the current processing logic is that it's tightly coupled with Hugging Face `tokenizers`/`transformers`, therefore makes it non-trivial for model developers to support custom models on vLLM. As vLLM shifts its focus to be more model developer friendly and easy to hack upon, this refactoring effort aims to reduce these layers of abstraction and level of fragmentation, as well as to make it easier for model providers to plug in custom input handling implementations not based on Hugging Face `tokenizers`/`transformers`. ### Proposed Change. In this joint proposal by @WoosukKwon @DarkLight1337 @huachenheli and me, we propose a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Unified Input Formatting and Processing via `Renderer` RFC;keep-open;multi-modality ### Motivation. vLLM’s current input processing pipeline has grown complex and fragmented. Tokenization, chat template formattin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: eatures**, and `AsyncLLM` deals with **tokens-in-tokens-out**. Another important benefit of this separation is that `Renderer`'s implementation does not have to be based on Hugging Face Transformers (or even Python) as...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: OpenAI-style” JSON spec) into token ids, multimodal features and related metadata to be directly consumed by `EngineCore`, which means all of input preparation is handled in one place. By moving these steps out of `Asyn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ssor`. Renderer’s responsibility is to format and convert high-level API requests (in “OpenAI-style” JSON spec) into token ids, multimodal features and related metadata to be directly consumed by `EngineCore`, which mea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
