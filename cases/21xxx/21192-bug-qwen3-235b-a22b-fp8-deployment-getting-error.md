# vllm-project/vllm#21192: [Bug]: Qwen3-235B-A22B-FP8 deployment getting error

| 字段 | 值 |
| --- | --- |
| Issue | [#21192](https://github.com/vllm-project/vllm/issues/21192) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-235B-A22B-FP8 deployment getting error

### Issue 正文摘录

### Your current environment error while Qwen3-235B-A22B-FP8 model deployment using 0.9.2 image tag ### 🐛 Describe the bug I was trying to deploy https://huggingface.co/Qwen/Qwen3-235B-A22B-FP8 model using 4XH100 GPUs, with below vllm confg: #echo "Checking GPU status..." #nvidia-smi echo "=== GPU Debug Info ===" nvidia-smi echo "CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES" echo "NVIDIA_VISIBLE_DEVICES: $NVIDIA_VISIBLE_DEVICES" echo "Available GPUs:" python3 -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'GPU count: {torch.cuda.device_count()}')" echo "=======================" # Start vLLM with error handling (I'm using vllm 0.9.2 image tag) vllm serve $MODEL_FOLDER \ --port $DEPLOY_PORT \ --served-model-name $DEPLOY_MODEL_NAME \ --max-model-len 32768 \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.95 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --max-num-batched-tokens 4096 \ --enable-chunked-prefill \ --enable-reasoning \ --reasoning-parser deepseek_r1 \ --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' \ --trust-remote-code I can see below logs: Available GPUs: CUDA available: True G...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: to deploy https://huggingface.co/Qwen/Qwen3-235B-A22B-FP8 model using 4XH100 GPUs, with below vllm confg: #echo "Checking GPU status..." #nvidia-smi echo "=== GPU Debug Info ===" nvidia-smi echo "CUDA_VISIBLE_DEVICES: $...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3-235B-A22B-FP8 deployment getting error bug;stale ### Your current environment error while Qwen3-235B-A22B-FP8 model deployment using 0.9.2 image tag ### 🐛 Describe the bug I was trying to deploy https://hug...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-235B-A22B-FP8 deployment getting error bug;stale ### Your current environment error while Qwen3-235B-A22B-FP8 model deployment using 0.9.2 image tag ### 🐛 Describe the bug I was trying to deploy https://hug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: BLE_DEVICES: $NVIDIA_VISIBLE_DEVICES" echo "Available GPUs:" python3 -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'GPU count: {torch.cuda.device_count()}')" echo "=====================...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3-235B-A22B-FP8 deployment getting error bug;stale ### Your current environment error while Qwen3-235B-A22B-FP8 model deployment using 0.9.2 image tag ### 🐛 Describe the bug I was trying to deploy https://hug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
