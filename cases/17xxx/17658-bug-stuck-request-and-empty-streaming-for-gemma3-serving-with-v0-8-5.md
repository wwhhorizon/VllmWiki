# vllm-project/vllm#17658: [Bug]: Stuck request and empty streaming for gemma3 serving with ^v0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#17658](https://github.com/vllm-project/vllm/issues/17658) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;quantization |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Stuck request and empty streaming for gemma3 serving with ^v0.8.5

### Issue 正文摘录

### Your current environment ok ### 🐛 Describe the bug I'm running VLLM with gemma3 and I've noticed with versions above (and including) v0.8.5, this model does not respond. ``` export MODEL_ID=ISTA-DASLab/gemma-3-27b-it-GPTQ-4b-128g export MODEL_ID_PORT=8000 export MODEL_ID_GPU=0 docker run \ --runtime nvidia \ -e VLLM_USE_V1=0 \ --ipc=host \ -p "${MODEL_ID_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VISIBLE_DEVICES=${MODEL_ID_GPU}" \ -v "${HF_HOME}:/root/.cache/huggingface" \ -v "VLLM_LOGGING_LEVEL=${VLLM_LOGGING_LEVEL}" \ vllm/vllm-openai:v0.8.5 \ --model ${MODEL_ID} \ --tokenizer google/gemma-3-27b-it \ --gpu-memory-utilization 0.9 \ --max-model-len 32000 \ --max_num_seqs 8 \ --served-model-name ista-daslab-gemma-3-27b-it-gptq-4b-128g ``` This the example request: ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "stream": false, "model": "ista-daslab-gemma-3-27b-it-gptq-4b-128g", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": [ {"type": "text", "text": "hello"} ]} ] }' ``` And the response is never delivered. What is interesting is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: # 🐛 Describe the bug I'm running VLLM with gemma3 and I've noticed with versions above (and including) v0.8.5, this model does not respond. ``` export MODEL_ID=ISTA-DASLab/gemma-3-27b-it-GPTQ-4b-128g export MODEL_ID_POR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Stuck request and empty streaming for gemma3 serving with ^v0.8.5 bug;stale ### Your current environment ok ### 🐛 Describe the bug I'm running VLLM with gemma3 and I've noticed with versions above (and including)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VISIBLE_DEVICES=${MODEL_ID_GPU}" \ -v "${HF_HOME}:/root/.cache/huggingface" \ -v "VLLM_LOGGING_LEVEL=${VLLM_LOGGING_LEVEL}" \ vllm/vllm-opena...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Stuck request and empty streaming for gemma3 serving with ^v0.8.5 bug;stale ### Your current environment ok ### 🐛 Describe the bug I'm running VLLM with gemma3 and I've noticed with versions above (and including)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: reases indefinetely: ``` INFO 05-05 07:16:33 [metrics.py:486] Avg prompt throughput: 1.9 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
