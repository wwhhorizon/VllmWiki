# vllm-project/vllm#7801: [Bug]: Running mistral-large results in an error related to NCCL

| 字段 | 值 |
| --- | --- |
| Issue | [#7801](https://github.com/vllm-project/vllm/issues/7801) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Running mistral-large results in an error related to NCCL

### Issue 正文摘录

### Your current environment ```tex The environment is the latest vllm-0.5.4's docker environment, and the command to run is:python3 api_server.py --port 10195 --model /data/models/Mistral-Large-Instruct-2407/ --served-model-name mistral --tensor-parallel-size 8 --max-model-len 4096 --disable-custom-all-reduce ``` ### 🐛 Describe the bug ```tex (VllmWorkerProcess pid=232) ERROR 08-23 08:25:25 multiproc_worker_utils.py:226] Exception in worker VllmWorkerProcess while processing method init_device: NCCL error: unhandled system error (run with NCCL_DEBUG=INFO for details), Traceback (most recent call last): (VllmWorkerProcess pid=232) ERROR 08-23 08:25:25 multiproc_worker_utils.py:226] File "/usr/local/lib/python3.10/dist-packages/vllm/executor/multiproc_worker_utils.py", line 223, in _run_worker_process (VllmWorkerProcess pid=232) ERROR 08-23 08:25:25 multiproc_worker_utils.py:226] output = executor(*args, **kwargs) (VllmWorkerProcess pid=232) ERROR 08-23 08:25:25 multiproc_worker_utils.py:226] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker.py", line 132, in init_device (VllmWorkerProcess pid=232) ERROR 08-23 08:25:25 multiproc_worker_utils.py:226] init_worker_distr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ironment, and the command to run is:python3 api_server.py --port 10195 --model /data/models/Mistral-Large-Instruct-2407/ --served-model-name mistral --tensor-parallel-size 8 --max-model-len 4096 --disable-custom-all-red...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r current environment ```tex The environment is the latest vllm-0.5.4's docker environment, and the command to run is:python3 api_server.py --port 10195 --model /data/models/Mistral-Large-Instruct-2407/ --served-model-n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Running mistral-large results in an error related to NCCL bug;stale ### Your current environment ```tex The environment is the latest vllm-0.5.4's docker environment, and the command to run is:python3 api_server....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: bug;stale ### Your current environment ```tex The environment is the latest vllm-0.5.4's docker environment, and the command to run is:python3 api_server.py --port 10195 --model /data/models/Mistral-Large-Instruct-2407/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
