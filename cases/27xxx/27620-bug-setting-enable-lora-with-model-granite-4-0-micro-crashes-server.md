# vllm-project/vllm#27620: [Bug]: Setting --enable-lora with model granite-4.0-micro crashes server

| 字段 | 值 |
| --- | --- |
| Issue | [#27620](https://github.com/vllm-project/vllm/issues/27620) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Setting --enable-lora with model granite-4.0-micro crashes server

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Steps to reproduce: 1. `vllm serve ibm-granite/granite-4.0-micro --enable-lora` Expected behavior: Server startup Behavior observed: Server crashes with stack trace pointing to another stack trace pointing to this stack trace: ``` (EngineCore_DP0 pid=424717) (EngineCore_DP0 pid=424717) INFO 10-27 18:38:44 [default_loader.py:267] Loading weights took 2.49 seconds (EngineCore_DP0 pid=424717) INFO 10-27 18:38:44 [punica_selector.py:19] Using PunicaWrapperGPU. (EngineCore_DP0 pid=424717) ERROR 10-27 18:38:45 [core.py:708] EngineCore failed to start. (EngineCore_DP0 pid=424717) ERROR 10-27 18:38:45 [core.py:708] Traceback (most recent call last): (EngineCore_DP0 pid=424717) ERROR 10-27 18:38:45 [core.py:708] File "/mnt/nvmedisk/freiss/granite/tmpenv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 699, in run_engine_core (EngineCore_DP0 pid=424717) ERROR 10-27 18:38:45 [core.py:708] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=424717) ERROR 10-27 18:38:45 [core.py:708] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=424717) ERROR 10-27 18:38:45 [core.py:708] File "/mnt/nvmedisk/freiss/granite/tmpenv/...

## 现有链接修复摘要

#27733 [BugFix]: --enable-lora with model granite-4.0-micro crash

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Setting --enable-lora with model granite-4.0-micro crashes server bug ### Your current environment ### 🐛 Describe the bug Steps to reproduce: 1. `vllm serve ibm-granite/granite-4.0-micro --enable-lora` Expected b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #27733 [BugFix]: --enable-lora with model granite-4.0-micro crash Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: er bug ### Your current environment ### 🐛 Describe the bug Steps to reproduce: 1. `vllm serve ibm-granite/granite-4.0-micro --enable-lora` Expected behavior: Server startup Behavior observed: Server crashes with stack t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27733](https://github.com/vllm-project/vllm/pull/27733) | closes_keyword | 0.95 | [BugFix]: --enable-lora with model granite-4.0-micro crash | Fix: #27620 note: must set `--enforce-eager` otherwise vllm will crash when use vscode debug mode ## Test Plan ## Test Result start up log: ``` INFO 10-29 09:17:34 [__init__.py |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
