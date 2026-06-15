# vllm-project/vllm#12798: [Bug]: Engine process died when serving DeepSeekVL2

| 字段 | 值 |
| --- | --- |
| Issue | [#12798](https://github.com/vllm-project/vllm/issues/12798) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine process died when serving DeepSeekVL2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## how to run 1. using official image v0.7.1. 2. reinstall vllm to use the latest code: `pip uninstall -y vllm && pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly` 3. start the container: ``` docker run -d --rm --network=host --name=vllm-deepseekvl2 \ --gpus all \ -v $MODEL:/model \ -e VLLM_LOGGING_LEVEL=DEBUG \ $IMAGE \ --model /model \ -tp 4 \ --disable-log-stats \ --port 23333 \ --hf_overrides '{"architectures": ["DeepseekVLV2ForCausalLM"]}' \ --chat-template /vllm-workspace/examples/template_deepseek_vl2.jinja \ --max-model-len 4096 \ --gpu-memory-utilization 0.95 \ --max-num-batched-tokens 8192 ``` 4. send requests to the server. ## the error Engine dies after dozens of requests. The log: ``` INFO 02-05 01:20:00 engine.py:275] Added request chatcmpl-87294cc938af457f9628dd82be72189c. ERROR 02-05 01:21:05 client.py:300] RuntimeError('Engine process (pid 76) died.') ERROR 02-05 01:21:05 client.py:300] NoneType: None CRITICAL 02-05 01:21:10 launcher.py:101] MQLLMEngine is already dead, terminating server process INFO: 10.44.128.16:28304 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error INFO:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rrent environment ### 🐛 Describe the bug ## how to run 1. using official image v0.7.1. 2. reinstall vllm to use the latest code: `pip uninstall -y vllm && pip install vllm --pre --extra-index-url https://wheels.vllm.ai/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Engine process died when serving DeepSeekVL2 bug;stale ### Your current environment ### 🐛 Describe the bug ## how to run 1. using official image v0.7.1. 2. reinstall vllm to use the latest code: `pip uninstall -y...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: del \ -tp 4 \ --disable-log-stats \ --port 23333 \ --hf_overrides '{"architectures": ["DeepseekVLV2ForCausalLM"]}' \ --chat-template /vllm-workspace/examples/template_deepseek_vl2.jinja \ --max-model-len 4096 \ --gpu-me...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: run -d --rm --network=host --name=vllm-deepseekvl2 \ --gpus all \ -v $MODEL:/model \ -e VLLM_LOGGING_LEVEL=DEBUG \ $IMAGE \ --model /model \ -tp 4 \ --disable-log-stats \ --port 23333 \ --hf_overrides '{"architectures":...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
