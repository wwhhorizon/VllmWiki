# vllm-project/vllm#13075: Could not run '_C::rms_norm' with arguments from the 'CUDA' backend.

| 字段 | 值 |
| --- | --- |
| Issue | [#13075](https://github.com/vllm-project/vllm/issues/13075) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;hardware_porting;model_support |
| 子分类 | install |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Could not run '_C::rms_norm' with arguments from the 'CUDA' backend.

### Issue 正文摘录

NotImplementedError: Error in model execution (input dumped to /tmp/err_execute_model_input_20250211-140137.pkl): Could not run '_C::rms_norm' with arguments from the 'CUDA' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if using custom build). If you are a Facebook employee using PyTorch on mobile, please visit https://fburl.com/ptmfixes for possible resolutions. '_C::rms_norm' is only available for these backends: [HIP, Meta, BackendSelect, Python, FuncTorchDynamicLayerBackMode, Functionalize, Named, Conjugate, Negative, ZeroTensor, ADInplaceOrView, AutogradOther, AutogradCPU, AutogradCUDA, AutogradXLA, AutogradMPS, AutogradXPU, AutogradHPU, AutogradLazy, AutogradMeta, Tracer, AutocastCPU, AutocastXPU, AutocastCUDA, FuncTorchBatched, BatchedNestedTensor, FuncTorchVmapMode, Batched, VmapMode, FuncTorchGradWrapper, PythonTLSSnapshot, FuncTorchDynamicLayerFrontMode, PreDispatch, PythonDispatcher]. ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Could not run '_C::rms_norm' with arguments from the 'CUDA' backend. installation NotImplementedError: Error in model execution (input dumped to /tmp/err_execute_model_input_20250211-140137.pkl): Could not run '_C::rms_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Could not run '_C::rms_norm' with arguments from the 'CUDA' backend. installation NotImplementedError: Error in model execution (input dumped to /tmp/err_execute_model_input_20250211-140137.pkl): Could not run '_C::rms_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Could not run '_C::rms_norm' with arguments from the 'CUDA' backend. installation NotImplementedError: Error in model execution (input dumped to /tmp/err_execute_model_input_20250211-140137.pkl): Could not run '_C::rms_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ents from the 'CUDA' backend. installation NotImplementedError: Error in model execution (input dumped to /tmp/err_execute_model_input_20250211-140137.pkl): Could not run '_C::rms_norm' with arguments from the 'CUDA' ba...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development activation_norm;ci_build;hardware_porting;model_support cuda;operator bui...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
