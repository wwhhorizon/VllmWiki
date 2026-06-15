# vllm-project/vllm#14547: [Bug]: RuntimeError: Found Tesla P100-SXM2-16GB which is too old to be supported by the triton GPU compiler, which is used as the backend. Triton only supports devices of CUDA Capability >= 7.0, but your device is of CUDA capability 6.0

| 字段 | 值 |
| --- | --- |
| Issue | [#14547](https://github.com/vllm-project/vllm/issues/14547) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Found Tesla P100-SXM2-16GB which is too old to be supported by the triton GPU compiler, which is used as the backend. Triton only supports devices of CUDA Capability >= 7.0, but your device is of CUDA capability 6.0

### Issue 正文摘录

### Your current environment `root@node38:/disk1/Qwen2.5-72B-Instruct-GPTQ-Int4# vi docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.7.3 container_name: qwen2.5-72b-int4 restart: always runtime: nvidia - 8002:8000 - /disk1/:/models --served-model-name=Qwen2.5-72B-Instruct-GPTQ-Int4 device_ids: [ "0","1","2","3" ] ipc: host vllm: ~ networks: "docker-compose.yml" [dos] 30L, 765B written root@node38:/disk1/Qwen2.5-72B-Instruct-GPTQ-Int4# docker ps CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES root@node38:/disk1/Qwen2.5-72B-Instruct-GPTQ-Int4# docker compose -f docker-compose.yml down root@node38:/disk1/Qwen2.5-72B-Instruct-GPTQ-Int4# docker compose -f docker-compose.yml up -d [+] Running 0/0 ⠋ Network qwen25-72b-instruct-gptq-int4_default Creating 0.1s [+] Running 1/1 ✔ Network qwen25-72b-instruct-gptq-int4_default Created 0.1s ⠋ Container qwen2.5-72b-int4 Creating 0.0s [+] Running 1/2 ✔ Network qwen25-72b-instruct-gptq-int4_default Created 0.1s ⠿ Container qwen2.5-72b-int4 Starting 0.1s [+] Running 1/2 ✔ Network qwen25-72b-instruct-gptq-int4_default Created 0.1s ⠿ Container qwen2.5-72b-int4 Starting 0.2s [+] Running 1/2 ✔ Network qwe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Tesla P100-SXM2-16GB which is too old to be supported by the triton GPU compiler, which is used as the backend. Triton only supports devices of CUDA Capability >= 7.0, but your device is of CUDA capability 6.0 bug;stale...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: of CUDA Capability >= 7.0, but your device is of CUDA capability 6.0 bug;stale ### Your current environment `root@node38:/disk1/Qwen2.5-72B-Instruct-GPTQ-Int4# vi docker-compose.yml version: '3.3' services: # vllm vllm-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: Your current environment `root@node38:/disk1/Qwen2.5-72B-Instruct-GPTQ-Int4# vi docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.7.3 container_name: qwen2.5-72b-int4 restart: al...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: pability 6.0 bug;stale ### Your current environment `root@node38:/disk1/Qwen2.5-72B-Instruct-GPTQ-Int4# vi docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.7.3 container_name: q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
