# vllm-project/vllm#13956: [Bug]: vllm multi-card deployment DeepSeek-R1- Distill-Qwen-32B-quantized.w4a16 error

| 字段 | 值 |
| --- | --- |
| Issue | [#13956](https://github.com/vllm-project/vllm/issues/13956) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm multi-card deployment DeepSeek-R1- Distill-Qwen-32B-quantized.w4a16 error

### Issue 正文摘录

### Your current environment Task exception was never retrieved [0/1799] future: exception=ZMQError('Operation not supported')> File "/opt/conda/lib/python3.11/site-packages/zmq/_future.py", line 372, in poll raise _zmq.ZMQError(_zmq.ENOTSUP) zmq.error.ZMQError: Operation not supported Task exception was never retrieved future: exception=ZMQError('Operation not supported')> Traceback (most recent call last): File "/opt/conda/lib/python3.11/site-packages/vllm/engine/multiprocessing/client.py", line 184, in run_output_handler_loop while await self.output_socket.poll(timeout=VLLM_RPC_TIMEOUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/site-packages/zmq/_future.py", line 372, in poll raise _zmq.ZMQError(_zmq.ENOTSUP) zmq.error.ZMQError: Operation not supported Task exception was never retrieved future: exception=ZMQError('Operation not supported')> Traceback (most recent call last): File "/opt/conda/lib/python3.11/site-packages/vllm/engine/multiprocessing/client.py", line 184, in run_output_handler_loop while await self.output_socket.poll(timeout=VLLM_RPC_TIMEOUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/site-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ) ^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/lib/python3.11/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: vllm multi-card deployment DeepSeek-R1- Distill-Qwen-32B-quantized.w4a16 error bug ### Your current environment Task exception was never retrieved
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm multi-card deployment DeepSeek-R1- Distill-Qwen-32B-quantized.w4a16 error bug ### Your current environment Task exception was never retrieved
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ib/python3.11/site-packages/vllm/scripts.py", line 201, in main args.dispatch_function(args) File "/opt/conda/lib/python3.11/site-packages/vllm/scripts.py", line 42, in serve uvloop.run(run_server(args)) File "/opt/cond...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 024 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
