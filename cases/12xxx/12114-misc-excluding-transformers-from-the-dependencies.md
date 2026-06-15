# vllm-project/vllm#12114: [Misc]: Excluding `transformers` from the dependencies

| 字段 | 值 |
| --- | --- |
| Issue | [#12114](https://github.com/vllm-project/vllm/issues/12114) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Excluding `transformers` from the dependencies

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi, I would like to use the vLLM library for inference using a VLM. However, my issue are the dependencies. The `requirements-common.txt` states the [following](https://github.com/vllm-project/vllm/blob/main/requirements-common.txt#L8C1-L9C46): ``` transformers >= 4.45.2 # Required for Llama 3.2 and Qwen2-VL. tokenizers >= 0.19.1 # Required for Llama 3. ``` Taking into account the comments here, I wanted to ask, is it really possible to use a locally saved VLM that is supported by vLLM, but without depending on `transformers`? Ideally, I would also like to exclude the `tokenizers` as well, but this is not my main issue. Thanks for the great work! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t vllm. Hi, I would like to use the vLLM library for inference using a VLM. However, my issue are the dependencies. The `requirements-common.txt` states the [following](https://github.com/vllm-project/vllm/blob/main/req...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Misc]: Excluding `transformers` from the dependencies stale ### Anything you want to discuss about vllm. Hi, I would like to use the vLLM library for inference using a VLM. However, my issue are the dependencies. The `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rk! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Excluding `transformers` from the dependencies stale ### Anything you want to discuss about vllm. Hi, I would like to use the vLLM library for inference using a VLM. However, my issue are the dependencies. The `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
