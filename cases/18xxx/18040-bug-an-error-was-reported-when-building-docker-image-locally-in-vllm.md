# vllm-project/vllm#18040: [Bug]: An error was reported when building docker image locally in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#18040](https://github.com/vllm-project/vllm/issues/18040) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: An error was reported when building docker image locally in vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug https://github.com/vllm-project/vllm/issues/17608 Since there is no release for this issue yet. I pulled the latest code locally and wanted to build a latest docker image. Then the following errors occurred. ```text9237.3 /workspace/csrc/quantization/gptq_marlin/kernel.h(36): warning #20281-D: in whole program compilation mode ("-rdc=false"), a __global__ function template instantiation or specialization ("marlin::Marlin ") will be required to have a definition in the current translation unit, when "-static-global-template-stub" will be set to "true" by default in the future. To resolve this issue, either use "-rdc=true", or explicitly set "-static-global-template-stub=false" (but see nvcc documentation about downsides of turning it off) 9237.3 9237.3 /workspace/csrc/quantization/gptq_marlin/kernel.h(36): warning #20281-D: in whole program compilation mode ("-rdc=false"), a __global__ function template instantiation or specialization ("marlin::Marlin ") will be required to have a definition in the current translation unit, when "-static-global-template-stub" will be set to "true" by default in the future. To re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: An error was reported when building docker image locally in vLLM bug;stale ### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug https://github.com/vllm-project/vllm/issues/17608 Since there is n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: mage. Then the following errors occurred. ```text9237.3 /workspace/csrc/quantization/gptq_marlin/kernel.h(36): warning #20281-D: in whole program compilation mode ("-rdc=false"), a __global__ function template instantia...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tion about downsides of turning it off) 9237.3 9311.4 [49/334] Building CUDA object CMakeFiles/_C.dir/csrc/quantization/gptq_marlin/gptq_marlin_repack.cu.o 9382.6 [50/334] Building CUDA object CMakeFiles/_C.dir/csrc/qua...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: itive data (ARG "SCCACHE_S3_NO_CREDENTIALS") (line 118) - LegacyKeyValueFormat: "ENV key=value" should be used instead of legacy "ENV key value" format (line 338) Dockerfile:139 -------------------- 138 | ENV CCACHE_DIR...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 9511.3 [53/334] Building CUDA object CMakeFiles/_C.dir/csrc/quantization/cutlass_w8a8/scaled_mm_c3x_sm90.cu.o 9624.3 [54/334] Building CUDA object CMakeFiles/_C.dir/csrc/quantization/cutlass_w8a8/c3x/scaled_mm_sm90_fp8....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
