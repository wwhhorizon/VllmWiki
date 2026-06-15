# vllm-project/vllm#16896: [Usage]: When deploying the GLM-4-32B BF16 model with vLLM 0.8.4, I encountered a GPU memory overflow

| 字段 | 值 |
| --- | --- |
| Issue | [#16896](https://github.com/vllm-project/vllm/issues/16896) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: When deploying the GLM-4-32B BF16 model with vLLM 0.8.4, I encountered a GPU memory overflow

### Issue 正文摘录

### Your current environment ```text ## environment： GPU： one node，4090 x 4，24G per GPU IMAGE: vllm/vllm-openai:0.8.4 MODEL: GLM-4-32B BF16, ## command : docker run -d --runtime nvidia --gpus 4 -p 8000:8000 -v /root/models:/root/models --env "TRANSFORMERS_OFFLINE=0" --env "HF_HUB_OFFLINE=0" -e "PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128" -e "PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True" -e "VLLM_USE_V1=0" --ipc=host --name=glm-4-32b vllm/vllm-openai:v0.8.4 --model /root/models/GLM-4-32B-0414 --trust-remote-code --served-model-name glm-4-32b --max_num_seqs 5 --max-model-len 16000 --tensor-parallel-size 4 --gpu_memory_utilization 0.75 --enforce-eager --model-impl transformers --kv-cache-dtype fp8 --disable-custom-all-reduce --enable-auto-tool-choice --tool-call-parser pythonic --compilation-config 0 ## Error: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 270.00 MiB. GPU 0 has a total capacity of 23.64 GiB of which 183.69 MiB is free. Process 503422 has 23.46 GiB memory in use. Of the allocated memory 22.91 GiB is allocated by PyTorch, and 2.00 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: When deploying the GLM-4-32B BF16 model with vLLM 0.8.4, I encountered a GPU memory overflow usage ### Your current environment ```text ## environment： GPU： one node，4090 x 4，24G per GPU IMAGE: vllm/vllm-openai...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: U IMAGE: vllm/vllm-openai:0.8.4 MODEL: GLM-4-32B BF16, ## command : docker run -d --runtime nvidia --gpus 4 -p 8000:8000 -v /root/models:/root/models --env "TRANSFORMERS_OFFLINE=0" --env "HF_HUB_OFFLINE=0" -e "PYTORCH_C...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: When deploying the GLM-4-32B BF16 model with vLLM 0.8.4, I encountered a GPU memory overflow usage ### Your current environment ```text ## environment： GPU： one node，4090 x 4，24G per GPU IMAGE: vllm/vllm-openai...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: When deploying the GLM-4-32B BF16 model with vLLM 0.8.4, I encountered a GPU memory overflow usage ### Your current environment ```text ## environment： GPU： one node，4090 x 4，24G per GPU IMAGE: vllm/vllm-openai:0.8.4 MO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: dels --env "TRANSFORMERS_OFFLINE=0" --env "HF_HUB_OFFLINE=0" -e "PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128" -e "PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True" -e "VLLM_USE_V1=0" --ipc=host --name=glm-4-32b vllm/v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
