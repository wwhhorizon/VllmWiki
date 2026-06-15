# vllm-project/vllm#18503: [Bug]: OLMo 2 models fail to load/run

| 字段 | 值 |
| --- | --- |
| Issue | [#18503](https://github.com/vllm-project/vllm/issues/18503) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OLMo 2 models fail to load/run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to load an OLMo 2 model as below leads to a ValueError. ```python from vllm.entrypoints.llm import LLM model = LLM("allenai/OLMo-2-0425-1B") ``` Error: ``` INFO 05-21 20:01:47 [default_loader.py:279] Loading weights took 0.72 seconds ERROR 05-21 20:01:47 [core.py:493] EngineCore failed to start. ERROR 05-21 20:01:47 [core.py:493] Traceback (most recent call last): ERROR 05-21 20:01:47 [core.py:493] File "/weka/oe-training-default/shanea/vllm/vllm/v1/engine/core.py", line 484, in run_engine_core ERROR 05-21 20:01:47 [core.py:493] engine_core = EngineCoreProc(*args, **kwargs) ERROR 05-21 20:01:47 [core.py:493] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 05-21 20:01:47 [core.py:493] File "/weka/oe-training-default/shanea/vllm/vllm/v1/engine/core.py", line 383, in __init__ ERROR 05-21 20:01:47 [core.py:493] super().__init__(vllm_config, executor_class, log_stats, ERROR 05-21 20:01:47 [core.py:493] File "/weka/oe-training-default/shanea/vllm/vllm/v1/engine/core.py", line 71, in __init__ ERROR 05-21 20:01:47 [core.py:493] self.model_executor = executor_class(vllm_config) ERROR 05-21 20:01:47 [core.py:493] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ E...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: del as below leads to a ValueError. ```python from vllm.entrypoints.llm import LLM model = LLM("allenai/OLMo-2-0425-1B") ``` Error: ``` INFO 05-21 20:01:47 [default_loader.py:279] Loading weights took 0.72 seconds ERROR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: OLMo 2 models fail to load/run bug ### Your current environment ### 🐛 Describe the bug Trying to load an OLMo 2 model as below leads to a ValueError. ```python from vllm.entrypoints.llm import LLM model = LLM("al...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
