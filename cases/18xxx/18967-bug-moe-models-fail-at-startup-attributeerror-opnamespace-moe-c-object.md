# vllm-project/vllm#18967: [Bug]: MoE models fail at startup: AttributeError: '_OpNamespace' '_moe_C' object has no attribute 'topk_softmax'

| 字段 | 值 |
| --- | --- |
| Issue | [#18967](https://github.com/vllm-project/vllm/issues/18967) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 43; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MoE models fail at startup: AttributeError: '_OpNamespace' '_moe_C' object has no attribute 'topk_softmax'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to load MoE models with `vllm 0.9.0` (installed in empty environment with `uv pip install vllm --torch-backend=auto`), the model fails to load with ```python AttributeError: '_OpNamespace' '_moe_C' object has no attribute 'topk_softmax' ``` I've observed the same issue with several MoE models: - `Qwen/Qwen3-30B-A3B` - `mistralai/Mixtral-8x7B-Instruct-v0.1` - `ibm/PowerMoE-3b` For instance, running: ```bash vllm serve ibm/PowerMoE-3b ``` I get the following error: ```python Traceback (most recent call last): File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/tristan.leclercq/vllm-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 504, in run_engine_core raise e File "/home/tristan.leclercq/vllm-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 491, in run_engine_core engine_core = EngineCoreProc(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/tristan.leclercq/vllm-env/lib/python3.11/site-packages/vllm/v1/eng...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ## 🐛 Describe the bug When trying to load MoE models with `vllm 0.9.0` (installed in empty environment with `uv pip install vllm --torch-backend=auto`), the model fails to load with ```python AttributeError: '_OpNamespa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: MoE models fail at startup: AttributeError: '_OpNamespace' '_moe_C' object has no attribute 'topk_softmax' bug ### Your current environment ### 🐛 Describe the bug When trying to load MoE models with `vllm 0.9.0`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 0.9.0` (installed in empty environment with `uv pip install vllm --torch-backend=auto`), the model fails to load with ```python AttributeError: '_OpNamespace' '_moe_C' object has no attribute 'topk_softmax' ``` I've obs...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: orker.py", line 185, in determine_available_memory self.model_runner.profile_run() File "/home/tristan.leclercq/vllm-env/lib/python3.11/site-packages/vllm/v1/worker/gpu_model_runner.py", line 1897, in profile_run hidden...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
