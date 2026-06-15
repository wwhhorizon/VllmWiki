# vllm-project/vllm#22997: [Bug]: v1 doesn't raise an error if request priority is set while model server not using priority scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#22997](https://github.com/vllm-project/vllm/issues/22997) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v1 doesn't raise an error if request priority is set while model server not using priority scheduling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [vllm documentation](https://docs.vllm.ai/en/v0.9.1/serving/openai_compatible_server.html#extra-parameters_1) specifies: ``` Any priority other than 0 will raise an error " "if the served model does not use priority scheduling. ``` Which is the case in v0, but v1 doesn't enforce this rule [v0 async_llm_engine](https://github.com/vllm-project/vllm/blob/main/vllm/engine/async_llm_engine.py#L423-L424), [v1 async_llm](https://github.com/vllm-project/vllm/blob/main/vllm/v1/engine/async_llm.py#L227-L253). Reproduce: - Run vllm v1 with default scheduling policy (fcfs) ``` vllm serve "CohereLabs/c4ai-command-r7b-12-2024" ``` - Send a chat request with a priority parameter: ``` curl -X POST "http://localhost:8000/v1/chat/completions" -H "Content-Type: application/json" --data '{ "model": "CohereLabs/c4ai-command-r7b-12-2024", "messages": [ { "role": "user", "content": "What is the capital of France?" } ], "priority": 1 }' ``` - Expected output: value error. However the request above succeeds. If the server runs with v0 `VLLM_USE_V1=0 vllm serve "CohereLabs/c4ai-command-r7b-12-2024` we get the expected error: ``` ### Before submitting a ne...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: v1 doesn't raise an error if request priority is set while model server not using priority scheduling bug;stale ### Your current environment ### 🐛 Describe the bug [vllm documentation](https://docs.vllm.ai/en/v0....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: com/vllm-project/vllm/blob/main/vllm/v1/engine/async_llm.py#L227-L253). Reproduce: - Run vllm v1 with default scheduling policy (fcfs) ``` vllm serve "CohereLabs/c4ai-command-r7b-12-2024" ``` - Send a chat request with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: i/en/v0.9.1/serving/openai_compatible_server.html#extra-parameters_1) specifies: ``` Any priority other than 0 will raise an error " "if the served model does not use priority scheduling. ``` Which is the case in v0, bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: v1 doesn't raise an error if request priority is set while model server not using priority scheduling bug;stale ### Your current environment ### 🐛 Describe the bug [vllm documentation](https://docs.vllm.ai/en/v0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
