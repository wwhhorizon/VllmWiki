# vllm-project/vllm#25697: [Bug][gpt-oss] streaming/tools RuntimeError: Attempted to exit cancel scope in a different task than it was entered in

| 字段 | 值 |
| --- | --- |
| Issue | [#25697](https://github.com/vllm-project/vllm/issues/25697) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][gpt-oss] streaming/tools RuntimeError: Attempted to exit cancel scope in a different task than it was entered in

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We're working on supporting streaming for ResponsesAPI for GPT-OSS. I've noticed that with tool calling recently integrated to GPTOSS for streaming (#23386, #23927), when I run the following I've noticed we are not cleaning up our context properly. I think the issue is related to: - in serving_responses, we create an asyncContextManager https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/serving_responses.py#L465 - this then initializes tool_sessions here: https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/context.py#L349 - but when we exit, we don't clean up the tool sessions properly (maybe we enter 2 contexts but exit in the wrong order/clean up all of them in the inner context so the outer context returns this error) I'm looking into mak PR to fix it, but wanted to share this bug with the general community / if anyone has ideas for this. Thoughts - I don't get this error in the non stream mode - If the client is not making a request with tools, we probably shouldn't initialize tool sessions at all? Some related issues https://github.com/modelcontextprotocol/python-sdk/issues/79 https://github.c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 52f07e/smart/inference_platform_sp/llm_predictor_gpu/__service__/service#link-tree/anyio/streams/memory.py:183: ResourceWarning: Unclosed warnings.warn( ResourceWarning: Enable tracemalloc to get the object allocation t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: set() /data/users/axia/fbsource/buck-out/v2/gen/fbcode/cc651496ec52f07e/smart/inference_platform_sp/llm_predictor_gpu/__service__/service#link-tree/anyio/streams/memory.py:183: ResourceWarning: Unclosed warnings.warn( R...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: pted to exit cancel scope in a different task than it was entered in bug;stale ### Your current environment ### 🐛 Describe the bug We're working on supporting streaming for ResponsesAPI for GPT-OSS. I've noticed that wi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rence_platform_sp/llm_predictor_gpu/__service__/service#link-tree/anyio/_backends/_asyncio.py", line 773, in __aexit__ if self.cancel_scope.__exit__(type(exc), exc, exc.__traceback__): File "/data/users/axia/fbsource/bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug][gpt-oss] streaming/tools RuntimeError: Attempted to exit cancel scope in a different task than it was entered in bug;stale ### Your current environment ### 🐛 Describe the bug We're working on supporting streaming...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
