# vllm-project/vllm#22619: [Usage]: how to tune a dense fp8_w8a8 model

| 字段 | 值 |
| --- | --- |
| Issue | [#22619](https://github.com/vllm-project/vllm/issues/22619) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to tune a dense fp8_w8a8 model

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm (EngineCore_0 pid=20659) WARNING 08-11 05:36:17 [fp8_utils.py:593] Using default W8A8 Block FP8 kernel config. Performance might be sub-optimal! Config file not found at /home/aabbccddwasd/vllm/vllm/model_executor/layers/quantization/utils/configs/N=5120,K=25600,device_name=NVIDIA_GeForce_RTX_4090,dtype=fp8_w8a8,block_shape=[128,128].json how to generate this file？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: how to tune a dense fp8_w8a8 model usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm (EngineCore_0 pid=20659) WARNING 08-11 05:36:17 [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ers/quantization/utils/configs/N=5120,K=25600,device_name=NVIDIA_GeForce_RTX_4090,dtype=fp8_w8a8,block_shape=[128,128].json how to generate this file？ ### Before submitting a new issue... - [x] Make sure you already sea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: how to tune a dense fp8_w8a8 model usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm (EngineCore_0 pid=20659) WARNING 08-11 05:36:17 [...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pid=20659) WARNING 08-11 05:36:17 [fp8_utils.py:593] Using default W8A8 Block FP8 kernel config. Performance might be sub-optimal! Config file not found at /home/aabbccddwasd/vllm/vllm/model_executor/layers/quantization...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to tune a dense fp8_w8a8 model usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm (EngineCore_0 pid=20659) WARNING 08-11 05:36:17 [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
