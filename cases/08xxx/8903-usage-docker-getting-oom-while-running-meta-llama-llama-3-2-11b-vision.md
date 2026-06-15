# vllm-project/vllm#8903: [Usage]: DOCKER - Getting OOM while running `meta-llama/Llama-3.2-11B-Vision-Instruct`

| 字段 | 值 |
| --- | --- |
| Issue | [#8903](https://github.com/vllm-project/vllm/issues/8903) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: DOCKER - Getting OOM while running `meta-llama/Llama-3.2-11B-Vision-Instruct`

### Issue 正文摘录

### Your current environment I'm trying to run `meta-llama/Llama-3.2-11B-Vision-Instruct` using vLLM docker: **GPU Server specifications:** - GPU Count: 4 - GPU Type: A100 - 80GB **vLLM Docker run command:** ```bash docker run --gpus all \ -v /data/hf_cache/ \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.2-11B-Vision-Instruct \ --tensor-parallel-size 4 \ --max-model-len 4096 \ --download_dir /data/vllm_cache \ --enforce-eager ``` ---- **Following is the issue which I'm facing:** ```bash VllmWorkerProcess pid=214) ERROR 09-27 05:20:38 multiproc_worker_utils.py:233] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks: CUDA out of memory. Tried to allocate 19.63 GiB. GPU 3 has a total capacity of 79.15 GiB of which 17.73 GiB is free. Process 78729 has 61.41 GiB memory in use. Of the allocated memory 56.64 GiB is allocated by PyTorch, and 4.07 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: DOCKER - Getting OOM while running `meta-llama/Llama-3.2-11B-Vision-Instruct` usage ### Your current environment I'm trying to run `meta-llama/Llama-3.2-11B-Vision-Instruct` using vLLM docker: **GPU Server spec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: DOCKER - Getting OOM while running `meta-llama/Llama-3.2-11B-Vision-Instruct` usage ### Your current environment I'm trying to run `meta-llama/Llama-3.2-11B-Vision-Instruct` using vLLM docker: **GPU Server spec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vLLM docker: **GPU Server specifications:** - GPU Count: 4 - GPU Type: A100 - 80GB **vLLM Docker run command:** ```bash docker run --gpus all \ -v /data/hf_cache/ \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p 8000:8000 \ --ip...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: UB_TOKEN= " \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.2-11B-Vision-Instruct \ --tensor-parallel-size 4 \ --max-model-len 4096 \ --download_dir /data/vllm_cache \ --enforce-eager...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: DOCKER - Getting OOM while running `meta-llama/Llama-3.2-11B-Vision-Instruct` usage ### Your current environment I'm trying to run `meta-llama/Llama-3.2-11B-Vision-Instruct` using vLLM docker: **GPU Server spec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
