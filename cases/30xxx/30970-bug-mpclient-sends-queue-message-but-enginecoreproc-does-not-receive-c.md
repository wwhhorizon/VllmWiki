# vllm-project/vllm#30970: [Bug]:  MPClient sends queue message but EngineCoreProc does not receive, causing timeout.

| 字段 | 值 |
| --- | --- |
| Issue | [#30970](https://github.com/vllm-project/vllm/issues/30970) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  MPClient sends queue message but EngineCoreProc does not receive, causing timeout.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text We have discovered that the communication from AsyncMPClient to EngineCoreProc is established through ZMQ queue messages. However, in practical applications, due to network issues, overload conditions, etc., queue messages may risk being lost. This scenario cannot be consistently reproduced in the testing environment. Therefore, I have simulated this situation using code. In such cases, vllm may not have a retry mechanism and will not exhibit any exceptions. While everything appears normal within vllm, the application end will wait indefinitely until a timeout occurs. ``` ## Here is what will happen after I simulate queue message loss in the AsyncMPClient of v1/core_client:： ```text def _send_input_message( self, message: tuple[bytestr, ...], engine: EngineIdentity, objects: Any ) -> Awaitable[Any]: """ objects is a reference to retain until zmq is finished with the buffers, in case they were extracted from tensors in the request. """ # Simulate message loss if isinstance(objects, EngineCoreRequest): # Message directly "lost" to simulate send failure # Create an immediately completed future to simulate the illusion of "su...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: MPClient sends queue message but EngineCoreProc does not receive, causing timeout. bug ### Your current environment ### 🐛 Describe the bug ```text We have discovered that the communication from AsyncMPClient to E...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: o simulate the illusion of "successful sending" future = asyncio.Future() future.set_result(None) # Make the client think the send succeeded return future self.ensure_alive() self.free_pending_messages() msg = (engine,)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: s situation using code. In such cases, vllm may not have a retry mechanism and will not exhibit any exceptions. While everything appears normal within vllm, the application end will wait indefinitely until a timeout occ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: FO 12-18 22:46:39 [chat_utils.py:574] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this. (APIServer pid=23427) INFO: 127.0.0.1:47868 - "POST /v1/chat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
