# vllm-project/vllm#10987: [Bug]: Qwen2VL doesn't work with TPU backend

| 字段 | 值 |
| --- | --- |
| Issue | [#10987](https://github.com/vllm-project/vllm/issues/10987) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2VL doesn't work with TPU backend

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug What I did was simply run vllm serve Qwen/Qwen2-VL-7B-Instruct. Previously, I tested the pure LLM (Qwen2.5-7B), and it worked. I think this error code is relevant for debugging: ``` (RayWorkerWrapper pid=22778) INFO 12-08 10:38:29 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. [repeated 2x across cluster] (RayWorkerWrapper pid=22792) INFO 12-08 10:38:30 weight_utils.py:243] Using model weights format ['*.safetensors'] [repeated 2x across cluster] (RayWorkerWrapper pid=22792) ERROR 12-08 10:40:08 worker_base.py:467] Error executing method determine_num_available_blocks. This might cause deadlock in distributed execution. [repeated 2x across cluster] (RayWorkerWrapper pid=22792) ERROR 12-08 10:40:08 worker_base.py:467] Traceback (most recent call last): [repeated 2x across cluster] (RayWorkerWrapper pid=22792) ERROR 12-08 10:40:08 worker_base.py:467] File "/home/carlesoctav/vllm/vllm/worker/worker_base.py", line 459, in execute_method [repeated 2x across cluster] (RayWorkerWrapper pid=22792) ERROR 12-08 10:40:08 worker_base.py:467] re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: vant for debugging: ``` (RayWorkerWrapper pid=22778) INFO 12-08 10:38:29 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. [repeated 2x across cluster] (RayWor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2VL doesn't work with TPU backend bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug What I did was simply run vllm serve Qwen/Qwen2-VL-7B-Instruct. Previously, I
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Qwen2VL doesn't work with TPU backend bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug What I did was simply run vllm serve Qwen/Qwen2-VL-7B-Instruct. Previously,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen2VL doesn't work with TPU backend bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug What I did was simply run vllm serve Qwen/Qwen2-VL-7B-Instruct. Previously,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
