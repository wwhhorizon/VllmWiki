# vllm-project/vllm#1025: ray failed to register worker

| 字段 | 值 |
| --- | --- |
| Issue | [#1025](https://github.com/vllm-project/vllm/issues/1025) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ray failed to register worker

### Issue 正文摘录

Hi, all, I both encountered the bugs mentioned above when I started a local ray instance on T4 gpus and A800 gpus, the startup shell like this: ```shell #!/bin/bash model=/home/user/models/Llama-2-13b-hf host=127.0.0.1 port=5679 tokenizer=$model tensor_parallel_size=8 gpu_memory_utilization=0.9 swap_space=16 echo $tensor_parallel_size python -m vllm.entrypoints.api_server \ --host=$host \ --port=$port \ --model=$model \ --tokenizer=$tokenizer \ --tensor-parallel-size=$tensor_parallel_size \ --gpu-memory-utilization=$gpu_memory_utilization \ --swap-space=$swap_space \ --engine-use-ray # --disable-log-requests \ # --max-num-batched-tokens 8192 # --disable-log-stats \ ``` the bug I encountered as follows: ```text [2023-09-13 02:28:19,539 E 119771 119771] core_worker.cc:201: Failed to register worker 01000000ffffffffffffffffffffffffffffffffffffffffffffffff to Raylet. IOError: [RayletClient] Unable to register worker with raylet. No such file or directory， ``` I have checked the ray log, the content as follows: ```text [2023-09-13 02:59:15,635 I 123317 123317] (raylet) worker_pool.cc:489: Started worker process with pid 123567, the token is 126 [2023-09-13 02:59:15,637 I 123317 123317]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 4 gpus and A800 gpus, the startup shell like this: ```shell #!/bin/bash model=/home/user/models/Llama-2-13b-hf host=127.0.0.1 port=5679 tokenizer=$model tensor_parallel_size=8 gpu_memory_utilization=0.9 swap_space=16 ec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e Ray agent was unexpectedly killed or failed. Agent can fail when - The version of `grpcio` doesn't follow Ray's requirement. Agent can segfault with the incorrect `grpcio` version. Check the grpcio version `pip freeze...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 15,637 W 123317 123317] (raylet) client_connection.cc:528: [worker]ProcessMessage with type RegisterClientRequest took 6982 ms. [2023-09-13 02:59:18,671 W 123317 123322] (raylet) metric_exporter.cc:212: [1] Export metri...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: swap-space=$swap_space \ --engine-use-ray # --disable-log-requests \ # --max-num-batched-tokens 8192 # --disable-log-stats \ ``` the bug I encountered as follows: ```text [2023-09-13 02:28:19,539 E 119771 119771] core_w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: unexpected error or port conflict. Read the log `cat /tmp/ray/session_latest/logs/dashboard_agent.log`. You can find the log file structure here https://docs.ray.io/en/master/ray-observability/ray-logging.html#logging-d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
