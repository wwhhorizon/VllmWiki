# vllm-project/vllm#26479: [Bug]: 0.10.1 offline stop profiler error Can't disable Kineto profiler when it's not running

| 字段 | 值 |
| --- | --- |
| Issue | [#26479](https://github.com/vllm-project/vllm/issues/26479) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.10.1 offline stop profiler error Can't disable Kineto profiler when it's not running

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python model = vllm.LLM("/model/qwen3-8b-FP8") model.start_profile() model.generate("dddd") model.stop_profile() ``` ```shell error: (EngineCore_0 pid=18516) ERROR 10-09 09:40:09 [core.py:769] Invocation of profile method failed (EngineCore_0 pid=18516) ERROR 10-09 09:40:09 [core.py:769] Traceback (most recent call last): (EngineCore_0 pid=18516) ERROR 10-09 09:40:09 [core.py:769] File "/usr/local/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 766, in _handle_client_request (EngineCore_0 pid=18516) ERROR 10-09 09:40:09 [core.py:769] result = method(*self._convert_msgspec_args(method, args)) (EngineCore_0 pid=18516) ERROR 10-09 09:40:09 [core.py:769] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_0 pid=18516) ERROR 10-09 09:40:09 [core.py:769] File "/usr/local/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 356, in profile (EngineCore_0 pid=18516) ERROR 10-09 09:40:09 [core.py:769] self.model_executor.profile(is_start) (EngineCore_0 pid=18516) ERROR 10-09 09:40:09 [core.py:769] File "/usr/local/lib/python3.12/site-packages/vllm/v1/executor/abstract.py", line 96, in profile (EngineCore_0 pid...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding cuda;fp8;operator;triton build_error;c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ### 🐛 Describe the bug ```python model = vllm.LLM("/model/qwen3-8b-FP8") model.start_profile() model.generate("dddd") model.stop_profile() ``` ```shell error: (EngineCore_0 pid=18516) ERROR 10-09 09:40:09 [core.py:769]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: p profiler error Can't disable Kineto profiler when it's not running bug;stale ### Your current environment ### 🐛 Describe the bug ```python model = vllm.LLM("/model/qwen3-8b-FP8") model.start_profile() model.generate("...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: stale ### Your current environment ### 🐛 Describe the bug ```python model = vllm.LLM("/model/qwen3-8b-FP8") model.start_profile() model.generate("dddd") model.stop_profile() ``` ```shell error: (EngineCore_0 pid=18516)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
