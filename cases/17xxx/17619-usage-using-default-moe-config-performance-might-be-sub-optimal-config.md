# vllm-project/vllm#17619: [Usage]: Using default MoE config. Performance might be sub-optimal! Config file not found

| 字段 | 值 |
| --- | --- |
| Issue | [#17619](https://github.com/vllm-project/vllm/issues/17619) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Using default MoE config. Performance might be sub-optimal! Config file not found

### Issue 正文摘录

### Your current environment While deploying Qwen/Qwen3-235B-A22B-FP8 with v0.8.5.post1 (VllmWorker rank=1 pid=236) WARNING 05-03 17:42:23 [fused_moe.py:668] Using default MoE config. Performance might be sub-optimal! Config file not found at /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/configs/E=16,N=1536,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json Getting warning about missing configuration file not, not sure what could be the issue ### How would you like to use vllm While deploying Qwen/Qwen3-235B-A22B-FP8 with v0.8.5.post1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Using default MoE config. Performance might be sub-optimal! Config file not found usage;stale ### Your current environment While deploying Qwen/Qwen3-235B-A22B-FP8 with v0.8.5.post1 (VllmWorker rank=1 pid=236)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: stale ### Your current environment While deploying Qwen/Qwen3-235B-A22B-FP8 with v0.8.5.post1 (VllmWorker rank=1 pid=236) WARNING 05-03 17:42:23 [fused_moe.py:668] Using default MoE config. Performance might be sub-opti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m/model_executor/layers/fused_moe/configs/E=16,N=1536,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json Getting warning about missing configuration file not, not sure what could be the issue ##...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: moe/configs/E=16,N=1536,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json Getting warning about missing configuration file not, not sure what could be the issue ### How would you like to use vl...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: Using default MoE config. Performance might be sub-optimal! Config file not found usage;stale ### Your current environment While deploying Qwen/Qwen3-235B-A22B-FP8 with v0.8.5.post1 (VllmWorker rank=1 pid=236)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
