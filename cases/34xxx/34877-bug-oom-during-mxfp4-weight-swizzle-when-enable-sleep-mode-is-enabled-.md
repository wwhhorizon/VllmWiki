# vllm-project/vllm#34877: [Bug]: OOM during mxfp4 weight swizzle when --enable-sleep-mode is enabled on single GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#34877](https://github.com/vllm-project/vllm/issues/34877) |
| 状态 | open |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM during mxfp4 weight swizzle when --enable-sleep-mode is enabled on single GPU

### Issue 正文摘录

### Your current environment - vLLM: `v0.16.0rc2.dev293+g2b84ac669` (nightly docker image `vllm/vllm-openai:nightly`) - GPU: 1x NVIDIA H100 94GB (93.10 GiB) - Model: mxfp4 quantized, 120B params, 15 safetensor shards ### 🐛 Describe the bug Loading an mxfp4-quantized 120B model with `--enable-sleep-mode` on a single H100 94GB OOMs during the post-load weight swizzle at `cumem_allocator.cpp:137`. Weights load fine (15/15 shards, ~11s), but the Hopper layout swizzle needs a 1.01 GiB temp buffer and all physical GPU memory is already committed via prior `cuMemCreate` calls. Removing `--enable-sleep-mode` from an otherwise identical command loads and serves the model without issue. **Reproduce:** ```bash docker run -d -it --gpus all \ --name gpt-oss-120b-vllm-sleep \ -p 9875:8000 --ipc=host --shm-size 32g \ -e VLLM_SERVER_DEV_MODE=1 \ -v /home/models/gpt-oss-120b:/models/gpt-oss-120b:ro \ vllm/vllm-openai:nightly \ --model /models/gpt-oss-120b \ --host 0.0.0.0 --port 8000 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.85 \ --max-model-len 8192 --max-num-seqs 2 \ --enable-chunked-prefill --enforce-eager \ --enable-sleep-mode \ --served-model-name gpt-oss-120b ``` **Error:** ```...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: our current environment - vLLM: `v0.16.0rc2.dev293+g2b84ac669` (nightly docker image `vllm/vllm-openai:nightly`) - GPU: 1x NVIDIA H100 94GB (93.10 GiB) - Model: mxfp4 quantized, 120B params, 15 safetensor shards ### 🐛 D...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: c669` (nightly docker image `vllm/vllm-openai:nightly`) - GPU: 1x NVIDIA H100 94GB (93.10 GiB) - Model: mxfp4 quantized, 120B params, 15 safetensor shards ### 🐛 Describe the bug Loading an mxfp4-quantized 120B model wit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: OOM during mxfp4 weight swizzle when --enable-sleep-mode is enabled on single GPU stale ### Your current environment - vLLM: `v0.16.0rc2.dev293+g2b84ac669` (nightly docker image `vllm/vllm-openai:nightly`) - GPU:...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: OOM during mxfp4 weight swizzle when --enable-sleep-mode is enabled on single GPU stale ### Your current environment - vLLM: `v0.16.0rc2.dev293+g2b84ac669` (nightly docker image `vllm/vllm-openai:nightly`) - GPU:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: age `vllm/vllm-openai:nightly`) - GPU: 1x NVIDIA H100 94GB (93.10 GiB) - Model: mxfp4 quantized, 120B params, 15 safetensor shards ### 🐛 Describe the bug Loading an mxfp4-quantized 120B model with `--enable-sleep-mode`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
