# vllm-project/vllm#19727: [Feature]: AWQ DeepSeek support on MI300X

| 字段 | 值 |
| --- | --- |
| Issue | [#19727](https://github.com/vllm-project/vllm/issues/19727) |
| 状态 | closed |
| 标签 | feature request;rocm;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: AWQ DeepSeek support on MI300X

### Issue 正文摘录

I'm testing [`RedHatAI/DeepSeek-R1-0528-quantized.w4a16`](https://huggingface.co/RedHatAI/DeepSeek-R1-0528-quantized.w4a16) on 4xMI300X with this command: ```sh vllm serve RedHatAI/DeepSeek-R1-0528-quantized.w4a16 --host 0.0.0.0 --port 3000 --max-model-len 8192 --max-seq-len-to-capture 8192 --enable-chunked-prefill --enable-prefix-caching --trust-remote-code --disable-log-requests --tensor-parallel-size 4 --gpu-memory-utilization 0.95 --served-model-name deepseek-chat ``` And I get: ``` '_OpNamespace' '_C' object has no attribute 'gptq_marlin_repack' ``` I've tried `VLLM_USE_TRITON_AWQ=1` (seems like it's activated automatically for rocm devices anyway), but it looks like there is no `gptq_marlin_repack` in `awq_triton.py` so that didn't help: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/awq_triton.py #### Related: * https://github.com/vllm-project/vllm/issues/11249

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: AWQ DeepSeek support on MI300X feature request;rocm;stale I'm testing [`RedHatAI/DeepSeek-R1-0528-quantized.w4a16`](https://huggingface.co/RedHatAI/DeepSeek-R1-0528-quantized.w4a16) on 4xMI300X with this comm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: AWQ DeepSeek support on MI300X feature request;rocm;stale I'm testing [`RedHatAI/DeepSeek-R1-0528-quantized.w4a16`](https://huggingface.co/RedHatAI/DeepSeek-R1-0528-quantized.w4a16) on 4xMI300X with this comm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ;stale I'm testing [`RedHatAI/DeepSeek-R1-0528-quantized.w4a16`](https://huggingface.co/RedHatAI/DeepSeek-R1-0528-quantized.w4a16) on 4xMI300X with this command: ```sh vllm serve RedHatAI/DeepSeek-R1-0528-quantized.w4a1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ' object has no attribute 'gptq_marlin_repack' ``` I've tried `VLLM_USE_TRITON_AWQ=1` (seems like it's activated automatically for rocm devices anyway), but it looks like there is no `gptq_marlin_repack` in `awq_triton....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: I300X feature request;rocm;stale I'm testing [`RedHatAI/DeepSeek-R1-0528-quantized.w4a16`](https://huggingface.co/RedHatAI/DeepSeek-R1-0528-quantized.w4a16) on 4xMI300X with this command: ```sh vllm serve RedHatAI/DeepS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
