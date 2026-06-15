# vllm-project/vllm#21685: [Bug]: Waiting on local engine process -  FP8 model streaming Qwen3-Coder-480B-FP8 via Run:AI streamer from S3 with LWS in K8s

| 字段 | 值 |
| --- | --- |
| Issue | [#21685](https://github.com/vllm-project/vllm/issues/21685) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Waiting on local engine process -  FP8 model streaming Qwen3-Coder-480B-FP8 via Run:AI streamer from S3 with LWS in K8s

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I deploy the model with a `LeaderWorkerSet` there's no error message, or help to be found from the logs which explains why a local engine process is waiting. This makes debugging difficult. In my case I am using the `Run:AI Streamer` to load my model from a local S3 compatible bucket to have quick load-times of the safetensors. That being said, it was not clear from the documentation how this works when deploying vLLM for distributed inference. In the midst of loading the weights, the process simply stalls and logs are as follows: ``` (RayWorkerWrapper pid=596) Loading safetensors using Runai Model Streamer: 2% Completed | 1133/60329 [00:31<27:42, 35.61it/s] (RayWorkerWrapper pid=596) DEBUG 07-27 10:13:56 [utils.py:741] Waiting for 1 local, 0 remote core engine proc(s) to start. DEBUG 07-27 10:14:06 [utils.py:741] Waiting for 1 local, 0 remote core engine proc(s) to start. DEBUG 07-27 10:14:16 [utils.py:741] Waiting for 1 local, 0 remote core engine proc(s) to start. ``` First of all, it would be good with more details about which engine process is causing the wait to happen. Secondly, if this is due to an error of some sort...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;samp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Waiting on local engine process - FP8 model streaming Qwen3-Coder-480B-FP8 via Run:AI streamer from S3 with LWS in K8s bug ### Your current environment ### 🐛 Describe the bug When I deploy the model with a `Leade...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Waiting on local engine process - FP8 model streaming Qwen3-Coder-480B-FP8 via Run:AI streamer from S3 with LWS in K8s bug ### Your current environment ### 🐛 Describe the bug When I deploy the model with a `Leade...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Waiting on local engine process - FP8 model streaming Qwen3-Coder-480B-FP8 via Run:AI streamer from S3 with LWS in K8s bug ### Your current environment ### 🐛 Describe the bug When I deploy the model with a `Leade...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
