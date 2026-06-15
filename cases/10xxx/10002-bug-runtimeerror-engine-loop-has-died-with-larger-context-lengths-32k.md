# vllm-project/vllm#10002: [Bug]: RuntimeError: Engine loop has died with larger context lengths (>32k)

| 字段 | 值 |
| --- | --- |
| Issue | [#10002](https://github.com/vllm-project/vllm/issues/10002) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Engine loop has died with larger context lengths (>32k)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug even with ``` VLLM_WORKER_MULTIPROC_METHOD: "spawn" VLLM_LOGGING_LEVEL: "DEBUG" VLLM_TRACE_FUNCTION: "1" NCCL_DEBUG: "TRACE" ``` i could not collect more logs than ``` ERROR 11-04 12:53:08 client.py:250] RuntimeError('Engine loop has died') ERROR 11-04 12:53:08 client.py:250] Traceback (most recent call last): ERROR 11-04 12:53:08 client.py:250] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/client.py", line 150, in run_heartbeat_loop ERROR 11-04 12:53:08 client.py:250] await self._check_success( ERROR 11-04 12:53:08 client.py:250] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/client.py", line 314, in _check_success ERROR 11-04 12:53:08 client.py:250] raise response ERROR 11-04 12:53:08 client.py:250] RuntimeError: Engine loop has died INFO: 10.9.147.84:47210 - "GET /metrics HTTP/1.1" 200 OK INFO: 10.9.147.84:47210 - "GET /metrics HTTP/1.1" 200 OK INFO: 10.9.147.84:47210 - "GET /metrics HTTP/1.1" 200 OK CRITICAL 11-04 12:53:11 launcher.py:72] AsyncLLMEngine has failed, terminating server process INFO: 10.9.150.232:38400 - "GET /health HTTP/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: untimeError: Engine loop has died with larger context lengths (>32k) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug even with ``` VLLM_WORKER_MULTIPROC_METHOD: "spawn"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 18k context length prompt, failed with a 38k context length. Would appreciate some pointers on how to debug more here. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: er context lengths (>32k) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug even with ``` VLLM_WORKER_MULTIPROC_METHOD: "spawn" VLLM_LOGGING_LEVEL: "DEBUG" VLLM_TRACE_FUNC...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
