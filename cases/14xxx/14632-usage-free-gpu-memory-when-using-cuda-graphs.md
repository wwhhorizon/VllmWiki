# vllm-project/vllm#14632: [Usage]: Free GPU memory when using CUDA graphs

| 字段 | 值 |
| --- | --- |
| Issue | [#14632](https://github.com/vllm-project/vllm/issues/14632) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Free GPU memory when using CUDA graphs

### Issue 正文摘录

### Your current environment . ### How would you like to use vllm Hello 👋 I am using vLLM library with engine v1.0. Everything is working fine in `eager_mode=True`. However, is order to boost performance I set it to `False` and relay on CUDA graphs kernels. There is a problem with my understanding whenever I can free GPU cards memory during inference process. I've got OOM memory kill despite the fact of using `torch.cuda.empty_cache()` method after every batch iteration. I guess it doesn't work with graphs kernels? Also, I've tried to play with `--max-seq-len-to-capture` engine's variable but with no positive effect. Am I missing something in therms of setting engine/environmental variables correctly? Below my example of engine init and env. variables. ```python vLLM_model = LLM( model=path, max_num_seqs=8192, max_num_batched_tokens=65536, tensor_parallel_size=4, pipeline_parallel_size=1, dtype="float16", trust_remote_code=True, limit_mm_per_prompt={"image": 10}, enforce_eager=False, enable_prefix_caching=True, enable_chunked_prefill=True, disable_custom_all_reduce=True, gpu_memory_utilization=0.9, max_seq_len_to_capture=2048, ) ``` ```bash export TORCH_CUDA_ARCH_LIST="9.0" export...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: port VLLM_USE_V1=1 export VLLM_WORKER_MULTIPROC_METHOD=spawn export VLLM_FLASHINFER_FORCE_TENSOR_CORES=1 export VLLM_LOGITS_PROCESSOR_THREADS=1 export CUDA_HOME=/net/software/aarch64/el8/CUDA/12.4.0/ export PATH="${CUDA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: Free GPU memory when using CUDA graphs usage ### Your current environment . ### How would you like to use vllm Hello 👋 I am using vLLM library with engine v1.0. Everything is working fine in `eager_mode=True`....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: tensor_parallel_size=4, pipeline_parallel_size=1, dtype="float16", trust_remote_code=True, limit_mm_per_prompt={"image": 10}, enforce_eager=False, enable_prefix_caching=True, enable_chunked_prefill=True, disable_custom_...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Usage]: Free GPU memory when using CUDA graphs usage ### Your current environment . ### How would you like to use vllm Hello 👋 I am using vLLM library with engine v1.0. Everything is working fine in `eager_mode=True`....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tly asked questions. performance model_support cuda;kernel oom dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
