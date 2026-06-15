# vllm-project/vllm#25155: [Installation]: run container by docker images failed, because of the oneDNN

| 字段 | 值 |
| --- | --- |
| Issue | [#25155](https://github.com/vllm-project/vllm/issues/25155) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: run container by docker images failed, because of the oneDNN

### Issue 正文摘录

### Your current environment ```text Env: MAC M2Pro ``` ### How you are installing vllm ```sh 1 step. install oneDNN 2 step. build vLLM from source codes 3 step. build docker image 4 step. run docker container based the docker image, i got the follow Error Logs: --- NotImplementedError: Could not run '_C::onednn_mm' with arguments from the 'CPU' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if using custom build). If you are a Facebook employee using PyTorch on mobile, please visit https://fburl.com/ptmfixes for possible resolutions. '_C::onednn_mm' is only available for these backends: [Meta, BackendSelect, Python, FuncTorchDynamicLayerBackMode, Functionalize, Named, Conjugate, Negative, ZeroTensor, ADInplaceOrView, AutogradOther, AutogradCPU, AutogradCUDA, AutogradXLA, AutogradMPS, AutogradXPU, AutogradHPU, AutogradLazy, AutogradMTIA, AutogradMAIA, AutogradMeta, Tracer, AutocastCPU, AutocastMTIA, AutocastMAIA, AutocastXPU, AutocastMPS, AutocastCUDA, FuncTorchBatched, BatchedNestedTensor, FuncTorchVmapMode, Batched, VmapMode, FuncTorchGradWrapper, PythonTLSSnapshot, FuncTorchDynamicLayerFrontM...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: run container by docker images failed, because of the oneDNN installation ### Your current environment ```text Env: MAC M2Pro ``` ### How you are installing vllm ```sh 1 step. install oneDNN 2 step. bui
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mentedError: Could not run '_C::onednn_mm' with arguments from the 'CPU' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if using cus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gative, ZeroTensor, ADInplaceOrView, AutogradOther, AutogradCPU, AutogradCUDA, AutogradXLA, AutogradMPS, AutogradXPU, AutogradHPU, AutogradLazy, AutogradMTIA, AutogradMAIA, AutogradMeta, Tracer, AutocastCPU, AutocastMTI...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
