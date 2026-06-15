# vllm-project/vllm#30904: [Bug]: Empty content on NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#30904](https://github.com/vllm-project/vllm/issues/30904) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;fp8 |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Empty content on NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

### Issue 正文摘录

### Your current environment System: Cant install collect_env.py but its an ubuntu 24 machine with 1 Blackwell RTX 6000 PRO and 128gb RAM, anyway all run inside the official VLLM image. ### 🐛 Describe the bug Docker running command: ``` docker run --rm --name "vllm_server_3000" --user root --runtime nvidia --gpus '"device=0"' --shm-size 2g --ipc=host \ -e HF_HUB_ENABLE_HF_TRANSFER="true" \ -e RAY_DEDUP_LOGS=1 -e VLLM_IMAGE_FETCH_TIMEOUT=15 \ -e HF_HOME="/data" \ -e VLLM_TEST_FORCE_FP8_MARLIN=1 \ -e VLLM_MARLIN_INPUT_DTYPE="fp8" \ -e VLLM_ATTENTION_BACKEND="FLASHINFER" \ -p 8000:8000 -v "$(pwd)/data_aphro/cache:/app/aphrodite-engine/.cache" -v "$(pwd)/data_aphro:/home/workspace" -v "$(pwd)/datafolder:/data" \ --entrypoint /bin/sh \ vllm/vllm-openai:lastest \ -c "python3 -m vllm.entrypoints.openai.api_server \ --download-dir '/data' -tp 1 --model 'nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8' --trust-remote-code \ --gpu-memory-utilization 0.8 --max-model-len 64000 --calculate-kv-scales \ --max-log-len 100000 --disable-log-requests --api-key 123 --reasoning-parser-plugin "/data/nano_v3_reasoning_parser.py" \ --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser nan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: motron-3-Nano-30B-A3B-FP8 bug ### Your current environment System: Cant install collect_env.py but its an ubuntu 24 machine with 1 Blackwell RTX 6000 PRO and 128gb RAM, anyway all run inside the official VLLM image. ###...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Empty content on NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 bug ### Your current environment System: Cant install collect_env.py but its an ubuntu 24 machine with 1 Blackwell RTX 6000 PRO and 128gb RAM, anyway all run in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: oot --runtime nvidia --gpus '"device=0"' --shm-size 2g --ipc=host \ -e HF_HUB_ENABLE_HF_TRANSFER="true" \ -e RAY_DEDUP_LOGS=1 -e VLLM_IMAGE_FETCH_TIMEOUT=15 \ -e HF_HOME="/data" \ -e VLLM_TEST_FORCE_FP8_MARLIN=1 \ -e VL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: l-len 64000 --calculate-kv-scales \ --max-log-len 100000 --disable-log-requests --api-key 123 --reasoning-parser-plugin "/data/nano_v3_reasoning_parser.py" \ --enable-auto-tool-choice --tool-call-parser qwen3_coder --re...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: _FP8_MARLIN=1 \ -e VLLM_MARLIN_INPUT_DTYPE="fp8" \ -e VLLM_ATTENTION_BACKEND="FLASHINFER" \ -p 8000:8000 -v "$(pwd)/data_aphro/cache:/app/aphrodite-engine/.cache" -v "$(pwd)/data_aphro:/home/workspace" -v "$(pwd)/datafo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
