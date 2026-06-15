# vllm-project/vllm#2654: Call for Help: Proper Build System (CMake, Bazel, etc). 

| 字段 | 值 |
| --- | --- |
| Issue | [#2654](https://github.com/vllm-project/vllm/issues/2654) |
| 状态 | closed |
| 标签 | help wanted |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Call for Help: Proper Build System (CMake, Bazel, etc). 

### Issue 正文摘录

Currently vLLM's compilation tool uses PyTorch's extension builders, which calls Ninja under the hood. This works okay but have the following issues: * Only supports NVIDIA and AMD GPUs. * Slow sequential builds. This is amplified by adding quantization kernels and LoRA kernels. * No caching and incremental builds. We would liked to ask for community's help on recommending a technology, prototype, and implement it. Ideally something like CMake or Bazel could work but it requires some careful thinking. The requirements: * Must support multiple hardware architecture (NVIDIA, AMD, Intel, etc). * Must support incremental build, which also implies caching. * Must support parallelizable build. * Good to have editor support (by generating compilation database). * Ideally it would not OOM like current setup. Currently due to the rigid structure, we have to carefully set `MAX_JOBS` and `NVCC_THREADS` to get around compiler goes out of memory. I think this is because nvcc spawn threads for each SM architecture we are compiling to. * vaguely, "future proof". Currently, the "build system" is all in here https://github.com/vllm-project/vllm/blob/main/setup.py

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Call for Help: Proper Build System (CMake, Bazel, etc). help wanted Currently vLLM's compilation tool uses PyTorch's extension builders, which calls Ninja under the hood. This works okay but have the following issues: *...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e careful thinking. The requirements: * Must support multiple hardware architecture (NVIDIA, AMD, Intel, etc). * Must support incremental build, which also implies caching. * Must support parallelizable build. * Good to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: DIA and AMD GPUs. * Slow sequential builds. This is amplified by adding quantization kernels and LoRA kernels. * No caching and incremental builds. We would liked to ask for community's help on recommending a technology...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: or support (by generating compilation database). * Ideally it would not OOM like current setup. Currently due to the rigid structure, we have to carefully set `MAX_JOBS` and `NVCC_THREADS` to get around compiler goes ou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lm-project/vllm/blob/main/setup.py performance ci_build;hardware_porting;model_support;quantization cuda;kernel;quantization build_error;oom;slowdown env_dependency Currently vLLM's compilation tool uses PyTorch's exten...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
