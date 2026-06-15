# vllm-project/vllm#9538: [Bug]: vllm failing on tpu v5litepod-8

| 字段 | 值 |
| --- | --- |
| Issue | [#9538](https://github.com/vllm-project/vllm/issues/9538) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm failing on tpu v5litepod-8

### Issue 正文摘录

### Your current environment collect_env.py doesn't report any gpu information on tpu nodes. ### Model Input Dumps . ### 🐛 Describe the bug When I build and run the docker container according to the [vllm tpu guide](https://docs.vllm.ai/en/latest/getting_started/tpu-installation.html) I get the following error: ``` ERROR 10-21 02:38:59 worker_base.py:464] requests.exceptions.ConnectionError: HTTPConnectionPool(host='metadata.google.internal', port=80): Max retries exceeded with url: /computeMetadata/v1/instance/attributes/tpu-env (Caused by NewConnectionError(' : Failed to establish a new connection: [Errno 111] Connection refused')) Process SpawnProcess-1: Traceback (most recent call last): File "/usr/local/lib/python3.10/site-packages/urllib3/connection.py", line 199, in _new_conn sock = connection.create_connection( File "/usr/local/lib/python3.10/site-packages/urllib3/util/connection.py", line 85, in create_connection raise err File "/usr/local/lib/python3.10/site-packages/urllib3/util/connection.py", line 73, in create_connection sock.connect(sa) ConnectionRefusedError: [Errno 111] Connection refused The above exception was the direct cause of the following exception: Traceba...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ug ### Your current environment collect_env.py doesn't report any gpu information on tpu nodes. ### Model Input Dumps . ### 🐛 Describe the bug When I build and run the docker container according to the [vllm tpu guide](...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: on tpu nodes. ### Model Input Dumps . ### 🐛 Describe the bug When I build and run the docker container according to the [vllm tpu guide](https://docs.vllm.ai/en/latest/getting_started/tpu-installation.html) I get the fo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: I get the following error: ``` ERROR 10-21 02:38:59 worker_base.py:464] requests.exceptions.ConnectionError: HTTPConnectionPool(host='metadata.google.internal', port=80): Max retries exceeded with url: /computeMetadata/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: , head_size, scale, num_kv_heads, File "/workspace/vllm/vllm/attention/backends/pallas.py", line 122, in __init__ if torch_xla.tpu.version() : Failed to establish a new connection: [Errno 111] Connection refused')) ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: py", line 85, in __init__ self.impl = impl_cls(num_heads, head_size, scale, num_kv_heads, File "/workspace/vllm/vllm/attention/backends/pallas.py", line 122, in __init__ if torch_xla.tpu.version() : Failed to establish...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
