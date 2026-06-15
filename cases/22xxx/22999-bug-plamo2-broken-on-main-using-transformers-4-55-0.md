# vllm-project/vllm#22999: [Bug]: plamo2 broken on main using transformers==4.55.0

| 字段 | 值 |
| --- | --- |
| Issue | [#22999](https://github.com/vllm-project/vllm/issues/22999) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: plamo2 broken on main using transformers==4.55.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve pfnet/plamo-2.1-2b-cpt --trust-remote-code ``` produces: ``` ERROR 08-15 14:27:19 [engine.py:467] Plamo2ForCausalLM.get_input_embeddings() missing 1 required positional argument: 'input_ids' ERROR 08-15 14:27:19 [engine.py:467] Traceback (most recent call last): ERROR 08-15 14:27:19 [engine.py:467] File "/home/zrltpa/vllm/vllm/engine/multiprocessing/engine.py", line 455, in run_mp_engine ERROR 08-15 14:27:19 [engine.py:467] engine = MQLLMEngine.from_vllm_config( ERROR 08-15 14:27:19 [engine.py:467] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 08-15 14:27:19 [engine.py:467] File "/home/zrltpa/vllm/vllm/utils/__init__.py", line 1552, in inner ERROR 08-15 14:27:19 [engine.py:467] return fn(*args, **kwargs) ERROR 08-15 14:27:19 [engine.py:467] ^^^^^^^^^^^^^^^^^^^ ERROR 08-15 14:27:19 [engine.py:467] File "/home/zrltpa/vllm/vllm/engine/multiprocessing/engine.py", line 144, in from_vllm_config ERROR 08-15 14:27:19 [engine.py:467] return cls( ERROR 08-15 14:27:19 [engine.py:467] ^^^^ ERROR 08-15 14:27:19 [engine.py:467] File "/home/zrltpa/vllm/vllm/engine/multiprocessing/engine.py", line 88, in __init__ ERROR 08-15 14:27:19 [engin...

## 现有链接修复摘要

#23998 [V1] v1 engine + full CUDA graph support for PLaMo2

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ERROR 08-15 14:27:19 [engine.py:467] engine = MQLLMEngine.from_vllm_config( ERROR 08-15 14:27:19 [engine.py:467] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 08-15 14:27:19 [engine.py:467] File "/home/zrltpa/vllm/vllm/utils/__in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #23998 [V1] v1 engine + full CUDA graph support for PLaMo2 Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #23998 [V1] v1 engine + full CUDA graph support for PL...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23998](https://github.com/vllm-project/vllm/pull/23998) | closes_keyword | 0.95 | [V1] v1 engine + full CUDA graph support for PLaMo2 | fix #22999. ## Benchmarks ### Latency Latency improves quite a bit. This PR (v1 engine, `CUDAGraphMode.FULL_AND_PIECEWISE`): ``` $ VLLM_USE_V1=1 vllm bench latency --model pfne |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
