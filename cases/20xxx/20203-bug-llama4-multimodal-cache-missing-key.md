# vllm-project/vllm#20203: [Bug]: Llama4 multimodal cache missing key

| 字段 | 值 |
| --- | --- |
| Issue | [#20203](https://github.com/vllm-project/vllm/issues/20203) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama4 multimodal cache missing key

### Issue 正文摘录

### Your current environment Python 3.11 CUDA 12.4 vLLM 0.8.4 ### 🐛 Describe the bug vLLM v0.8.4 ``` ERROR 06-27 16:32:19 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): ERROR 06-27 16:32:19 [core.py:387] File "/opt/conda/lib/python3.11/site-packages/cachetools/__init__.py", line 66, in __getitem__ ERROR 06-27 16:32:19 [core.py:387] return self.__data[key] ERROR 06-27 16:32:19 [core.py:387] ~~~~~~~~~~~^^^^^ ERROR 06-27 16:32:19 [core.py:387] KeyError: 'f224b2249792ee5054e8ec7c0b68f6d22889843159c73bdea187eda555743f85' ERROR 06-27 16:32:19 [core.py:387] ERROR 06-27 16:32:19 [core.py:387] During handling of the above exception, another exception occurred: ERROR 06-27 16:32:19 [core.py:387] ERROR 06-27 16:32:19 [core.py:387] Traceback (most recent call last): ERROR 06-27 16:32:19 [core.py:387] File "/opt/conda/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 380, in run_engine_core ERROR 06-27 16:32:19 [core.py:387] engine_core.run_busy_loop() ERROR 06-27 16:32:19 [core.py:387] File "/opt/conda/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 400, in run_busy_loop ERROR 06-27 16:32:19 [core.py:387] self._process_input_queue() ERROR 06-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;frontend_api;multimodal_vlm cuda crash env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Llama4 multimodal cache missing key bug ### Your current environment Python 3.11 CUDA 12.4 vLLM 0.8.4 ### 🐛 Describe the bug vLLM v0.8.4 ``` ERROR 06-27 16:32:19 [core.py:387] EngineCore hit an exception: Traceba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ltimodal cache missing key bug ### Your current environment Python 3.11 CUDA 12.4 vLLM 0.8.4 ### 🐛 Describe the bug vLLM v0.8.4 ``` ERROR 06-27 16:32:19 [core.py:387] EngineCore hit an exception: Traceback (most recent...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: run_busy_loop ERROR 06-27 16:32:19 [core.py:387] self._process_input_queue() ERROR 06-27 16:32:19 [core.py:387] File "/opt/conda/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 425, in _process_input_queue ER...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Llama4 multimodal cache missing key bug ### Your current environment Python 3.11 CUDA 12.4 vLLM 0.8.4 ### 🐛 Describe the bug vLLM v0.8.4 ``` ERROR 06-27 16:32:19 [core.py:387] EngineCore hit an exception: Traceba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
