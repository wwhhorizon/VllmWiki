# vllm-project/vllm#30819: [Bug]: vLLM inference stuck when requesting video description on VLM models

| 字段 | 值 |
| --- | --- |
| Issue | [#30819](https://github.com/vllm-project/vllm/issues/30819) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM inference stuck when requesting video description on VLM models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Commit ID: 66c3537e5df215d8095d7042b8e7abd51260393f When serving VLMs (tested with Qwen (Qwen/Qwen2.5-VL-3B-Instruct, Qwen/Qwen2.5-VL-7B-Instruct) and cosmos reason1 (nvidia/cosmos-reason1-7b), vLLM get stuck when requesting video decoding. Installed vLLM following these instructions: > Install uv if you don't have it already. git clone ... cd to repo uv venv --python 3.12 --seed Enter generated venv VLLM_USE_PRECOMPILED=1 uv pip install -e . Done! Ran vLLM with the following command: ```bash vllm serve Qwen/Qwen2.5-VL-3B-Instruct --trust-remote-code --tensor-parallel-size 1 --max-model-len 65536 --gpu-memory-utilization 0.6 --no-enforce-eager --mm-processor-cache-gb 0 --max-num-seqs 64 --no-enable-prefix-caching --api-server-count 3 --media-io-kwargs '{"video":{"fps":1}}' --mm-processor-kwargs '{"max_pixels": 151200}' ``` Ran a local http server to serve videos from `sharegpt/zip_folder/panda`: ```bash cd /path/to/sharegpt/zip_folder/panda python3 -m http.server 8080 ``` Performed a curl request to vllm after initialization completed: ```bash curl -sS -X POST 'http://0.0.0.0:8000/v1/chat/completions' \ -H 'Content-Type: applicat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: idia/cosmos-reason1-7b), vLLM get stuck when requesting video decoding. Installed vLLM following these instructions: > Install uv if you don't have it already. git clone ... cd to repo uv venv --python 3.12 --seed Enter...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vLLM inference stuck when requesting video description on VLM models bug;stale ### Your current environment ### 🐛 Describe the bug Commit ID: 66c3537e5df215d8095d7042b8e7abd51260393f When serving VLMs (tested wit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: th Qwen (Qwen/Qwen2.5-VL-3B-Instruct, Qwen/Qwen2.5-VL-7B-Instruct) and cosmos reason1 (nvidia/cosmos-reason1-7b), vLLM get stuck when requesting video decoding. Installed vLLM following these instructions: > Install uv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vLLM inference stuck when requesting video description on VLM models bug;stale ### Your current environment ### 🐛 Describe the bug Commit ID: 66c3537e5df215d8095d7042b8e7abd51260393f When serving VLMs (tested wit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _porting;model_support;multimodal_vlm;sampling_logits cuda;gemm;operator;triton build_error;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
