# vllm-project/vllm#13654: [Installation]: Two CPU-only hosts installed.

| 字段 | 值 |
| --- | --- |
| Issue | [#13654](https://github.com/vllm-project/vllm/issues/13654) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Two CPU-only hosts installed.

### Issue 正文摘录

### Your current environment ```text Two AMD CPU server hosts, without GPUs. vllm=0.7.3 python=3.10.12 ``` ### How you are installing vllm ```sh Two CPU-only hosts have been set up as a Ray cluster. Using the master-slave nodes for model parallelism with vllm. An error occurred when running the command on the master node. python -m vllm.entrypoints.api_server --model /home/DeepSeek-R1-Distill-Qwen-1.5B --pipeline-parallel-size 2 --dtype float16 --device cpu INFO 02-21 14:48:25 async_llm_engine.py:211] Added request 7fa918ea16bf48778a0a0c741648f85d. ERROR 02-21 14:48:27 async_llm_engine.py:68] Engine background task failed ERROR 02-21 14:48:27 async_llm_engine.py:68] Traceback (most recent call last): ERROR 02-21 14:48:27 async_llm_engine.py:68] File "/home/vllm/lib/python3.10/site-packages/vllm-0.7.3.dev216+g4c822298.d20250219.cpu-py3.10-linux-x86_64.egg/vllm/engine/async_llm_engine.py", line 58, in _log_task_completion ERROR 02-21 14:48:27 async_llm_engine.py:68] return_value = task.result() ERROR 02-21 14:48:27 async_llm_engine.py:68] File "/home/vllm/lib/python3.10/site-packages/vllm-0.7.3.dev216+g4c822298.d20250219.cpu-py3.10-linux-x86_64.egg/vllm/engine/async_llm_engine.py",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Two CPU-only hosts installed. installation;stale ### Your current environment ```text Two AMD CPU server hosts, without GPUs. vllm=0.7.3 python=3.10.12 ``` ### How you are installing vllm ```sh Two CPU-
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: me/DeepSeek-R1-Distill-Qwen-1.5B --pipeline-parallel-size 2 --dtype float16 --device cpu INFO 02-21 14:48:25 async_llm_engine.py:211] Added request 7fa918ea16bf48778a0a0c741648f85d. ERROR 02-21 14:48:27 async_llm_engine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: set up as a Ray cluster. Using the master-slave nodes for model parallelism with vllm. An error occurred when running the command on the master node. python -m vllm.entrypoints.api_server --model /home/DeepSeek-R1-Disti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: osts have been set up as a Ray cluster. Using the master-slave nodes for model parallelism with vllm. An error occurred when running the command on the master node. python -m vllm.entrypoints.api_server --model /home/De...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: Two CPU-only hosts installed. installation;stale ### Your current environment ```text Two AMD CPU server hosts, without GPUs. vllm=0.7.3 python=3.10.12 ``` ### How you are installing vllm ```sh Two CPU-o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
