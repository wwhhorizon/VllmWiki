# vllm-project/vllm#12404: [Bug]: InternVL2-26B-AWQ  Service startup failure

| 字段 | 值 |
| --- | --- |
| Issue | [#12404](https://github.com/vllm-project/vllm/issues/12404) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: InternVL2-26B-AWQ  Service startup failure

### Issue 正文摘录

### Your current environment ``` INFO 01-24 11:28:59 api_server.py:651] vLLM API server version 0.6.5 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` vllm serve InternVL2-26B-AWQ --served-model-name intervl2 --gpu_memory_utilization 0.99 --tensor-parallel-size 4 --limit-mm-per-prompt image=5,video=1 ``` ``` INFO 01-24 11:28:59 api_server.py:651] vLLM API server version 0.6.5 ERROR 01-24 11:29:27 engine.py:366] File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/internlm2.py", line 430, in load_weights ERROR 01-24 11:29:27 engine.py:366] param = params_dict[name] ERROR 01-24 11:29:27 engine.py:366] KeyError: 'model.layers.0.attention.wqkv.qweight' ERROR 01-24 11:29:28 multiproc_worker_utils.py:123] Worker VllmWorkerProcess pid 6961 died, exit code: -15 INFO 01-24 11:29:28 multiproc_worker_utils.py:127] Killing local vLLM worker processes ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: InternVL2-26B-AWQ Service startup failure bug;stale ### Your current environment ``` INFO 01-24 11:28:59 api_server.py:651] vLLM API server version 0.6.5 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: environment ``` INFO 01-24 11:28:59 api_server.py:651] vLLM API server version 0.6.5 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` vllm serve InternVL2-26B-AWQ --served-model-name intervl2 --gpu_mem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: InternVL2-26B-AWQ Service startup failure bug;stale ### Your current environment ``` INFO 01-24 11:28:59 api_server.py:651] vLLM API server version 0.6.5 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
