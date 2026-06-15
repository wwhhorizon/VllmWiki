# vllm-project/vllm#13145: [Bug]: Docker 多机多卡部署--模型启动报错

| 字段 | 值 |
| --- | --- |
| Issue | [#13145](https://github.com/vllm-project/vllm/issues/13145) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Docker 多机多卡部署--模型启动报错

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 我使用docker部署vllm并进行多机多卡的推理，结果在启动` DeepSeek-R1-Distill-Llama-70B `模型时报错。 docker： vllm/vllm-openai:v0.7.2 报错信息： ``` (RayWorkerWrapper pid=319, ip=10.68.27.14) WARNING 02-12 01:21:27 custom_all_reduce.py:136] Custom allreduce is disabled because it's not supported on more than two PCIe-only GPUs. To silence this warning, specify disable_custom_all_reduce=True explicitly. [repeated 6x across cluster] Loading safetensors checkpoint shards: 0% Completed | 0/16 [00:00 [rank0]: sys.exit(main()) [rank0]: ^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/scripts.py", line 204, in main [rank0]: args.dispatch_function(args) [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/scripts.py", line 44, in serve [rank0]: uvloop.run(run_server(args)) [rank0]: File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run [rank0]: return __asyncio.run( [rank0]: ^^^^^^^^^^^^^^ [rank0]: File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run [rank0]: return runner.run(main) [rank0]: ^^^^^^^^^^^^^^^^ [rank0]: File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run [rank0]: return self._loop.ru...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 🐛 Describe the bug 我使用docker部署vllm并进行多机多卡的推理，结果在启动` DeepSeek-R1-Distill-Llama-70B `模型时报错。 docker： vllm/vllm-openai:v0.7.2 报错信息： ``` (RayWorkerWrapper pid=319, ip=10.68.27.14) WARNING 02-12 01:21:27 custom_all_reduce.py:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Docker 多机多卡部署--模型启动报错 bug;stale ### Your current environment ### 🐛 Describe the bug 我使用docker部署vllm并进行多机多卡的推理，结果在启动` DeepSeek-R1-Distill-Llama-70B `模型时报错。 docker： vllm/vllm-openai:v0.7.2 报错信息： ``` (RayWorkerWrapp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 3.12/dist-packages/vllm/scripts.py", line 204, in main [rank0]: args.dispatch_function(args) [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/scripts.py", line 44, in serve [rank0]: uvloop.run(run_server(args...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 使用。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Docker 多机多卡部署--模型启动报错 bug;stale ### Your current environment ### 🐛 Describe the bug 我使用docker部署vllm并进行多机多卡的推理，结果在启动` DeepSeek-R1-Distill-Llama-70B `模型时报错。 docker： vllm/vllm-openai:v0.7.2 报错信息： ``` (RayWorkerWrapp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
