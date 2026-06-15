# vllm-project/vllm#8963: [Bug]:  Device-side assertion `false' failed, while starting vllm server.

| 字段 | 值 |
| --- | --- |
| Issue | [#8963](https://github.com/vllm-project/vllm/issues/8963) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Device-side assertion `false' failed, while starting vllm server.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When the vllm server is started via: ``` vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 2 ``` Before the server starts it starts to spam ``` /vllm-workspace/build/temp.linux-x86_64-cpython-39/csrc/rocm/attention.hip:896: void paged_attention_ll4mi_QKV_kernel(const scalar_t *__restrict, const cache_t *__restrict, const cache_t *__restrict, const int, const float, const int *__restrict, const int *__restrict, const int, const float *__restrict, const int, const int, const int, float *__restrict, float *__restrict, scalar_t *__restrict, scalar_t *__restrict, int, float, float) [scalar_t = __hip_bfloat16, cache_t = __hip_bfloat16, KV_DTYPE = vllm::Fp8KVCacheDataType::kAuto, BLOCK_SIZE = 16, HEAD_SIZE = 128, NUM_THREADS = 512, GQA_RATIO = 4]: Device-side assertion `false' failed. ``` until I force quit the container. I'm using the current latest commit (2ae25f79cf1e8d21f7bcba097e4c039463c22be4).

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: *__restrict, scalar_t *__restrict, int, float, float) [scalar_t = __hip_bfloat16, cache_t = __hip_bfloat16, KV_DTYPE = vllm::Fp8KVCacheDataType::kAuto, BLOCK_SIZE = 16, HEAD_SIZE = 128, NUM_THREADS = 512, GQA_RATIO = 4]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ze 2 ``` Before the server starts it starts to spam ``` /vllm-workspace/build/temp.linux-x86_64-cpython-39/csrc/rocm/attention.hip:896: void paged_attention_ll4mi_QKV_kernel(const scalar_t *__restrict, const cache_t *__...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : Device-side assertion `false' failed, while starting vllm server. bug;rocm ### Your current environment ### 🐛 Describe the bug When the vllm server is started via: ``` vllm serve meta-llama/Llama-3.1-8B-Instruct --ten...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: Device-side assertion `false' failed, while starting vllm server. bug;rocm ### Your current environment ### 🐛 Describe the bug When the vllm server is started via: ``` vllm serve meta-llama/Llama-3.1-8B-Instruct...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: scribe the bug When the vllm server is started via: ``` vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 2 ``` Before the server starts it starts to spam ``` /vllm-workspace/build/temp.linux-x86_64-cpy...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
