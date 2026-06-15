# vllm-project/vllm#28230: [Bug]: GPU VRAM continuously increase during Qwen3-VL usage over days until OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#28230](https://github.com/vllm-project/vllm/issues/28230) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;gemm |
| 症状 | oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU VRAM continuously increase during Qwen3-VL usage over days until OOM

### Issue 正文摘录

### Your current environment Setup: docker run -d \ --runtime nvidia \ --gpus '"device=3,4,5,6"' \ -e TRANSFORMERS_OFFLINE=1 \ -e DEBUG="true" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:v0.11.0 \ --gpu-memory-utilization 0.95 \ --model Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 \ --tensor-parallel-size 4 \ --mm-encoder-tp-mode data \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --limit-mm-per-prompt.video 0 Server: 8*H200 with CUDA=12.6. ### 🐛 Describe the bug This is the same issue described in https://github.com/vllm-project/vllm/issues/27466 https://github.com/vllm-project/vllm/issues/27452 VRAM continuously increase over days after usage with vision. When available VRAM drops below 500MB, OOM occurs during new requests. As described in other posts, removing mm_encoder_tp_mode="data" or --enforce-eager does not work either. There is currently no acceptable solution. Is there a memory leakage? It is understood that VRAM usage may go up during vision task, but that should be cleared. VRAM cannot continuously increase and eventually hit OOM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n3-VL usage over days until OOM bug ### Your current environment Setup: docker run -d \ --runtime nvidia \ --gpus '"device=3,4,5,6"' \ -e TRANSFORMERS_OFFLINE=1 \ -e DEBUG="true" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: gpu-memory-utilization 0.95 \ --model Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 \ --tensor-parallel-size 4 \ --mm-encoder-tp-mode data \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --limit-mm-per-prompt.video 0 S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: call-parser hermes \ --limit-mm-per-prompt.video 0 Server: 8*H200 with CUDA=12.6. ### 🐛 Describe the bug This is the same issue described in https://github.com/vllm-project/vllm/issues/27466 https://github.com/vllm-proj...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: GPU VRAM continuously increase during Qwen3-VL usage over days until OOM bug ### Your current environment Setup: docker run -d \ --runtime nvidia \ --gpus '"device=3,4,5,6"' \ -e TRANSFORMERS_OFFLINE=1 \ -e DEBUG...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: g]: GPU VRAM continuously increase during Qwen3-VL usage over days until OOM bug ### Your current environment Setup: docker run -d \ --runtime nvidia \ --gpus '"device=3,4,5,6"' \ -e TRANSFORMERS_OFFLINE=1 \ -e DEBUG="t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
