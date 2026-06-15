# vllm-project/vllm#20347: [Bug]: 'DeepSeekMultiTokenPredictor' object has no attribute 'embed_tokens'

| 字段 | 值 |
| --- | --- |
| Issue | [#20347](https://github.com/vllm-project/vllm/issues/20347) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 'DeepSeekMultiTokenPredictor' object has no attribute 'embed_tokens'

### Issue 正文摘录

### Your current environment vllm serve /model/DeepSeek-R1 --host 0.0.0.0 --port 8000 --max-num-seqs 1024 --tensor-parallel-size 8 --speculative-config '{"method": "deepseek_mtp", "num_speculative_tokens": 8}' ### 🐛 Describe the bug vllm v0.9.1执行报错 (VllmWorker rank=5 pid=2573) ERROR 07-01 19:03:19 [multiproc_executor.py:492] WorkerProc failed to start. (VllmWorker rank=5 pid=2573) ERROR 07-01 19:03:19 [multiproc_executor.py:492] Traceback (most recent call last): (VllmWorker rank=5 pid=2573) ERROR 07-01 19:03:19 [multiproc_executor.py:492] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 466, in worker_main (VllmWorker rank=5 pid=2573) ERROR 07-01 19:03:19 [multiproc_executor.py:492] worker = WorkerProc(*args, **kwargs) (VllmWorker rank=5 pid=2573) ERROR 07-01 19:03:19 [multiproc_executor.py:492] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=5 pid=2573) ERROR 07-01 19:03:19 [multiproc_executor.py:492] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 363, in __init__ (VllmWorker rank=5 pid=2573) ERROR 07-01 19:03:19 [multiproc_executor.py:492] self.worker.load_model() (VllmWorker rank=5 pid=2573) E...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: host 0.0.0.0 --port 8000 --max-num-seqs 1024 --tensor-parallel-size 8 --speculative-config '{"method": "deepseek_mtp", "num_speculative_tokens": 8}' ### 🐛 Describe the bug vllm v0.9.1执行报错 (VllmWorker rank=5 pid=2573) ER...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: o attribute 'embed_tokens' bug ### Your current environment vllm serve /model/DeepSeek-R1 --host 0.0.0.0 --port 8000 --max-num-seqs 1024 --tensor-parallel-size 8 --speculative-config '{"method": "deepseek_mtp", "num_spe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 68) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
