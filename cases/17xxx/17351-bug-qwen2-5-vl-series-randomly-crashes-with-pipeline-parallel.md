# vllm-project/vllm#17351: [Bug]: Qwen2.5-VL Series Randomly Crashes with Pipeline Parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#17351](https://github.com/vllm-project/vllm/issues/17351) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL Series Randomly Crashes with Pipeline Parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash export VLLM_ENGINE_ITERATION_TIMEOUT_S=300 export VLLM_USE_V1=0 CUDA_VISIBLE_DEVICES=4,5,6,7 vllm serve Qwen/Qwen2.5-VL-7B-Instruct \ --dtype bfloat16 \ --enforce-eager \ --gpu-memory-utilization 0.8 \ --tensor-parallel-size 2 \ --pipeline-parallel-size 2 \ --max_model_len 32768 ``` It randomly crashes when receiving around 300 requests with a Segmentation Fault. ``` INFO 04-29 04:15:30 [async_llm_engine.py:211] Added request chatcmpl-e92e5055cda04d308deb63c59b970483. INFO 04-29 04:15:30 [async_llm_engine.py:179] Finished request chatcmpl-7564a69f6a9c43b7a1884d9ddb3acff5. INFO: 127.0.0.1:34612 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 04-29 04:15:31 [async_llm_engine.py:179] Finished request chatcmpl-a03adbc6ef2a4f20a43e60ea8854ae15. INFO: 127.0.0.1:34772 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 04-29 04:15:31 [logger.py:39] Received request chatcmpl-6c3abda0ebe546bba9e2046db784549a: prompt: ' system\nYou are a helpful assistant. \n user\nHint: Please answer the question and provide the correct option letter, e.g., A, B, C, D, at the end.\nQuestion: What shape of a leaf is similar to Serrate, but has sm...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 0.0%. ^A 4 0x00000000003c56ec cuVDPAUCtxCreate() ???:0 5 0x00000000004fa310 cudbgMain() ???:0 6 0x000000000013d1d6 cuMemGetAttribute_v2() ???:0 7 0x000000000013d5f1 cuMemGetAttribute_v2() ???:0 8 0x000000000013e017 cuMe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Qwen2.5-VL Series Randomly Crashes with Pipeline Parallel bug;stale ### Your current environment ### 🐛 Describe the bug ```bash export VLLM_ENGINE_ITERATION_TIMEOUT_S=300 export VLLM_USE_V1=0 CUDA_VISIBLE_DEVICES...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _tokens=4096, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: A_VISIBLE_DEVICES=4,5,6,7 vllm serve Qwen/Qwen2.5-VL-7B-Instruct \ --dtype bfloat16 \ --enforce-eager \ --gpu-memory-utilization 0.8 \ --tensor-parallel-size 2 \ --pipeline-parallel-size 2 \ --max_model_len 32768 ``` It...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ```bash export VLLM_ENGINE_ITERATION_TIMEOUT_S=300 export VLLM_USE_V1=0 CUDA_VISIBLE_DEVICES=4,5,6,7 vllm serve Qwen/Qwen2.5-VL-7B-Instruct \ --dtype bfloat16 \ --enforce-eager \ --gpu-memory-utilization 0.8 \ --tensor-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
