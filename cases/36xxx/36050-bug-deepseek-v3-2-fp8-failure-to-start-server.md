# vllm-project/vllm#36050: [Bug]: DeepSeek v3.2 FP8 Failure to start server

| 字段 | 值 |
| --- | --- |
| Issue | [#36050](https://github.com/vllm-project/vllm/issues/36050) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek v3.2 FP8 Failure to start server

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-V3.2 --data-parallel-size 8 --enable-expert-parallel ``` ``` (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] Traceback (most recent call last): (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] File "/vllm/vllm/v1/executor/multiproc_executor.py", line 813, in worker_main (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] worker = WorkerProc(*args, **kwargs) (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] File "/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] return func(*args, **kwargs) (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] ^^^^^^^^^^^^^^^^^^^^^ (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_e...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: DeepSeek v3.2 FP8 Failure to start server bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-V3.2 --data-parallel-size 8 --enable-expert-parallel ``` ``` (Worker pid=70964...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 3) ERROR 03-04 22:13:14 [multiproc_executor.py:844] self.worker.load_model() (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] File "/vllm/vllm/v1/worker/gpu_worker.py", li...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: `` vllm serve deepseek-ai/DeepSeek-V3.2 --data-parallel-size 8 --enable-expert-parallel ``` ``` (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] Traceback (most recent cal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ) ERROR 03-04 22:13:14 [multiproc_executor.py:844] File "/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker pid=709643) (Worker_DP2_EP2 pid=709643) ERROR 03-04 22:13:14 [multiproc_executor.py:844] return fun...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
