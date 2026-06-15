# vllm-project/vllm#12035: [Usage]: Failed to serve local model in distributed inference

| 字段 | 值 |
| --- | --- |
| Issue | [#12035](https://github.com/vllm-project/vllm/issues/12035) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Failed to serve local model in distributed inference

### Issue 正文摘录

### Your current environment ```text Deploy vllm with docker image v0.6.0 and v0.6.6 in Kubernetes, both have the question. ``` ### How would you like to use vllm The command looks like below, I set the pp=2 to simulate multi-host scenarios, so I have 2 nodes each with 1GPU: ``` python3 -m vllm.entrypoints.openai.api_server --model /workspace/models/models--Qwen--Qwen2-0.5B --host 0.0.0.0 --port 8080 --tensor-parallel-size 1 --pipeline-parallel-size 2 ``` The error looks like: ``` (RayWorkerWrapper pid=410, ip=172.24.0.105) ERROR 01-14 03:08:55 worker_base.py:467] The above exception was the direct cause of the following exception: (RayWorkerWrapper pid=410, ip=172.24.0.105) ERROR 01-14 03:08:55 worker_base.py:467] (RayWorkerWrapper pid=410, ip=172.24.0.105) ERROR 01-14 03:08:55 worker_base.py:467] Traceback (most recent call last): (RayWorkerWrapper pid=410, ip=172.24.0.105) ERROR 01-14 03:08:55 worker_base.py:467] File "/usr/local/lib/python3.12/dist-packages/vllm/worker/worker_base.py", line 459, in execute_method (RayWorkerWrapper pid=410, ip=172.24.0.105) ERROR 01-14 03:08:55 worker_base.py:467] return executor(*args, **kwargs) (RayWorkerWrapper pid=410, ip=172.24.0.105) ERRO...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Failed to serve local model in distributed inference usage ### Your current environment ```text Deploy vllm with docker image v0.6.0 and v0.6.6 in Kubernetes, both have the question. ``` ### How would you like...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d inference usage ### Your current environment ```text Deploy vllm with docker image v0.6.0 and v0.6.6 in Kubernetes, both have the question. ``` ### How would you like to use vllm The command looks like below, I set th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 5 worker_base.py:467] file_list = fs.ls(model_name_or_path, detail=False, revision=revision) (RayWorkerWrapper pid=410, ip=172.24.0.105) ERROR 01-14 03:08:55 worker_base.py:467] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
