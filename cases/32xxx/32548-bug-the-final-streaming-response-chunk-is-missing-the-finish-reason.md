# vllm-project/vllm#32548: [Bug]: The final streaming response chunk is missing the finish_reason.

| 字段 | 值 |
| --- | --- |
| Issue | [#32548](https://github.com/vllm-project/vllm/issues/32548) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The final streaming response chunk is missing the finish_reason.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug docker run -d -t --gpus \"device=0,1,2,3,4,5,6,7\" --shm-size=512g \ --privileged \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ --name GLM-4.7-FP8 \ -p 8001:8000 \ -v /data/share/GLM-47-FP8:/root/GLM-47-FP8 \ vllm/vllm-openai:nightly-0d4044edd85de30d7d4558aeea4d1e95c7c556d6 \ --model /root/GLM-47-FP8 -tp 8 --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --served-model-name glm-4.7-fp8 \ --max-model-len 65536 \ --max-num-seqs 128 \ --gpu-memory-utilization 0.9 data: {"id":"chatcmpl-84152bfddeaa1570","object":"chat.completion.chunk","created":1768731088,"model":"glm-4.7-fp8","choices":[{"index":0,"delta":{"content":"上青","reasoning_content":null},"logprobs":null,"finish_reason":null,"token_ids":null}]} data: {"id":"chatcmpl-84152bfddeaa1570","object":"chat.completion.chunk","created":1768731088,"model":"glm-4.7-fp8","choices":[{"index":0,"delta":{"content":"天","reasoning_content":null},"logprobs":null,"finish_reason":"stop","stop_reason":151336,"token_ids":null}]} data: {"id":"chatcmpl-84152bfddeaa1570","object":"chat.co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: son. bug;stale ### Your current environment ### 🐛 Describe the bug docker run -d -t --gpus \"device=0,1,2,3,4,5,6,7\" --shm-size=512g \ --privileged \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ --name GLM-4.7-FP8 \ -p 80...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -privileged \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ --name GLM-4.7-FP8 \ -p 8001:8000 \ -v /data/share/GLM-47-FP8:/root/GLM-47-FP8 \ vllm/vllm-openai:nightly-0d4044edd85de30d7d4558aeea4d1e95c7c556d6 \ --model /root/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --gpus \"device=0,1,2,3,4,5,6,7\" --shm-size=512g \ --privileged \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ --name GLM-4.7-FP8 \ -p 8001:8000 \ -v /data/share/GLM-47-FP8:/root/GLM-47-FP8 \ vllm/vllm-openai:nightly-0d40...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vllm/vllm-openai:nightly-0d4044edd85de30d7d4558aeea4d1e95c7c556d6 \ --model /root/GLM-47-FP8 -tp 8 --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --tool-call-parser glm47 \ --reasoning...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g]: The final streaming response chunk is missing the finish_reason. bug;stale ### Your current environment ### 🐛 Describe the bug docker run -d -t --gpus \"device=0,1,2,3,4,5,6,7\" --shm-size=512g \ --privileged \ -e C...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
