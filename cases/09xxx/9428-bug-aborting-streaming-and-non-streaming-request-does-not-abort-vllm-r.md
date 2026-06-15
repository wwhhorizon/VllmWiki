# vllm-project/vllm#9428: [Bug]: aborting streaming and non-streaming request does not abort vllm request

| 字段 | 值 |
| --- | --- |
| Issue | [#9428](https://github.com/vllm-project/vllm/issues/9428) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: aborting streaming and non-streaming request does not abort vllm request

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to implement a timeout of a total stream request due to an internal proxy closing the connection before request can be completed. On the proxy, I am trying to abort the request to vllm however vllm does not seem to abort the request and continues generating. Thought it would be fixed as mentioned here however this fix #7671 has seemed to have regressed or am I implementing the abort incorrectly? Also this would be fixed if vllm had a total request length timeout param (even on streaming requests). Not sure if this exists but I could not find documentation on this. ```python client = OpenAI( base_url=openai_api_base, api_key=openai_api_key, ) models = client.models.list() model = models.data[0].id params = { "stream": True } response = client.chat.completions.create( messages=[ {"role": "user", "content": "tell me a 3000 word fantasy story"} ], model=model, **params ) try: count=0 for chunk in response: if chunk.choices[0].delta.content: print(chunk.choices[0].delta.content, end='') count = count + 1 if count > 100: response.close() response.response.close() break finally: response.close(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency You...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: aborting streaming and non-streaming request does not abort vllm request bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to implement a timeout of a total...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: es not abort vllm request bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to implement a timeout of a total stream request due to an internal proxy closing the co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
