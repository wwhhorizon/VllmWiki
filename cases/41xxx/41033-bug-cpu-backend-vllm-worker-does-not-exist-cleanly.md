# vllm-project/vllm#41033: [Bug]: [CPU Backend] VLLM Worker does not exist cleanly

| 字段 | 值 |
| --- | --- |
| Issue | [#41033](https://github.com/vllm-project/vllm/issues/41033) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [CPU Backend] VLLM Worker does not exist cleanly

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Reproducer: Build vLLM on CPU then run: ``` vllm bench throughput --num-prompts ``` Error: ``` (Worker pid=387928) INFO 04-27 17:12:12 [multiproc_executor.py:775] Parent process exited, terminating worker queues (Worker pid=387928) INFO 04-27 17:12:12 [multiproc_executor.py:872] WorkerProc shutting down. (Worker pid=387928) Process VllmWorker-0: (Worker pid=387928) Traceback (most recent call last): (Worker pid=387928) File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap (Worker pid=387928) self.run() (Worker pid=387928) File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run (Worker pid=387928) self._target(*self._args, **self._kwargs) (Worker pid=387928) File "/home/fadara01/vllm-fix-engine-exit/venv/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 895, in worker_main (Worker pid=387928) worker.shutdown() (Worker pid=387928) File "/home/fadara01/vllm-fix-engine-exit/venv/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 760, in shutdown (Worker pid=387928) self.worker.shutdown() (Worker pid=387928) File "/home/fadara01/vllm-fix-engine-e...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: scribe the bug Reproducer: Build vLLM on CPU then run: ``` vllm bench throughput --num-prompts ``` Error: ``` (Worker pid=387928) INFO 04-27 17:12:12 [multiproc_executor.py:775] Parent process exited, terminating worker...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: [CPU Backend] VLLM Worker does not exist cleanly bug;cpu ### Your current environment ### 🐛 Describe the bug Reproducer: Build vLLM on CPU then run: ``` vllm bench throughput --num-prompts ``` Error: ``` (Worker...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: cleanly bug;cpu ### Your current environment ### 🐛 Describe the bug Reproducer: Build vLLM on CPU then run: ``` vllm bench throughput --num-prompts ``` Error: ``` (Worker pid=387928) INFO 04-27 17:12:12 [multiproc_execu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pu ### Your current environment ### 🐛 Describe the bug Reproducer: Build vLLM on CPU then run: ``` vllm bench throughput --num-prompts ``` Error: ``` (Worker pid=387928) INFO 04-27 17:12:12 [multiproc_executor.py:775] P...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
