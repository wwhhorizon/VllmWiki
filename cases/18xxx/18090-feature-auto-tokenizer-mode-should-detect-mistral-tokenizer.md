# vllm-project/vllm#18090: [Feature]: Auto tokenizer mode should detect mistral tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#18090](https://github.com/vllm-project/vllm/issues/18090) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Auto tokenizer mode should detect mistral tokenizer

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The default "auto" `tokenizer_mode` should prioritize using the MistralTokenizer when the files for it are available. For a model like https://huggingface.co/mistralai/Pixtral-12B-2409 that only has the mistral format model files, it is currently required to set `--tokenizer-mode mistral` explicitly. However, both `load_format` and `config_format` are able to auto-detect / fallback to the mistral files with their default "auto" setting. There it also a warning with a strong recommendation to use `--tokenizer-mode=mistral` with mistral models [REF](https://github.com/vllm-project/vllm/blob/0b217da646fd4cc08cd0dd20d0ea69f81d64ab35/vllm/transformers_utils/tokenizer.py#L209-L217), so it would make sense to make that the default behavior with "auto". ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e using the MistralTokenizer when the files for it are available. For a model like https://huggingface.co/mistralai/Pixtral-12B-2409 that only has the mistral format model files, it is currently required to set `--token...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Auto tokenizer mode should detect mistral tokenizer feature request;stale ### 🚀 The feature, motivation and pitch The default "auto" `tokenizer_mode` should prioritize using the MistralTokenizer when the file...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: owever, both `load_format` and `config_format` are able to auto-detect / fallback to the mistral files with their default "auto" setting. There it also a warning with a strong recommendation to use `--tokenizer-mode=mis...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l files, it is currently required to set `--tokenizer-mode mistral` explicitly. However, both `load_format` and `config_format` are able to auto-detect / fallback to the mistral files with their default "auto" setting....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
