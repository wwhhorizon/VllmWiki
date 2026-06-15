# vllm-project/vllm#19577: [Bug]: Pre-built CPU vllm docker image exits out without error message

| 字段 | 值 |
| --- | --- |
| Issue | [#19577](https://github.com/vllm-project/vllm/issues/19577) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pre-built CPU vllm docker image exits out without error message

### Issue 正文摘录

### Your current environment Platform is Oracle Linux Server 8.10 (x86_64). Can't share specific details ### 🐛 Describe the bug Trying to do a setup with prebuilt vllm image for CPU. this is the call I'm trying. ``` docker run --privileged=true --shm-size=4g -p 8000:8000 -e VLLM_CPU_OMP_THREADS_BIND=0-31 -e VLLM_LOGGING_LEVEL=DEBUG -e NCCL_DEBUG=TRACE -e VLLM_TRACE_FUNCTION=1 public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.9.1 --model=meta-llama/Llama-3.2-1B-Instruct --dtype=bfloat16 ``` Image is from this repo ``` https://gallery.ecr.aws/q9t5s3a7/vllm-cpu-release-repo ``` The issue is that the container would exit out after this last output and doesn't show any reason why it crashes out. ``` DEBUG 06-12 19:58:31 [__init__.py:31] No plugins for group vllm.platform_plugins found. DEBUG 06-12 19:58:31 [__init__.py:35] Checking if TPU platform is available. DEBUG 06-12 19:58:31 [__init__.py:45] TPU platform is not available because: No module named 'libtpu' DEBUG 06-12 19:58:31 [__init__.py:52] Checking if CUDA platform is available. DEBUG 06-12 19:58:31 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBUG 06-12 19:58:31 [__init__.py:93...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 06-12 19:58:31 [__init__.py:52] Checking if CUDA platform is available. DEBUG 06-12 19:58:31 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBU...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Pre-built CPU vllm docker image exits out without error message bug;stale ### Your current environment Platform is Oracle Linux Server 8.10 (x86_64). Can't share specific details ### 🐛 Describe the bug Trying to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /vllm-cpu-release-repo:v0.9.1 --model=meta-llama/Llama-3.2-1B-Instruct --dtype=bfloat16 ``` Image is from this repo ``` https://gallery.ecr.aws/q9t5s3a7/vllm-cpu-release-repo ``` The issue is that the container would ex...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _TRACE_FUNCTION=1 public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.9.1 --model=meta-llama/Llama-3.2-1B-Instruct --dtype=bfloat16 ``` Image is from this repo ``` https://gallery.ecr.aws/q9t5s3a7/vllm-cpu-release-repo ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: riding a previously registered kernel for the same operator and the same dispatch key operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
