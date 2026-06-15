# vllm-project/vllm#35991: [Installation]: Making server with GPT-OSS-20B on vllm+openwebui rtx5080 16gb

| 字段 | 值 |
| --- | --- |
| Issue | [#35991](https://github.com/vllm-project/vllm/issues/35991) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cache;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Making server with GPT-OSS-20B on vllm+openwebui rtx5080 16gb

### Issue 正文摘录

### Your current environment Could you please suggest a working Docker-compose file for running the gpt-oss-20b model on my Nvidia RTX 5080 16GB? I'm trying the vllm + openwebui + LiteLLM stack. The hugging face website for this model states that it's compatible with graphics cards with 16 VRAM. I've already tried the following: ``` networks: ai-net: driver: bridge services: vllm: image: vllm/vllm-openai:v0.10.1 container_name: gpt-oss-20b restart: unless-stopped runtime: nvidia environment: - NVIDIA_VISIBLE_DEVICES=all - PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True ports: - "8000:8000" volumes: - "/media/uadmin/Локальный диск/ai_work/models/gptoss_fromhf:/models" command: > --model /models --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.9 --max-model-len 4096 --quantization mxfp4 --dtype auto --trust-remote-code --tool-call-parser pythonic --reasoning-parser GptOss --enable-auto-tool-choice networks: - ai-net open-webui: image: ghcr.io/open-webui/open-webui:main container_name: open-webui-gui restart: unless-stopped ports: - "3000:8080" volumes: - "/media/uadmin/Локальный диск/ai_work/open-webui-data:/app/backend/data" environment: - OPENAI_API_BASE_URL=http://vllm:8000...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Making server with GPT-OSS-20B on vllm+openwebui rtx5080 16gb installation ### Your current environment Could you please suggest a working Docker-compose file for running the gpt-oss-20b model on my Nvidi
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 00 --gpu-memory-utilization 0.9 --max-model-len 4096 --quantization mxfp4 --dtype auto --trust-remote-code --tool-call-parser pythonic --reasoning-parser GptOss --enable-auto-tool-choice networks: - ai-net open-webui: i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Installation]: Making server with GPT-OSS-20B on vllm+openwebui rtx5080 16gb installation ### Your current environment Could you please suggest a working Docker-compose file for running the gpt-oss-20b model on my Nvid...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Installation]: Making server with GPT-OSS-20B on vllm+openwebui rtx5080 16gb installation ### Your current environment Could you please suggest a working Docker-compose file for running the gpt-oss-20b model on my Nvid...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: umes: - "/media/uadmin/Локальный диск/ai_work/open-webui-data:/app/backend/data" environment: - OPENAI_API_BASE_URL=http://vllm:8000/v1 - OPENAI_API_KEY=sk-local-admin depends_on: - vllm networks: - ai-net ``` It gives...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
