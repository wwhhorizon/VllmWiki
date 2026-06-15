# vllm-project/vllm#10478: [Bug]: vLLM CPU mode broken Unable to get JIT kernel for brgemm

| 字段 | 值 |
| --- | --- |
| Issue | [#10478](https://github.com/vllm-project/vllm/issues/10478) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM CPU mode broken Unable to get JIT kernel for brgemm

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Seems oneDNN is missing in latest Dockerfile or at least some part of it seems missing. This used to work in v0.6.3 fine though. I was suspecting this PR since it touched how oneDNN is included: https://github.com/vllm-project/vllm/pull/9344 Steps to reproduce: 1. Git clone vllm repo latest main branch or v0.6.4.post1 2. Build the cpu docker image: `docker build -t test-cpu -f Dockerfile.cpu .` 3. Run the openai server: ``` docker run -d --name vllm -p 8000:8000 -e VLLM_LOGGING_LEVEL=DEBUG -e ONEDNN_VERBOSE=all -e VLLM_WORKER_MULTIPROC_METHOD=spawn test-cpu --model facebook/opt-125m --disable-frontend-multiprocessing ``` 4. Wait for server to be ready and then send a simple prompt: ``` curl -v --fail-with-body --show-error http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "facebook/opt-125m", "prompt": "San Francisco is a", "max_tokens": 7, "temperature": 0 }' ``` Full logs: ``` INFO 11-20 06:32:30 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. INFO 11-20 06:32:31 api_server.py:592] vLLM API ser...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: _No response_ ### 🐛 Describe the bug Seems oneDNN is missing in latest Dockerfile or at least some part of it seems missing. This used to work in v0.6.3 fine though. I was suspecting this PR since it touched how oneDNN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: vLLM CPU mode broken Unable to get JIT kernel for brgemm bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Seems oneDNN is missing in latest Dockerfile or at least...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: perature": 0 }' ``` Full logs: ``` INFO 11-20 06:32:30 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. INFO 11-20 06:32:31 api_server.py:592] vLLM API server...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: get JIT kernel for brgemm bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Seems oneDNN is missing in latest Dockerfile or at least some part of it seems missing. This us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
