# vllm-project/vllm#26190: [Bug]: Qwen3-VL Launch failed due to incompatible API in get_dummy_input

| 字段 | 值 |
| --- | --- |
| Issue | [#26190](https://github.com/vllm-project/vllm/issues/26190) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL Launch failed due to incompatible API in get_dummy_input

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug _get_dummy_mm_inputs got unexpected argument ``` vllm serve Qwen/Qwen3-VL-235B-A22B-Instruct -tp 8 --limit-mm-per-prompt.video 0 --gpu_memory_utilization 0.95 --max_num_seqs 128 ``` ``` (Worker_TP0 pid=3351357) INFO 10-03 11:14:43 [gpu_model_runner.py:3461] Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. (Worker_TP0 pid=3351357) ERROR 10-03 11:14:43 [multiproc_executor.py:671] WorkerProc hit an exception. (Worker_TP0 pid=3351357) ERROR 10-03 11:14:43 [multiproc_executor.py:671] Traceback (most recent call last): (Worker_TP0 pid=3351357) ERROR 10-03 11:14:43 [multiproc_executor.py:671] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop (Worker_TP0 pid=3351357) ERROR 10-03 11:14:43 [multiproc_executor.py:671] output = func(*args, **kwargs) (Worker_TP0 pid=3351357) ERROR 10-03 11:14:43 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=3351357) ERROR 10-03 11:14:43 [multiproc_executor.py:671] File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 120,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL Launch failed due to incompatible API in get_dummy_input bug ### Your current environment ### 🐛 Describe the bug _get_dummy_mm_inputs got unexpected argument ``` vllm serve Qwen/Qwen3-VL-235B-A22B-Instru...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 10-03 11:14:43 [multiproc_executor.py:671] TypeError: Qwen3VLDummyInputsBuilder.get_dummy_processor_inputs() takes 3 positional arguments but 4 were given (Worker_TP0 pid=3351357) ERROR 10-03 11:14:43 [multiproc_executo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 61] Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. (Worker_TP0 pid=3351357) ERROR 10-03 11:14:43 [multiproc_executor.py:671] WorkerProc hit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: model_support;multimodal_vlm;sampling_logits cuda;gemm;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
