# vllm-project/vllm#10039: [Bug]: PyTorch 2.5.x vLLM 1.0.0 dev issue with tensor parallel size > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#10039](https://github.com/vllm-project/vllm/issues/10039) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: PyTorch 2.5.x vLLM 1.0.0 dev issue with tensor parallel size > 1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, the latest version of vLLM with the wheels 1.0.0dev (pip install https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl) causes issues with tensor parallel size when set above 1. Task exception was never retrieved future: exception=ZMQError('Operation not supported')> Traceback (most recent call last): File "/root/miniconda3/envs/vlm3/lib/python3.10/site-packages/vllm/engine/multiprocessing/client.py", line 181, in run_output_handler_loop while await self.output_socket.poll(timeout=VLLM_RPC_TIMEOUT File "/root/miniconda3/envs/vlm3/lib/python3.10/site-packages/zmq/_future.py", line 400, in poll raise _zmq.ZMQError(_zmq.ENOTSUP) zmq.error.ZMQError: Operation not supported Task exception was never retrieved future: exception=ZMQError('Operation not supported')> Traceback (most recent call last): File "/root/miniconda3/envs/vlm3/lib/python3.10/site-packages/vllm/engine/multiprocessing/client.py", line 181, in run_output_handler_loop while await self.output_socket.poll(timeout=VLLM_RPC_TIMEOUT File "/root/miniconda3/envs/vlm3/lib/python3.10/site-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: el Input Dumps _No response_ ### 🐛 Describe the bug Hello, the latest version of vLLM with the wheels 1.0.0dev (pip install https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tensor parallel size > 1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, the latest version of vLLM with the wheels 1.0.0dev (pip install https://vllm-wheels.s3.u...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ib/python3.10/site-packages/vllm/scripts.py", line 195, in main args.dispatch_function(args) File "/root/miniconda3/envs/vlm3/lib/python3.10/site-packages/vllm/scripts.py", line 41, in serve uvloop.run(run_server(args))...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d ' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: PyTorch 2.5.x vLLM 1.0.0 dev issue with tensor parallel size > 1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, the latest version of vLLM with the wheels 1....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
