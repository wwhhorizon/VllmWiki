# vllm-project/vllm#14465: [Bug]: Mistral-Small-24B-Instruct-2501 on V1 fails to start with Mistral tokenizer since V1 enabled guided decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#14465](https://github.com/vllm-project/vllm/issues/14465) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral-Small-24B-Instruct-2501 on V1 fails to start with Mistral tokenizer since V1 enabled guided decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Cannot start Mistral-Small-24B-Instruct-2501 with the Mistral tokenizer on V1 anymore. Traceback: ```text ERROR 03-07 16:37:49 [core.py:324] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-07 16:37:49 [core.py:324] File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 316, in run_engine_core ERROR 03-07 16:37:49 [core.py:324] engine_core = EngineCoreProc(*args, **kwargs) ERROR 03-07 16:37:49 [core.py:324] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-07 16:37:49 [core.py:324] File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 271, in __init__ ERROR 03-07 16:37:49 [core.py:324] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-07 16:37:49 [core.py:324] File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 65, in __init__ ERROR 03-07 16:37:49 [core.py:324] self.structured_output_manager = StructuredOutputManager(vllm_config) ERROR 03-07 16:37:49 [core.py:324] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-07 16:37:49 [core.py:324] File "/home/jeff/.virtualenvs/vllm312...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Mistral-Small-24B-Instruct-2501 on V1 fails to start with Mistral tokenizer since V1 enabled guided decoding bug;structured-output ### Your current environment ### 🐛 Describe the bug Cannot start Mistral-Small-24...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: in __init__ ERROR 03-07 16:37:49 [core.py:324] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-07 16:37:49 [core.py:324] File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-packages/vllm/v1/engin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
