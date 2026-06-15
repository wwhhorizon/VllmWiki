# vllm-project/vllm#20284: [Bug]: vLLM Crashes When Using N-gram Speculative Decoding with LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#20284](https://github.com/vllm-project/vllm/issues/20284) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM Crashes When Using N-gram Speculative Decoding with LoRA

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When enabling both LoRA and ngram speculative decoding, vLLM starts and works correctly, but crashes when processing more than one concurrent request. Setup: ```python llm = LLM( model="meta-llama/Llama-2-7b-hf", enable_lora=True, speculative_config={ "method": "ngram", "num_speculative_tokens": 5, "prompt_lookup_max": 4, } ) ``` The full traceback of the exception: ``` File "/usr/local/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__ raise exc File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__ await self.app(scope, receive, _send) File "/usr/local/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__ await self.app(scope, receive, send) File "/usr/local/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sing more than one concurrent request. Setup: ```python llm = LLM( model="meta-llama/Llama-2-7b-hf", enable_lora=True, speculative_config={ "method": "ngram", "num_speculative_tokens": 5, "prompt_lookup_max": 4, } ) ```...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vLLM Crashes When Using N-gram Speculative Decoding with LoRA bug;stale ### Your current environment ### 🐛 Describe the bug When enabling both LoRA and ngram speculative decoding, vLLM starts and works correctly,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ceive, sender) File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/site-packages/starlette/routing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
