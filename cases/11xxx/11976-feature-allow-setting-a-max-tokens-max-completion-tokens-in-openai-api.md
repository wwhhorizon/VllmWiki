# vllm-project/vllm#11976: [Feature]: Allow setting a max_tokens (max_completion_tokens in OpenAI API) for all requests.

| 字段 | 值 |
| --- | --- |
| Issue | [#11976](https://github.com/vllm-project/vllm/issues/11976) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow setting a max_tokens (max_completion_tokens in OpenAI API) for all requests.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm running vLLM for production LLM hosting and would like to cap the max_tokens (total number of generated output tokens) for all requests. Currently when using the OpenAI API server, the [default_max_tokens](https://github.com/vllm-project/vllm/blob/9597a095f2c02670b44f5973635ce4b9852e8eab/vllm/entrypoints/openai/serving_chat.py#L190) is calculated to be the context_window - prompt tokens. However, for models like Llama-3.1 which has a context window of 128K, this far too large. ### Alternatives One potential solution would allow having `max_new_tokens` be specified in the generation_config.json file that would be read at launch time. This could then become the server's `max_tokens`. Currently, only repetition_penalty, temperature, top_k, top_p, and min_p seem to be [supported](https://github.com/vllm-project/vllm/blob/9597a095f2c02670b44f5973635ce4b9852e8eab/vllm/config.py#L898) The code in [openai/serving_completion](https://github.com/vllm-project/vllm/blob/9597a095f2c02670b44f5973635ce4b9852e8eab/vllm/entrypoints/openai/serving_completion.py#L118) would need to take into account that you want the minimum of the (max_model_len-prompt_to...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 0) is calculated to be the context_window - prompt tokens. However, for models like Llama-3.1 which has a context window of 128K, this far too large. ### Alternatives One potential solution would allow having `max_new_t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: atives One potential solution would allow having `max_new_tokens` be specified in the generation_config.json file that would be read at launch time. This could then become the server's `max_tokens`. Currently, only repe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Allow setting a max_tokens (max_completion_tokens in OpenAI API) for all requests. good first issue;feature request ### 🚀 The feature, motivation and pitch I'm running vLLM for production LLM hosting and would like to c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
