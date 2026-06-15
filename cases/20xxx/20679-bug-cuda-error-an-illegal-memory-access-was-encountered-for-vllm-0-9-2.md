# vllm-project/vllm#20679: [Bug]: CUDA error: an illegal memory access was encountered for vllm 0.9.2 + cuda12.8

| 字段 | 值 |
| --- | --- |
| Issue | [#20679](https://github.com/vllm-project/vllm/issues/20679) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error: an illegal memory access was encountered for vllm 0.9.2 + cuda12.8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start serve ``` vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B ``` start infer ``` python benchmarks/benchmark_serving.py --backend vllm --model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B --random-input-len 13 --random-output-len 512 --dataset-name random --num-prompts 1 ``` serve error ``` (VllmWorker rank=1 pid=6939) ERROR 07-09 18:53:37 [multiproc_executor.py:522] ... /venv_v092/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line 748, in _prepare_inputs (VllmWorker rank=1 pid=6939) ERROR 07-09 18:53:37 [multiproc_executor.py:522] logits_indices = query_start_loc[1:] - 1 (VllmWorker rank=1 pid=6939) ERROR 07-09 18:53:37 [multiproc_executor.py:522] RuntimeError: CUDA error: an illegal memory access was encountered (VllmWorker rank=1 pid=6939) ERROR 07-09 18:53:37 [multiproc_executor.py:522] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;sampling;triton build_e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA error: an illegal memory access was encountered for vllm 0.9.2 + cuda12.8 bug;stale ### Your current environment ### 🐛 Describe the bug start serve ``` vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ll-Qwen-7B ``` start infer ``` python benchmarks/benchmark_serving.py --backend vllm --model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B --random-input-len 13 --random-output-len 512 --dataset-name random --num-prompts 1 ``...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ribe the bug start serve ``` vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B ``` start infer ``` python benchmarks/benchmark_serving.py --backend vllm --model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B --random-input-le...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : an illegal memory access was encountered for vllm 0.9.2 + cuda12.8 bug;stale ### Your current environment ### 🐛 Describe the bug start serve ``` vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B ``` start infer ``` p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
