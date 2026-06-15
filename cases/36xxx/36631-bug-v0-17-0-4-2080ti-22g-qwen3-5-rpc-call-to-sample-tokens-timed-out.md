# vllm-project/vllm#36631: [Bug]: v0.17.0 4*2080ti 22G Qwen3.5 RPC call to sample_tokens timed out.

| 字段 | 值 |
| --- | --- |
| Issue | [#36631](https://github.com/vllm-project/vllm/issues/36631) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.17.0 4*2080ti 22G Qwen3.5 RPC call to sample_tokens timed out.

### Issue 正文摘录

### Your current environment ``` docker run -d --name vllm-Qwen3.5 \ --gpus all \ --ipc=host \ --shm-size=64g \ -p 11435:8000 \ -v /home/ubuntu/models:/models \ vllm/vllm-openai:v0.17.0 \ --model /models/Qwen/Qwen3.5-35B-A3B-AWQ-4bit \ --served-model-name Qwen3.5-35B-A3B \ --api-key token-llm \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.90 \ --dtype half \ --kv-cache-dtype auto \ --block-size 16 \ --swap-space 4 \ --max-model-len 32768 \ --max-num-seqs 4 \ --max-cudagraph-capture-size 8 \ --reasoning-parser qwen3 \ --tool-call-parser qwen3_coder \ --enable-auto-tool-choice \ --default-chat-template-kwargs '{"enable_thinking": false}' \ --override-generation-config '{"temperature":0.7,"top_p":0.8,"top_k":20,"min_p":0.0,"presence_penalty":1.5,"repetition_penalty":1.0}' ``` ### 🐛 Describe the bug Log: ``` (APIServer pid=1) INFO: 192.168.5.200:61737 - "POST /v1/chat/completions HTTP/1.1" 200 OK (EngineCore_DP0 pid=188) INFO 03-10 09:22:02 [shm_broadcast.py:548] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). (EngineCore_D...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ne (v0.17.0) with config: model='/models/Qwen/Qwen3.5-35B-A3B-AWQ-4bit', speculative_config=None, tokenizer='/models/Qwen/Qwen3.5-35B-A3B-AWQ-4bit', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokeniz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: C call to sample_tokens timed out. bug ### Your current environment ``` docker run -d --name vllm-Qwen3.5 \ --gpus all \ --ipc=host \ --shm-size=64g \ -p 11435:8000 \ -v /home/ubuntu/models:/models \ vllm/vllm-openai:v0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: memory-utilization 0.90 \ --dtype half \ --kv-cache-dtype auto \ --block-size 16 \ --swap-space 4 \ --max-model-len 32768 \ --max-num-seqs 4 \ --max-cudagraph-capture-size 8 \ --reasoning-parser qwen3 \ --tool-call-pars...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: v0.17.0 4*2080ti 22G Qwen3.5 RPC call to sample_tokens timed out. bug ### Your current environment ``` docker run -d --name vllm-Qwen3.5 \ --gpus all \ --ipc=host \ --shm-size=64g \ -p 11435:8000 \ -v /home/ubunt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='qwen3', reasoning_par...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
