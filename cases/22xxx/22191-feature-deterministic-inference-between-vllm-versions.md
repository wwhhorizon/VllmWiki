# vllm-project/vllm#22191: [Feature]: Deterministic inference between vllm versions

| 字段 | 值 |
| --- | --- |
| Issue | [#22191](https://github.com/vllm-project/vllm/issues/22191) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | nondeterministic |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Deterministic inference between vllm versions

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I don't know if it's feasible, but maybe something can be done. With the right settings you can have deterministic inference using vllm. First screen show output from the attached script using vllm in version 0.9.0 Second screen show output from version 0.10.0 Script, the main part that runs in a loop: ```python messages = [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Generate random thoughts. /no_think"} ] # Call the hosted vLLM server via LiteLLM stream_iter = litellm.completion( model="hosted_vllm/llm", api_base="http://10.232.29.88:8000/v1/", messages=messages, stream=True, temperature=0, max_tokens=1000, ) for part in stream_iter: print(part.choices[0].delta.content or "", end="", flush=True) ``` vllm arguments (maybe this will be helpful for someone): ```bash docker run --runtime nvidia --gpus all -d --name vllm-Qwen3-32B --restart unless-stopped -v ~/.cache/vllm:/root/.cache/vllm -v ~/.cache/huggingface:/root/.cache/huggingface -e VLLM_FLASH_ATTN_VERSION=2 -e VLLM_USE_V1=1 -e VLLM_USE_FLASHINFER_SAMPLER=0 -e VLLM_TEST_DYNAMO_FULLGRAPH_CAPTURE=1 -e VLLM_ATTENTION_BACKEND=FLASH_ATTN -e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Feature]: Deterministic inference between vllm versions feature request;stale ### 🚀 The feature, motivation and pitch Hi, I don't know if it's feasible, but maybe something can be done. With the right settings you can...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: KUP_COUNT=0 -p 8000:8000 vllm/vllm-openai:v0.10.0 --model Qwen/Qwen3-32B-FP8 --served-model-name llm --max-model-len 26060 --max-seq-len-to-capture 26060 --max-num-batched-tokens 26060 --block-size 32 --gpu-memory-utili...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: NAMO_FULLGRAPH_CAPTURE=1 -e VLLM_ATTENTION_BACKEND=FLASH_ATTN -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True -e VLLM_ENABLE_V1_MULTIPROCESSING=1 -e MAX_JOBS=32 -e VLLM_USE_PRECOMPILED=true -e RAY_ROTATION_MAX_BYTES...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ed vLLM server via LiteLLM stream_iter = litellm.completion( model="hosted_vllm/llm", api_base="http://10.232.29.88:8000/v1/", messages=messages, stream=True, temperature=0, max_tokens=1000, ) for part in stream_iter: p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Deterministic inference between vllm versions feature request;stale ### 🚀 The feature, motivation and pitch Hi, I don't know if it's feasible, but maybe something can be done. With the right settings you can...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
