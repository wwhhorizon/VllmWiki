# vllm-project/vllm#5060: [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.

| 字段 | 值 |
| --- | --- |
| Issue | [#5060](https://github.com/vllm-project/vllm/issues/5060) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 46; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.

### Issue 正文摘录

### Your current environment docker image: vllm/vllm-openai:0.4.2 Model: https://huggingface.co/alpindale/c4ai-command-r-plus-GPTQ GPUs: RTX8000 * 2 ### 🐛 Describe the bug The model works fine until the following error is raised. ------------------------------------------------------- INFO 05-26 22:28:18 async_llm_engine.py:529] Received request cmpl-10dff83cb4b6422ba8c64213942a7e46: prompt: ' "Question: Is Korea the name of a Nation?\nGuideline: No explanation.\nFormat: {"Answer": " "} ', sampling_params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=['---'], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=4096, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [5, 5, 255000, 255006, 9, 60478, 33, 3294, 13489, 1690, 2773, 1719, 1671, 20611, 38, 206, 46622, 7609, 33, 3679, 33940, 21, 206, 8961, 33, 19586, 61664, 2209, 31614, 28131, 20721, 22, 3598, 11205, 37...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: stale ### Your current environment docker image: vllm/vllm-openai:0.4.2 Model: https://huggingface.co/alpindale/c4ai-command-r-plus-GPTQ GPUs: RTX8000 * 2 ### 🐛 Describe the bug The model works fine until the following...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ground loop has errored already. bug;stale ### Your current environment docker image: vllm/vllm-openai:0.4.2 Model: https://huggingface.co/alpindale/c4ai-command-r-plus-GPTQ GPUs: RTX8000 * 2 ### 🐛 Describe the bug The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2 Model: https://huggingface.co/alpindale/c4ai-command-r-plus-GPTQ GPUs: RTX8000 * 2 ### 🐛 Describe the bug The model works fine until the following error is raised. -----------------------------------------------------...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lm_engine.AsyncEngineDeadError: Background loop has errored already. bug;stale ### Your current environment docker image: vllm/vllm-openai:0.4.2 Model: https://huggingface.co/alpindale/c4ai-command-r-plus-GPTQ GPUs: RTX...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
