# vllm-project/vllm#41172: [Bug]: Mimo v2.5 model loading fails from s3/remote locations

| 字段 | 值 |
| --- | --- |
| Issue | [#41172](https://github.com/vllm-project/vllm/issues/41172) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mimo v2.5 model loading fails from s3/remote locations

### Issue 正文摘录

### Your current environment using the mimov2.5 docker container: vllm/vllm-openai:mimov25-cu129 ### 🐛 Describe the bug When trying to load mimo v2.5 from s3 location, we get a failure because of the /audioTokenizer folder not being downloaded to local disk/streamed. This is the same if we use runai_streamer or not. ``` vllm serve s3://path-to-mimo/mimo-v2.5 \ --tensor-parallel-size 4 \ --trust-remote-code \ --gpu-memory-utilization 0.95 \ --max-model-len auto \ --generation-config vllm ``` Fails with: ``` (Worker_TP0 pid=1083) ERROR 04-28 22:40:19 [multiproc_executor.py:870] WorkerProc failed to start. (Worker_TP0 pid=1083) ERROR 04-28 22:40:19 [multiproc_executor.py:870] Traceback (most recent call last): (Worker_TP0 pid=1083) ERROR 04-28 22:40:19 [multiproc_executor.py:870] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 837, in worker_main (Worker_TP0 pid=1083) ERROR 04-28 22:40:19 [multiproc_executor.py:870] worker = WorkerProc(*args, **kwargs) (Worker_TP0 pid=1083) ERROR 04-28 22:40:19 [multiproc_executor.py:870] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=1083) ERROR 04-28 22:40:19 [multiproc_executor.py:870] File "/usr/local/lib/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s3/remote locations bug ### Your current environment using the mimov2.5 docker container: vllm/vllm-openai:mimov25-cu129 ### 🐛 Describe the bug When trying to load mimo v2.5 from s3 location, we get a failure because of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Mimo v2.5 model loading fails from s3/remote locations bug ### Your current environment using the mimov2.5 docker container: vllm/vllm-openai:mimov25-cu129 ### 🐛 Describe the bug When trying to load mimo v2.5 fro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
