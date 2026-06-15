# vllm-project/vllm#13093: [Bug]: ray distributed inference - Current node has no GPU available error

| 字段 | 值 |
| --- | --- |
| Issue | [#13093](https://github.com/vllm-project/vllm/issues/13093) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ray distributed inference - Current node has no GPU available error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Following [the distributed serving guideline](https://docs.vllm.ai/en/latest/serving/distributed_serving.html), I have run a 2 H100 node ray cluster and vllm model server on top of it. While the ray cluster setup following `run_cluster.sh` looks green: ```log ======== Autoscaler status: 2025-02-11 20:50:28.351629 ======== Node status --------------------------------------------------------------- Active: 1 node_9ea7e32dcda1451e97e40ba9bf8b5e9cfd3068425b0c46ff8bf41a50 1 node_4914066c82a54bfeb0b2c8b73e5a081e02f9d7724d73463e93d3a2de Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/128.0 CPU 0.0/16.0 GPU 0B/1.78TiB memory 0B/124.0GiB object_store_memory ``` vLLM ray job consistently fails with the following error: ```log 2025-02-11 21:35:17,102 INFO worker.py:1654 -- Connecting to existing Ray cluster at address: 123.45.67.1:6379... 2025-02-11 21:35:17,114 INFO worker.py:1832 -- Connected to Ray cluster. View the dashboard at 127.0.0.1:8265 2025-02-11 21:35:17,531 INFO worker.py:1654 -- Connecting to existing Ray cluster at address: 123.45....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ntrypoints/openai/api_server.py", line 875, in run_server async with build_async_engine_client(args) as engine_client: File "/usr/bin/python3/contextlib.py", line 199, in __aenter__ return await anext(self.gen) File "/h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: docs.vllm.ai/en/latest/serving/distributed_serving.html), I have run a 2 H100 node ray cluster and vllm model server on top of it. While the ray cluster setup following `run_cluster.sh` looks green: ```log ======== Auto...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ib/python3.10/site-packages/vllm/scripts.py", line 204, in main args.dispatch_function(args) File "/home/jovyan/venvs/vllm-hgpu/lib/python3.10/site-packages/vllm/scripts.py", line 44, in serve uvloop.run(run_server(args...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: distributed_serving.html), I have run a 2 H100 node ray cluster and vllm model server on top of it. While the ray cluster setup following `run_cluster.sh` looks green: ```log ======== Autoscaler status: 2025-02-11 20:50...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: uster setup following `run_cluster.sh` looks green: ```log ======== Autoscaler status: 2025-02-11 20:50:28.351629 ======== Node status --------------------------------------------------------------- Active: 1 node_9ea7e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
