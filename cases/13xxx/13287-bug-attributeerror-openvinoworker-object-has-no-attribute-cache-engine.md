# vllm-project/vllm#13287: [Bug]: AttributeError: 'OpenVINOWorker' object has no attribute 'cache_engine'

| 字段 | 值 |
| --- | --- |
| Issue | [#13287](https://github.com/vllm-project/vllm/issues/13287) |
| 状态 | closed |
| 标签 | bug;stale |
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

> [Bug]: AttributeError: 'OpenVINOWorker' object has no attribute 'cache_engine'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Getting the following error while inferencing an embedding model with OpenVino ``` ERROR 02-14 11:10:20 engine.py:139] AttributeError("'OpenVINOWorker' object has no attribute 'cache_engine'") ERROR 02-14 11:10:20 engine.py:139] Traceback (most recent call last): ERROR 02-14 11:10:20 engine.py:139] File "/home/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 137, in start ERROR 02-14 11:10:20 engine.py:139] self.run_engine_loop() ERROR 02-14 11:10:20 engine.py:139] File "/home/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 200, in run_engine_loop ERROR 02-14 11:10:20 engine.py:139] request_outputs = self.engine_step() ERROR 02-14 11:10:20 engine.py:139] File "/home/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 218, in engine_step ERROR 02-14 11:10:20 engine.py:139] raise e ERROR 02-14 11:10:20 engine.py:139] File "/home/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 209, in engine_step ERROR 02-14 11:10:20 engine.py:139] return self.engine.step() ERROR 02-14 11:10:20 engine.py:139] File "/home/lib/python3.10/site-packages/vl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ent ### 🐛 Describe the bug Getting the following error while inferencing an embedding model with OpenVino ``` ERROR 02-14 11:10:20 engine.py:139] AttributeError("'OpenVINOWorker' object has no attribute 'cache_engine'")...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ributeError: 'OpenVINOWorker' object has no attribute 'cache_engine' bug;stale ### Your current environment ### 🐛 Describe the bug Getting the following error while inferencing an embedding model with OpenVino ``` ERROR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in execute_model ERROR 02-14 11:10:20 engine.py:139] self.cache_copy(blocks_to_copy) ERROR 02-14 11:10:20 engine.py:139] File "/home/lib/python3.10/site-packages/vllm/worker/openvino_worker.py", line 365, in cache_copy...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
