# vllm-project/vllm#28209: [Bug]: Engine crash when structured_outputs.grammar receives empty string

| 字段 | 值 |
| --- | --- |
| Issue | [#28209](https://github.com/vllm-project/vllm/issues/28209) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Engine crash when structured_outputs.grammar receives empty string

### Issue 正文摘录

### Your current environment - ### 🐛 Describe the bug The server crashes when a client sends an empty string in the `grammar` field within `structured_outputs` . ``` { "error": { "message": "EngineCore encountered an issue. See stack trace (above) for the root cause.", "type": "Internal Server Error", "param": null, "code": 500 } } ``` ``` (APIServer pid=1731) INFO 11-06 04:47:21 [launcher.py:42] Route: /is_scaling_elastic_ep, Methods: POST (APIServer pid=1731) INFO 11-06 04:47:21 [launcher.py:42] Route: /invocations, Methods: POST (APIServer pid=1731) INFO 11-06 04:47:21 [launcher.py:42] Route: /metrics, Methods: GET (APIServer pid=1731) INFO: Started server process [1731] (APIServer pid=1731) INFO: Waiting for application startup. (APIServer pid=1731) INFO: Application startup complete. (APIServer pid=1731) WARNING 11-06 04:48:37 [protocol.py:93] The following fields were present in the request but ignored: {'defaults'} (APIServer pid=1731) INFO 11-06 04:48:37 [chat_utils.py:560] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this. (EngineCore_DP0 pid=1996) ERROR 11-06 04:48:38 [core.py:710] EngineCore encounter...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ) INFO: Started server process [1731] (APIServer pid=1731) INFO: Waiting for application startup. (APIServer pid=1731) INFO: Application startup complete. (APIServer pid=1731) WARNING 11-06 04:48:37 [protocol.py:93] The...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: FO 11-06 04:48:37 [chat_utils.py:560] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this. (EngineCore_DP0 pid=1996) ERROR 11-06 04:48:38 [core.py:710]...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ineCore_DP0 pid=1996) ERROR 11-06 04:48:38 [core.py:710] return self.backend.compile_grammar(request_type, grammar_spec) (EngineCore_DP0 pid=1996) ERROR 11-06 04:48:38 [core.py:710] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: DP0 pid=1996) ERROR 11-06 04:48:38 [core.py:710] return self.backend.compile_grammar(request_type, grammar_spec) (EngineCore_DP0 pid=1996) ERROR 11-06 04:48:38 [core.py:710] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
