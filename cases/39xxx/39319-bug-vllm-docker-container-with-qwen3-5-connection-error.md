# vllm-project/vllm#39319: [Bug]: vLLM docker container with Qwen3.5 - Connection error

| 字段 | 值 |
| --- | --- |
| Issue | [#39319](https://github.com/vllm-project/vllm/issues/39319) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM docker container with Qwen3.5 - Connection error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Good morning everyone, I am trying to develop an agent using LangGraph and I started with Ollama. Now I wanted to switch to vLLM (so I am new to it), using Qwen3.5-9b and Qwen3-14b. I have already downloaded them locally and I can find them in my hub dir of HuggingFace. Following several tutorials, I wrote this yaml file to launch three different docker containers for three different LLMs in background while I am running the main agent. here is the file: ``` services: vllm_main_agent: image: vllm/vllm-openai container_name: vllm_main_agent runtime: nvidia ipc: host ports: - "8000:8000" volumes: - ~/.cache/huggingface:/root/.cache/huggingface environment: - NVIDIA_VISIBLE_DEVICES=0 - NVIDIA_DRIVER_CAPABILITIES=compute,utility restart: unless-stopped command: > --model Qwen/Qwen3.5-9B --trust-remote-code --tensor-parallel-size 1 --max-model-len 40960 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-prefix-caching --gdn-prefill-backend triton vllm_mem0_extractor: image: vllm/vllm-openai container_name: vllm_mem0_extractor runtime: nvidia ipc: host ports: - "8001:8000" volumes: - ~/.cache/hug...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: vLLM docker container with Qwen3.5 - Connection error bug ### Your current environment ### 🐛 Describe the bug Good morning everyone, I am trying to develop an agent using LangGraph and I started with Ollama. Now...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: all-parser qwen3_coder --enable-prefix-caching --gdn-prefill-backend triton vllm_mem0_extractor: image: vllm/vllm-openai container_name: vllm_mem0_extractor runtime: nvidia ipc: host ports: - "8001:8000" volumes: - ~/.c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM docker container with Qwen3.5 - Connection error bug ### Your current environment ### 🐛 Describe the bug Good morning everyone, I am trying to develop an agent using LangGraph and I started with Ollama. Now...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ad model Qwen/Qwen3-14B-AWQ... (EngineCore pid=445) INFO 04-08 16:07:23 [cuda.py:334] Using FLASH_ATTN attention backend out of potential backends: ['FLASH_ATTN', 'FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION']. (EngineC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: --tool-call-parser qwen3_coder --enable-prefix-caching --gdn-prefill-backend triton vllm_mem0_extractor: image: vllm/vllm-openai container_name: vllm_mem0_extractor runtime: nvidia ipc: host ports: - "8001:8000" volumes...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
