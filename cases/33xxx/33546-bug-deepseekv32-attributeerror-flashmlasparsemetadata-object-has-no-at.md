# vllm-project/vllm#33546: [Bug][DeepSeekV32]: AttributeError: 'FlashMLASparseMetadata' object has no attribute 'num_decodes'

| 字段 | 值 |
| --- | --- |
| Issue | [#33546](https://github.com/vllm-project/vllm/issues/33546) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][DeepSeekV32]: AttributeError: 'FlashMLASparseMetadata' object has no attribute 'num_decodes'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve /mnt/data4/models/deepseek-ai/DeepSeek-V3___2 -tp=8 --tokenizer-mode deepseek_v32 --enable-auto-tool-choice --tool-call-parser deepseek_v32 --reasoning-parser deepseek_v3 ``` ``` (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] Traceback (most recent call last): (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] File "/mnt/data4/jxy/vllm/vllm/v1/executor/multiproc_executor.py", line 847, in worker_busy_loop (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] output = func(*args, **kwargs) (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] File "/mnt/data4/jxy/vllm/vllm/v1/worker/gpu_worker.py", line 455, in compile_or_warm_up_model (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] cuda_graph_memory_bytes = self.model_runner.capture_model() (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_exec...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] cuda_graph_memory_bytes = self.model_runner.capture_model() (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ] File "/mnt/data4/jxy/venv/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 1044, in _fn (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] return fn(*args, **kwargs) (Worker_TP5 p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: File "/mnt/data4/jxy/vllm/vllm/v1/worker/gpu_worker.py", line 455, in compile_or_warm_up_model (Worker_TP5 pid=2702854) ERROR 02-02 15:18:53 [multiproc_executor.py:852] cuda_graph_memory_bytes = self.model_runner.captur...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug][DeepSeekV32]: AttributeError: 'FlashMLASparseMetadata' object has no attribute 'num_decodes' bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve /mnt/data4/models/deepseek-ai/DeepSeek-V3___2 -tp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: urrent environment ### 🐛 Describe the bug ``` vllm serve /mnt/data4/models/deepseek-ai/DeepSeek-V3___2 -tp=8 --tokenizer-mode deepseek_v32 --enable-auto-tool-choice --tool-call-parser deepseek_v32 --reasoning-parser dee...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
