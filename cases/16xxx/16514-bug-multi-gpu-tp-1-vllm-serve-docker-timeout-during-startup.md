# vllm-project/vllm#16514: [Bug]: Multi-GPU (TP > 1) vLLM serve docker timeout during startup

| 字段 | 值 |
| --- | --- |
| Issue | [#16514](https://github.com/vllm-project/vllm/issues/16514) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-GPU (TP > 1) vLLM serve docker timeout during startup

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello! ### Problem I've ran into an issue trying to serve a model in a multi-gpu setup (TP > 1). I used a docker compose script to launch the vllm container (provided below). When trying to serve a local `Qwen2.5-72B-Instruct` model (originally from HuggingFace), the start up hangs after vLLM on each worker finds the `nccl` lib, then just hangs (see the log below, `VLLM_TRACE_FUNCTION=1` and `VLLM_LOGGING_LEVEL=DEBUG` are set). While it is hanging, I noticed that one of the GPUs has full utilization (100% GPU Util, empty VRAM), while all others are idling: ### Repro attempts - Issue doesn't happen when TP up`. The Qwen model files should be downloaded and stored at `/model_storage` directory (I'm fairly certain the path to model can just be replaced by HF model ID and let it download, don't think this will change the outcome): ``` name: llm-common-qwen-72b services: vllm-server-qwen-72b: image: vllm/vllm-openai:latest container_name: vllm-qwen-72b-instruct command: > --model /model_storage/Qwen2.5-3B-Instruct --served-model-name vllm-qwen-72b --tensor-parallel-size 4 --enable-chunked-prefill --enable-prefix-caching --enable-auto-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Multi-GPU (TP > 1) vLLM serve docker timeout during startup bug ### Your current environment ### 🐛 Describe the bug Hello! ### Problem I've ran into an issue trying to serve a model in a multi-gpu setup (TP > 1)....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e the bug Hello! ### Problem I've ran into an issue trying to serve a model in a multi-gpu setup (TP > 1). I used a docker compose script to launch the vllm container (provided below). When trying to serve a local `Qwen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: name vllm-qwen-72b --tensor-parallel-size 4 --enable-chunked-prefill --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser hermes --host localhost --port 7201 --rope-scaling '{"factor": 4.0, "original_max...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;slowdown d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: vironment: - VLLM_LOGGING_LEVEL=DEBUG # for vllm debugging - CUDA_VISIBLE_DEVICES=0,1,2,3 - NVIDIA_VISIBLE_DEVICES=all # If running on GPU - NVIDIA_DRIVER_CAPABILITIES=compute,utility deploy: resources: reservations: de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
