# vllm-project/vllm#7692: [RFC]: Add Ascend NPU as a new backend

| 字段 | 值 |
| --- | --- |
| Issue | [#7692](https://github.com/vllm-project/vllm/issues/7692) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add Ascend NPU as a new backend

### Issue 正文摘录

### Motivation. VLLM provides an easy-to-use backend access machanism and there are many backends have been integrated. As shown in https://github.com/vllm-project/vllm/issues/6368, https://github.com/vllm-project/vllm/issues/6728, https://github.com/vllm-project/vllm/issues/6066, many users want to use vllm on Ascend NPU. The **main purpose** of this RFC is to follow the existing backend access machanism and **make Ascend NPU available for VLLM**. ### Proposed Change. ![图片1](https://github.com/user-attachments/assets/ed02c5ce-64b4-4244-803b-0499d253e016) We introduce `Ascend Executor/Worker(s)` based on `GPU Executor/Worker(s)` as Ascend runtime management and worker on NPU. We also apply the `Ascend Backend` as the replacement of `attention layer`, the `Page Attention/Flash Attention` ops are implemented here. ![图片2](https://github.com/user-attachments/assets/58d2e85f-6c29-4846-8162-7fa1dd2afcf5) Because torch_npu already natively supports torch since 2.1.0, we should try to keep it consistent with the GPU code and make the least code changes in our implements. ### Feedback Period. A month ### CC List. @mgoin @WoosukKwon ### Any Other Things. ### Background **Ascend NPU** is a r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ** is a range of AI processors using Neural Processing Unit. It will efficiently handle matrix-matrix multiplication, dot-product and scalars. There are many projects have supported Ascend NPU, such as [onnxruntime](htt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC]: Add Ascend NPU as a new backend RFC ### Motivation. VLLM provides an easy-to-use backend access machanism and there are many backends have been integrated. As shown in https://github.com/vllm-project/vllm/issues/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: html), [deepspeed](https://github.com/microsoft/DeepSpeed/issues/4567), [llama.cpp](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md#cann) **[MindIE](https://www.hiascend.com/en/software/mindie)** is the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: RFC ### Motivation. VLLM provides an easy-to-use backend access machanism and there are many backends have been integrated. As shown in https://github.com/vllm-project/vllm/issues/6368, https://github.com/vllm-project/v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
