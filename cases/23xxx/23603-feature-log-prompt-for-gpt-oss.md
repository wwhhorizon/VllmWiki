# vllm-project/vllm#23603: [Feature]: Log prompt for gpt-oss

| 字段 | 值 |
| --- | --- |
| Issue | [#23603](https://github.com/vllm-project/vllm/issues/23603) |
| 状态 | closed |
| 标签 | feature request;stale;gpt-oss |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Log prompt for gpt-oss

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Right now the vllm-openai logs only show prompt_token_ids for gpt oss, so I can’t see the actual system or developer prompts. Adding Harmony decode would allow the prompts themselves to be visible in the logs, and I’d like to add that feature ### Alternatives ```diff diff --git a/vllm/vllm/entrypoints/harmony_utils.py b/vllm/vllm/entrypoints/harmony_utils.py @@ +def decode_tokens(token_ids: Iterable[int]): + return get_encoding().decode(token_ids) ``` ```diff diff --git a/vllm/vllm/entrypoints/openai/serving_chat.py b/vllm/vllm/openai/serving_chat.py @@ + from vllm.entrypoints.harmony_utils import decode_tokens def _make_request_with_harmony( self, request: ChatCompletionRequest, ): # Render prompt token ids. prompt_token_ids = render_for_completion(messages) + prompt = decode_tokens(prompt_token_ids) + prompt_dict = {"prompt": prompt, "prompt_token_ids": prompt_token_ids} engine_prompt = EngineTokensPrompt(prompt_token_ids=prompt_token_ids) # Add cache_salt if provided in the request if request.cache_salt is not None: engine_prompt["cache_salt"] = request.cache_salt - return messages, [prompt_token_ids], [engine_prompt] + return messages, [...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Log prompt for gpt-oss feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Right now the vllm-openai logs only show prompt_token_ids for gpt oss, so I can’t see the actual system or develope...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: llm/vllm/openai/serving_chat.py @@ + from vllm.entrypoints.harmony_utils import decode_tokens def _make_request_with_harmony( self, request: ChatCompletionRequest, ): # Render prompt token ids. prompt_token_ids = render...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Log prompt for gpt-oss feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Right now the vllm-openai logs only show prompt_token_ids for gpt oss, so I can’t see the actual system or develope...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
