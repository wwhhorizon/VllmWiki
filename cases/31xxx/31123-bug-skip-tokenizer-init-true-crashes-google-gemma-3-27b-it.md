# vllm-project/vllm#31123: [Bug]: skip_tokenizer_init=True crashes `google/gemma-3-27b-it`

| 字段 | 值 |
| --- | --- |
| Issue | [#31123](https://github.com/vllm-project/vllm/issues/31123) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: skip_tokenizer_init=True crashes `google/gemma-3-27b-it`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` uv run --with vllm==0.13.0 python -c 'import vllm; vllm.LLM("google/gemma-3-27b-it", load_format="dummy", enforce_eager=True, tensor_parallel_size=8, skip_tokenizer_init=True)' ``` got this error ``` (EngineCore_DP0 pid=3848444) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`. (EngineCore_DP0 pid=3848444) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`. (EngineCore_DP0 pid=3848444) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. Th...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: skip_tokenizer_init=True crashes `google/gemma-3-27b-it` bug;stale ### Your current environment ### 🐛 Describe the bug ``` uv run --with vllm==0.13.0 python -c 'import vllm; vllm.LLM("google/gemma-3-27b-it", load...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nt ### 🐛 Describe the bug ``` uv run --with vllm==0.13.0 python -c 'import vllm; vllm.LLM("google/gemma-3-27b-it", load_format="dummy", enforce_eager=True, tensor_parallel_size=8, skip_tokenizer_init=True)' ``` got this...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: pid=3848444) ERROR 12-21 22:36:30 [multiproc_executor.py:751] return profiler.get_mm_max_tokens( (EngineCore_DP0 pid=3848444) ERROR 12-21 22:36:30 [multiproc_executor.py:751] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ERROR 12-21 22:36:30 [multiproc_executor.py:751] File "/root/.cache/uv/archive-v0/_QNRfXPrLrVvrVi5nZnrp/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 722, in worker_main (EngineCore_DP0 pid=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: skip_tokenizer_init=True crashes `google/gemma-3-27b-it` bug;stale ### Your current environment ### 🐛 Describe the bug ``` uv run --with vllm==0.13.0 python -c 'import vllm; vllm.LLM("google/gemma-3-27b-it", load...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
