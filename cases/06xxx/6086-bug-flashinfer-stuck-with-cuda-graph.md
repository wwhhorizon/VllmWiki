# vllm-project/vllm#6086: [Bug]: Flashinfer stuck with CUDA Graph

| 字段 | 值 |
| --- | --- |
| Issue | [#6086](https://github.com/vllm-project/vllm/issues/6086) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Flashinfer stuck with CUDA Graph

### Issue 正文摘录

### Your current environment 2*3090 on Llama-2-13B @LiuXiaoxuanPKU Traceback as follows: ### 🐛 Describe the bug ```[416fa14255e5:25563:0:25918] Caught signal 11 (Segmentation fault: invalid permissions for mapped object at address 0x7f9c0d000000) [416fa14255e5:25629:0:25629] Caught signal 11 (Segmentation fault: invalid permissions for mapped object at address 0x7f9bb9000000) ==== backtrace (tid: 25918) ==== 0 0x0000000000042520 __sigaction() ???:0 1 0x00000000008dfeb8 flashinfer::PartitionPagedKVCacheComputeAuxiliaryInfo () ???:0 2 0x00000000009036b1 flashinfer::BatchDecodeHandler::BeginForwardDispatched () ???:0 3 0x0000000000892488 BatchDecodeWithPagedKVCachePyTorchWrapper::BeginForward(at::Tensor, at::Tensor, at::Tensor, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, float, at::Tensor, at::Tensor)::{lambda()#1}::operator()() const::{lambda()#1}::operator()() const::{lambda()#1}::operator()() const::{lambda()#2}::operator()() const::{lambda()#1}::operator()() const::{lambda()#1}::operator()() const::{lambda()#1}::operator()() const::{lambda()#1}::operator()() const::{lambda()#1}::operator()() tmpxft_00000134_00000000-6_batch_decode.compute_9...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Flashinfer stuck with CUDA Graph bug ### Your current environment 2*3090 on Llama-2-13B @LiuXiaoxuanPKU Traceback as follows: ### 🐛 Describe the bug ```[416fa14255e5:25563:0:25918] Caught signal 11 (Segmentation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Flashinfer stuck with CUDA Graph bug ### Your current environment 2*3090 on Llama-2-13B @LiuXiaoxuanPKU Traceback as follows: ### 🐛 Describe the bug ```[416fa14255e5:25563:0:25918] Caught signal 11 (Segmentation...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hinfer stuck with CUDA Graph bug ### Your current environment 2*3090 on Llama-2-13B @LiuXiaoxuanPKU Traceback as follows: ### 🐛 Describe the bug ```[416fa14255e5:25563:0:25918] Caught signal 11 (Segmentation fault: inva...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: cheComputeAuxiliaryInfo () ???:0 2 0x00000000009036b1 flashinfer::BatchDecodeHandler::BeginForwardDispatched () ???:0 3 0x0000000000892488 BatchDecodeWithPagedKVCachePyTorchWrapper::BeginForward(at::Tensor, at::Tensor,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ?:0 11 0x000000000016e7bb PyMethod_New() ???:0 12 0x000000000014e8a2 _PyEval_EvalFrameDefault() ???:0 13 0x000000000016e4e1 PyMethod_New() ???:0 14 0x000000000014a0d1 _PyEval_EvalFrameDefault() ???:0 15 0x00000000001607...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
