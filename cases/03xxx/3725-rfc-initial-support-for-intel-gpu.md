# vllm-project/vllm#3725: [RFC] Initial support for Intel GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#3725](https://github.com/vllm-project/vllm/issues/3725) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;operator;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] Initial support for Intel GPU

### Issue 正文摘录

### Anything you want to discuss about vllm. # Progress - [ ] Cmake and build System for Intel XPU/SYCL - [ ] vLLM custom op implementation in SYCL source code - [ ] Integrate Intel XPU backend for basic model inference. - [ ] Support tensor parallelism with Ray for XPU backend - [ ] Integrate with IPEX optimized kernels(eg, page attention) for better performance - [ ] Quantization support # Target Intel GPU device and models For Intel GPU device(in pytorch context, it's named `xpu`), we are trying to make vllm support Intel Xe architecture Graphic cards, including data center MAX GPUs(such as PVC 1550, PVC 1100), and client GPUs(such as Arc A770) natively. For models, we will make sure vLLM + xpu works well with all existing vLLM supported models. # Design ## Python API Since Intel GPU have similar API (via IPEX) and behavior compare with CUDA device, we just introduce 2 new classes 1. XPUExecutor(extends ExecutorBase), have similar behavior with GpuExecutor, will dispatch to generate this executor class based on device type in LLMEngine and AsyncLLMEngine 2. XPUWorker( extends Worker Class) is used to initial the environment, most of code is shared from parent class. ![xpu_vllm]...

## 现有链接修复摘要

#3814 [Hardware][Intel GPU]Add Initial Intel GPU(XPU) inference backend

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: FC;stale ### Anything you want to discuss about vllm. # Progress - [ ] Cmake and build System for Intel XPU/SYCL - [ ] vLLM custom op implementation in SYCL source code - [ ] Integrate Intel XPU backend for basic model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tel XPU backend for basic model inference. - [ ] Support tensor parallelism with Ray for XPU backend - [ ] Integrate with IPEX optimized kernels(eg, page attention) for better performance - [ ] Quantization support # Ta...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: custom op implementation in SYCL source code - [ ] Integrate Intel XPU backend for basic model inference. - [ ] Support tensor parallelism with Ray for XPU backend - [ ] Integrate with IPEX optimized kernels(eg, page at...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: IPEX optimized kernels(eg, page attention) for better performance - [ ] Quantization support # Target Intel GPU device and models For Intel GPU device(in pytorch context, it's named `xpu`), we are trying to make vllm su...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ntation in SYCL source code - [ ] Integrate Intel XPU backend for basic model inference. - [ ] Support tensor parallelism with Ray for XPU backend - [ ] Integrate with IPEX optimized kernels(eg, page attention) for bett...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#3814](https://github.com/vllm-project/vllm/pull/3814) | mentioned | 0.6 | [Hardware][Intel GPU]Add Initial Intel GPU(XPU) inference backend | nitial Intel GPU(XPU) inference backend **This PR is first PR for RFC #3725** _Intel is contributing both Intel CPU and Intel GPU support for vLLM. Initial PR #3634 for CPU alread… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
