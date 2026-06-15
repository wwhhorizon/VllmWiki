# vllm-project/vllm#16652: [Usage]: RTX 5090 with vllm/vllm-openai docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#16652](https://github.com/vllm-project/vllm/issues/16652) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: RTX 5090 with vllm/vllm-openai docker image

### Issue 正文摘录

### Your current environment Is there a way to work with vllm/vllm-openai docker image having a rtx 5090? Getting a lot of errors. ``` vllm_server | ERROR 04-15 02:01:15 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): vllm_server | ERROR 04-15 02:01:15 [core.py:387] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 378, in run_engine_core vllm_server | ERROR 04-15 02:01:15 [core.py:387] engine_core = EngineCoreProc(*args, **kwargs) vllm_server | ERROR 04-15 02:01:15 [core.py:387] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ vllm_server | ERROR 04-15 02:01:15 [core.py:387] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 320, in __init__ vllm_server | ERROR 04-15 02:01:15 [core.py:387] super().__init__(vllm_config, executor_class, log_stats) vllm_server | ERROR 04-15 02:01:15 [core.py:387] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 67, in __init__ vllm_server | ERROR 04-15 02:01:15 [core.py:387] self.model_executor = executor_class(vllm_config) vllm_server | ERROR 04-15 02:01:15 [core.py:387] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ vllm_server | ERROR 04-15 02:01:15 [core.py:387] File "/usr/l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: RTX 5090 with vllm/vllm-openai docker image usage ### Your current environment Is there a way to work with vllm/vllm-openai docker image having a rtx 5090? Getting a lot of errors. ``` vllm_server | ERROR 04-15...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: RTX 5090 with vllm/vllm-openai docker image usage ### Your current environment Is there a way to work with vllm/vllm-openai docker image having a rtx 5090? Getting a lot of errors. ``` vllm_server | ERROR 04-15...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m_server | ERROR 04-15 02:01:15 [core.py:387] super().__init__(vllm_config, executor_class, log_stats) vllm_server | ERROR 04-15 02:01:15 [core.py:387] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engi
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
