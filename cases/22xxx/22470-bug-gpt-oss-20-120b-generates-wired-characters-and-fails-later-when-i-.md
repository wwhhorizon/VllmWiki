# vllm-project/vllm#22470: [Bug]: gpt oss 20/120b generates wired characters and fails later when i use them

| 字段 | 值 |
| --- | --- |
| Issue | [#22470](https://github.com/vllm-project/vllm/issues/22470) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt oss 20/120b generates wired characters and fails later when i use them

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The vllm / model add strange characters in the response content. In the reasoning part, there are no characters like this. When i add the content to the messages in the next request - the server (sometime) returns error 400 ```Python headers = {"Host": f"localhost:5000", "Accept-Encoding": "deflate", "Accept-charset": "utf-8", "Connection": "keep-alive", "Accept": "application/json", "Content-Type":"application/json" } payload = { "messages": [ { "content": """Given the objective and plan and the status so far: The objective is: There was a robbery in Jorden 17, Paris, France at May 10 2024 14:30 . Please use all the knowledge you have and find the suspects. """, "name": "supervisor", "role": "user" } ], "model": "openai/gpt-oss-20b", "stream": False, "temperature": 0.0 } response = requests.post(url=f"http://localhost:5000/v1/chat/completions", headers=headers,json=payload) print(response.json()) ``` '{ "model": "openai/gpt-oss-20b", "choices": [{"index": 0, "message": {"role": "assistant", "content": "I\\u2019m sorry, but I don\\u2019t have any real\\u2011world data on a robbery that took place at Jorden\\u202f17 in Paris on 10...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: sue in the model itself - but maybe it in the vllm template. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s 20/120b generates wired characters and fails later when i use them bug;stale ### Your current environment ### 🐛 Describe the bug The vllm / model add strange characters in the response content. In the reasoning part,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: stale ### Your current environment ### 🐛 Describe the bug The vllm / model add strange characters in the response content. In the reasoning part, there are no characters like this. When i add the content to the messages...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
