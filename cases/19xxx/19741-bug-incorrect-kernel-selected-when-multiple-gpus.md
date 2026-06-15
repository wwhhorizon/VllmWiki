# vllm-project/vllm#19741: [Bug]: Incorrect kernel selected when multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#19741](https://github.com/vllm-project/vllm/issues/19741) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect kernel selected when multiple GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running docker image with following params: ``` docker run --name vllm-qwen3-30b --rm --gpus all --init -e "CUDA_VISIBLE_DEVICES=1,2" -e "VLLM_ATTENTION_BACKEND=FLASH_ATTN" -e "VLLM_USE_V1=0" -e "CUDA_DEVICE_ORDER=PCI_BUS_ID" -v "\\wsl$\Ubuntu\home\unat\vllm\huggingface:/root/.cache/huggingface" -v "\\wsl$\Ubuntu\home\unat\vllm\cache:/root/.cache/vllm" -p ${PORT}:8000 --ipc=host vllm/vllm-openai:v0.9.0.1 --model /root/.cache/huggingface/Qwen3-30B-A3B-FP8 -tp 2 --enable-expert-parallel --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser qwen3 --max-model-len 65536 --served-model-name qwen3-30b --max-seq-len-to-capture 65536 --max_num_seqs 2 --cuda_graph_sizes 4 --rope-scaling {\"rope_type\":\"yarn\",\"factor\":2.0,\"original_max_position_embeddings\":32768} --gpu-memory-utilization 0.95 --enable-prefix-caching --enable-chunked-prefill --dtype half ``` * CUDA0 - 5090 * CUDA1 - 4090 * CUDA2 - 3090 And it crashes with error `ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')")`. But same parameters on same system works fine with RTX3090 + RTX3090. Now...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ale ### Your current environment ### 🐛 Describe the bug I'm running docker image with following params: ``` docker run --name vllm-qwen3-30b --rm --gpus all --init -e "CUDA_VISIBLE_DEVICES=1,2" -e "VLLM_ATTENTION_BACKEN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: docker run --name vllm-qwen3-30b --rm --gpus all --init -e "CUDA_VISIBLE_DEVICES=1,2" -e "VLLM_ATTENTION_BACKEND=FLASH_ATTN" -e "VLLM_USE_V1=0" -e "CUDA_DEVICE_ORDER=PCI_BUS_ID" -v "\\wsl$\Ubuntu\home\unat\vllm\huggingf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llm-openai:v0.9.0.1 --model /root/.cache/huggingface/Qwen3-30B-A3B-FP8 -tp 2 --enable-expert-parallel --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser qwen3 --max-model-len 65536 --served-model-nam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ng docker image with following params: ``` docker run --name vllm-qwen3-30b --rm --gpus all --init -e "CUDA_VISIBLE_DEVICES=1,2" -e "VLLM_ATTENTION_BACKEND=FLASH_ATTN" -e "VLLM_USE_V1=0" -e "CUDA_DEVICE_ORDER=PCI_BUS_ID...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Incorrect kernel selected when multiple GPUs bug;stale ### Your current environment ### 🐛 Describe the bug I'm running docker image with following params: ``` docker run --name vllm-qwen3-30b --rm --gpus all --in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
