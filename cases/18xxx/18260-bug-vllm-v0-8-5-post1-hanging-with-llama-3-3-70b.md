# vllm-project/vllm#18260: [Bug]: vLLM v0.8.5.post1 hanging with Llama 3.3 70b

| 字段 | 值 |
| --- | --- |
| Issue | [#18260](https://github.com/vllm-project/vllm/issues/18260) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM v0.8.5.post1 hanging with Llama 3.3 70b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello folks, I've a Container running on Runpod, in which my container is restarting after waiting for a long time with the following message on vLLM: ``` 2025-05-16T13:12:16.645427617Z DEBUG 05-16 13:12:16 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} 2025-05-16T13:12:26.655452288Z DEBUG 05-16 13:12:26 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} 2025-05-16T13:12:36.666005080Z DEBUG 05-16 13:12:36 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} 2025-05-16T13:12:46.676453542Z DEBUG 05-16 13:12:46 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} 2025-05-16T13:12:56.686970595Z DEBUG 05-16 13:12:56 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} 2025-05-16T13:13:06.697525187Z DEBUG 05-16 13:13:06 [core_client.py:425] Waiting for 1 core engine proc(s) to start: {0} ``` This is happening with Llama 3.3 70b on the latest vLLM versions. Can someone help me in identifying what could be happening? Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: start: {0} ``` This is happening with Llama 3.3 70b on the latest vLLM versions. Can someone help me in identifying what could be happening? Thanks! ### Before submitting a new issue... - [x] Make sure you already searc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vLLM v0.8.5.post1 hanging with Llama 3.3 70b bug;stale ### Your current environment ### 🐛 Describe the bug Hello folks, I've a Container running on Runpod, in which my container is restarting after waiting for a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM v0.8.5.post1 hanging with Llama 3.3 70b bug;stale ### Your current environment ### 🐛 Describe the bug Hello folks, I've a Container running on Runpod, in which my container is restarting after waiting for a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
