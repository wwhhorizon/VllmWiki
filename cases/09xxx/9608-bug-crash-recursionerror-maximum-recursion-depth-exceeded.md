# vllm-project/vllm#9608: [Bug]: crash：RecursionError: maximum recursion depth exceeded

| 字段 | 值 |
| --- | --- |
| Issue | [#9608](https://github.com/vllm-project/vllm/issues/9608) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: crash：RecursionError: maximum recursion depth exceeded

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug command: ```bash vllm serve /hestia/model/Qwen2.5-14B-Instruct-AWQ --max-model-len 32768 --quantization awq --port 8001 --swap-space 0 --served-model-name qwen --num-gpu-blocks-override 2048 ``` ```bash INFO: 127.0.0.1:42158 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR 10-23 07:25:31 engine.py:158] RecursionError('maximum recursion depth exceeded') ERROR 10-23 07:25:31 engine.py:158] Traceback (most recent call last): ERROR 10-23 07:25:31 engine.py:158] File "/opt/conda/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 156, in start ERROR 10-23 07:25:31 engine.py:158] self.run_engine_loop() ERROR 10-23 07:25:31 engine.py:158] File "/opt/conda/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 219, in run_engine_loop ERROR 10-23 07:25:31 engine.py:158] request_outputs = self.engine_step() ERROR 10-23 07:25:31 engine.py:158] ^^^^^^^^^^^^^^^^^^ ERROR 10-23 07:25:31 engine.py:158] File "/opt/conda/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 237, in engine_step ERROR 10-23 07:25:31 engine.py:158] r...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: crash：RecursionError: maximum recursion depth exceeded bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug command: ```bash vllm serve /hestia/model/Qwen2.5-14B-Instr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding cuda;kernel;operator;quantization;triton b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: zation awq --port 8001 --swap-space 0 --served-model-name qwen --num-gpu-blocks-override 2048 ``` ```bash INFO: 127.0.0.1:42158 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR 10-23 07:25:31 engin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: recursion depth exceeded bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug command: ```bash vllm serve /hestia/model/Qwen2.5-14B-Instruct-AWQ --max-model-len 32768 --quant...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
