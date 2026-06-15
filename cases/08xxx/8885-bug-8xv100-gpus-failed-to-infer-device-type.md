# vllm-project/vllm#8885: [Bug]: 8xV100 gpus: Failed to infer device type

| 字段 | 值 |
| --- | --- |
| Issue | [#8885](https://github.com/vllm-project/vllm/issues/8885) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 8xV100 gpus: Failed to infer device type

### Issue 正文摘录

### Your current environment I'm trying to run inference in docker-compose, host: ubuntu 22.04 ``` uname -r 5.19.0-1010-nvidia-lowlatency ``` ``` version: '3.8' services: mixtral7x8b: image: vllm/vllm-openai:v0.5.5 restart: unless-stopped ports: - "100.73.239.219:8000:8000" volumes: - /opt/ai_models:/models deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] environment: - VLLM_API_KEY= # parameters for uvicorn (seconds) - TIMEOUT_KEEP_ALIVE=120 - TIMEOUT_GRACEFUL_SHUTDOWN=30 runtime: nvidia shm_size: 100gb command: > --host 0.0.0.0 --dtype=half --served-model-name Mixtral-8x7b --model /models/mistralai/Mixtral-8x7B-Instruct-v0.1 ``` ``` nvidia-smi Fri Sep 27 04:43:53 2024 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.90.12 Driver Version: 550.90.12 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+==================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ce type bug ### Your current environment I'm trying to run inference in docker-compose, host: ubuntu 22.04 ``` uname -r 5.19.0-1010-nvidia-lowlatency ``` ``` version: '3.8' services: mixtral7x8b: image: vllm/vllm-openai...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: : nvidia shm_size: 100gb command: > --host 0.0.0.0 --dtype=half --served-model-name Mixtral-8x7b --model /models/mistralai/Mixtral-8x7B-Instruct-v0.1 ``` ``` nvidia-smi Fri Sep 27 04:43:53 2024 +------------------------...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: --model /models/mistralai/Mixtral-8x7B-Instruct-v0.1 ``` ``` nvidia-smi Fri Sep 27 04:43:53 2024 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.90.12 Driver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ports: - "100.73.239.219:8000:8000" volumes: - /opt/ai_models:/models deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] environment: - VLLM_API_KEY= # parameters for uvicorn (
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: er='/models/mistralai/Mixtral-8x7B-Instruct-v0.1', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
