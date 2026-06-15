# vllm-project/vllm#25528: [Bug]: Big performance regress on V100/2080Ti using FlexAttention backend on V1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#25528](https://github.com/vllm-project/vllm/issues/25528) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Big performance regress on V100/2080Ti using FlexAttention backend on V1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Serve DeepSeek-R1-Distill-Qwen-32B with last VLLM 0.10.2 ``` CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve ./DeepSeek-R1-Distill-Qwen-32B --served-model-name DeepSeek-R1-Distill-Qwen-32B default --port 7866 --dtype half --trust-remote-code --disable-log-requests --gpu-memory-utilization 0.9 --max-model-len 32768 --max_num_seqs 24 -tp 4 --max-seq-len-to-capture 32768 ``` test with single request, server crashed. ``` curl ${BASE_URL}/chat/completions -H "Authorization: Bearer $OAI_KEY" -H "Content-Type: application/json" -d '{ "model": "default", "messages": [ {"role": "user", "content": "tell me something about LLM?"} ], "max_tokens": 512 }' ``` Serve DeepSeek-R1-Distill-Qwen-32B GGUF with last VLLM 0.10.2 ``` CUDA_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.openai.api_server --served-model-name DeepSeek-R1-Distill-Qwen-32B default --model DeepSeek-R1-Distill-Qwen-32B-Q5_K_M.gguf --port 7866 --dtype half --trust-remote-code --gpu-memory-utilization 0.9 --max-model-len 32768 --max_num_seqs 24 -tp 2 --max-seq-len-to-capture 32768 -O2 ``` Test with single request, token generate speed is 15.3 tokens/s. Test with 8 concurrent request, to...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: urrent environment ### 🐛 Describe the bug Serve DeepSeek-R1-Distill-Qwen-32B with last VLLM 0.10.2 ``` CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve ./DeepSeek-R1-Distill-Qwen-32B --served-model-name DeepSeek-R1-Distill-Qwen-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampli...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Big performance regress on V100/2080Ti using FlexAttention backend on V1 engine bug ### Your current environment ### 🐛 Describe the bug Serve DeepSeek-R1-Distill-Qwen-32B with last VLLM 0.10.2 ``` CUDA_VISIBLE_DE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: be the bug Serve DeepSeek-R1-Distill-Qwen-32B with last VLLM 0.10.2 ``` CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve ./DeepSeek-R1-Distill-Qwen-32B --served-model-name DeepSeek-R1-Distill-Qwen-32B default --port 7866 --dtype...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n-32B default --port 7866 --dtype half --trust-remote-code --disable-log-requests --gpu-memory-utilization 0.9 --max-model-len 32768 --max_num_seqs 24 -tp 4 --max-seq-len-to-capture 32768 ``` test with single request, s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
