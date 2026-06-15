# vllm-project/vllm#18556: [Bug]: PixtralForConditionalGeneration is broken due to bad placeholder tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#18556](https://github.com/vllm-project/vllm/issues/18556) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PixtralForConditionalGeneration is broken due to bad placeholder tokens

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to load the original Pixtral model in vLLM fails on main. It worked fine in `vllm==0.8.5.post1` Server command: ``` vllm serve mistralai/Pixtral-12B-2409 --load-format dummy --tokenizer-mode mistral ``` Output: ``` Traceback (most recent call last): File "/home/mgoin/.local/share/uv/python/cpython-3.12.4-linux-x86_64-gnu/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/home/mgoin/.local/share/uv/python/cpython-3.12.4-linux-x86_64-gnu/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/mgoin/code/vllm/vllm/v1/engine/core.py", line 497, in run_engine_core raise e File "/home/mgoin/code/vllm/vllm/v1/engine/core.py", line 484, in run_engine_core engine_core = EngineCoreProc(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/mgoin/code/vllm/vllm/v1/engine/core.py", line 383, in __init__ super().__init__(vllm_config, executor_class, log_stats, File "/home/mgoin/code/vllm/vllm/v1/engine/core.py", line 71, in __init__ self.model_executor = executor_class(vllm_config) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/mgoin/code/vllm/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ironment ### 🐛 Describe the bug Trying to load the original Pixtral model in vLLM fails on main. It worked fine in `vllm==0.8.5.post1` Server command: ``` vllm serve mistralai/Pixtral-12B-2409 --load-format dummy --toke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;ope...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: egistry.py", line 121, in get_max_tokens_per_item_by_modality return profiler.get_mm_max_tokens( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/mgoin/code/vllm/vllm/multimodal/profiling.py", line 266, in get_mm_max_tokens mm_i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
