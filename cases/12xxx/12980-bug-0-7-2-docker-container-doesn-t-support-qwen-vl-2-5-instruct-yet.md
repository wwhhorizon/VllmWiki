# vllm-project/vllm#12980: [Bug]: 0.7.2 Docker Container doesn't support Qwen VL 2.5 Instruct yet?

| 字段 | 值 |
| --- | --- |
| Issue | [#12980](https://github.com/vllm-project/vllm/issues/12980) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;gemm;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.7.2 Docker Container doesn't support Qwen VL 2.5 Instruct yet?

### Issue 正文摘录

### Your current environment Docker-based. ### 🐛 Describe the bug I start Docker VLLM Container like this: ```yaml services: vllm-qwen25-vl-72b: image: vllm/vllm-openai:v0.7.2 container_name: vllm-qwen25-vl-72b environment: - VLLM_NO_USAGE_STATS=1 - VLLM_USE_V1=1 ipc: host deploy: resources: reservations: devices: - driver: nvidia device_ids: ['0', '1', '2', '3'] capabilities: [ gpu ] network_mode: host volumes: - /mnt/sda/huggingface:/root/.cache/huggingface - .:/opt/vllm command: - --port=8003 - --model=Qwen/Qwen2.5-VL-72B-Instruct - --tensor-parallel-size=4 - --limit-mm-per-prompt=image=2 - --disable-log-requests - --swap-space=5 restart: unless-stopped ``` I get this as result: ```bash $ docker compose up [+] Running 1/0 ✔ Container vllm-qwen25-vl-72b Created 0.0s Attaching to vllm-qwen25-vl-72b vllm-qwen25-vl-72b | INFO 02-08 23:47:57 __init__.py:190] Automatically detected platform cuda. vllm-qwen25-vl-72b | INFO 02-08 23:47:59 api_server.py:840] vLLM API server version 0.7.2 vllm-qwen25-vl-72b | INFO 02-08 23:47:59 api_server.py:841] args: Namespace(host=None, port=8013, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: 0.7.2 Docker Container doesn't support Qwen VL 2.5 Instruct yet? bug ### Your current environment Docker-based. ### 🐛 Describe the bug I start Docker VLLM Container like this: ```yaml services: vllm-qwen25-vl-72b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: 0.7.2 Docker Container doesn't support Qwen VL 2.5 Instruct yet? bug ### Your current environment Docker-based. ### 🐛 Describe the bug I start Docker VLLM Container like this: ```yaml services: vllm-qwen25-vl-72b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: allel-size=4 - --limit-mm-per-prompt=image=2 - --disable-log-requests - --swap-space=5 restart: unless-stopped ``` I get this as result: ```bash $ docker compose up [+] Running 1/0 ✔ Container vllm-qwen25-vl-72b Created
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8013, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
