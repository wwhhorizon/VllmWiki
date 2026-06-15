# vllm-project/vllm#21661: [Bug]: RuntimeError: NCCL error: unhandled cuda error

| 字段 | 值 |
| --- | --- |
| Issue | [#21661](https://github.com/vllm-project/vllm/issues/21661) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: NCCL error: unhandled cuda error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I encountered this error while trying to deploy https://huggingface.co/Intel/Qwen3-235B-A22B-Thinking-2507-int4-mixed-AutoRound ``` The deployment failed to start 3 times in a row. This may be due to a problem with its constructor or initial health check failing. See controller logs for details. Error: [36mray::ServeReplica:Qwen3 235B A22B Thinking:vLLMGenericAPI.initialize_and_get_metadata()[39m (pid=2729922, ip=159.103.253.238, actor_id=665657fc491efe6840b6a01201000000, repr= ) File "/usr/lib64/python3.11/concurrent/futures/_base.py", line 456, in result return self.__get_result() ^^^^^^^^^^^^^^^^^^^ File "/usr/lib64/python3.11/concurrent/futures/_base.py", line 401, in __get_result raise self._exception ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/ray/serve/_private/replica.py", line 1001, in initialize_and_get_metadata await self._replica_impl.initialize(deployment_config) File "/ray/serve/_private/replica.py", line 720, in initialize raise RuntimeError(traceback.format_exc()) from None RuntimeError: Traceback (most recent call last): File "/ray/serve/_private/replica.py", line 698, in initialize await self._user_callable_w...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: escribe the bug I encountered this error while trying to deploy https://huggingface.co/Intel/Qwen3-235B-A22B-Thinking-2507-int4-mixed-AutoRound ``` The deployment failed to start 3 times in a row. This may be due to a p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization cuda;operator;quantization;triton build_error;crash dtype;e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ing to deploy https://huggingface.co/Intel/Qwen3-235B-A22B-Thinking-2507-int4-mixed-AutoRound ``` The deployment failed to start 3 times in a row. This may be due to a problem with its constructor or initial health chec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: RuntimeError: NCCL error: unhandled cuda error bug;stale ### Your current environment ### 🐛 Describe the bug I encountered this error while trying to deploy https://huggingface.co/Intel/Qwen3-235B-A22B-Thinking-2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: i;hardware_porting;model_support;quantization cuda;operator;quantization;triton build_error;crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
