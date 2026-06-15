# vllm-project/vllm#17707: [Bug]: RuntimeError: Worker failed with error 'SystemError: excessive stack use: stack is 3598 deep

| 字段 | 值 |
| --- | --- |
| Issue | [#17707](https://github.com/vllm-project/vllm/issues/17707) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Worker failed with error 'SystemError: excessive stack use: stack is 3598 deep

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug version 0.8.5&0.8.5.post1 ```bash (VllmWorker rank=0 pid=55723) Exception ignored in: .remove at 0x7fa2d018feb0> (VllmWorker rank=0 pid=55723) Traceback (most recent call last): (VllmWorker rank=0 pid=55723) File "/home/F233531/anaconda3/envs/vllm0850/lib/python3.10/site-packages/torch/utils/weak.py", line 125, in remove (VllmWorker rank=0 pid=55723) def remove(k, selfref=ref(self)): (VllmWorker rank=0 pid=55723) File "/home/F233531/anaconda3/envs/vllm0850/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 398, in signal_handler (VllmWorker rank=0 pid=55723) raise SystemExit() (VllmWorker rank=0 pid=55723) SystemExit: ERROR 05-06 16:54:45 [multiproc_executor.py:123] Worker proc VllmWorker-1 died unexpectedly, shutting down executor. Process EngineCore_0: Traceback (most recent call last): File "/home/F233531/anaconda3/envs/vllm0850/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap self.run() File "/home/F233531/anaconda3/envs/vllm0850/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/F233531/anaconda3/envs/vllm0850/lib/pytho...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s 3598 deep bug ### Your current environment ### 🐛 Describe the bug version 0.8.5&0.8.5.post1 ```bash (VllmWorker rank=0 pid=55723) Exception ignored in: .remove at 0x7fa2d018feb0> (VllmWorker rank=0 pid=55723) Tracebac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm/v1/engine/core.py", line 329, in __init__ super().__init__(vllm_config, executor_class, log_stats, File "/home/F233531/anaconda3/envs/vllm0850/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 71, in __ini...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
