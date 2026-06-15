# vllm-project/vllm#22232: [Bug]: DeepSeekV3 type model fails with UnboundLocalError: cannot access local variable 'shared_output'

| 字段 | 值 |
| --- | --- |
| Issue | [#22232](https://github.com/vllm-project/vllm/issues/22232) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeekV3 type model fails with UnboundLocalError: cannot access local variable 'shared_output'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed vllm v0.10.0rc1 with access to an H100 GPU. I want to experiment with DeepseekV3 without shared experts, by setting `n_shared_experts: null` in configuration. vLLM crashes during CUDA graph capture. The error is: ``` UnboundLocalError: cannot access local variable 'shared_output' where it is not associated with a value ``` The full output is: ``` Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks. [multiproc_worker_utils.py:239] Traceback (most recent call last): [multiproc_worker_utils.py:239] File "/usr/local/lib/python3.12/dist-packages/vllm/executor/multiproc_worker_utils.py", line 233, in _run_worker_process [multiproc_worker_utils.py:239] output = run_method(worker, method, args, kwargs) [multiproc_worker_utils.py:239] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [multiproc_worker_utils.py:239] File "/usr/local/lib/python3.12/dist-packages/vllm/utils/__init__.py", line 2991, in run_method [multiproc_worker_utils.py:239] return func(*args, **kwargs) [multiproc_worker_utils.py:239] ^^^^^^^^^^^^^^^^^^^^^ [multiproc_worker_utils.py:239] File "/usr/local/lib/python3.12/dist-packa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ut' bug;stale ### Your current environment ### 🐛 Describe the bug I installed vllm v0.10.0rc1 with access to an H100 GPU. I want to experiment with DeepseekV3 without shared experts, by setting `n_shared_experts: null`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### 🐛 Describe the bug I installed vllm v0.10.0rc1 with access to an H100 GPU. I want to experiment with DeepseekV3 without shared experts, by setting `n_shared_experts: null` in configuration. vLLM crashes during CUDA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: DeepSeekV3 type model fails with UnboundLocalError: cannot access local variable 'shared_output' bug;stale ### Your current environment ### 🐛 Describe the bug I installed vllm v0.10.0rc1 with access to an H100 GP...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: cess to an H100 GPU. I want to experiment with DeepseekV3 without shared experts, by setting `n_shared_experts: null` in configuration. vLLM crashes during CUDA graph capture. The error is: ``` UnboundLocalError: cannot...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: m_available_blocks [multiproc_worker_utils.py:239] self.model_runner.profile_run() [multiproc_worker_utils.py:239] File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 120, in decorate_context...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
