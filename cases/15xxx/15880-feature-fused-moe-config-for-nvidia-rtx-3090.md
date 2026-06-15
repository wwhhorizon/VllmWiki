# vllm-project/vllm#15880: [Feature]: Fused MoE config for Nvidia RTX 3090

| 字段 | 值 |
| --- | --- |
| Issue | [#15880](https://github.com/vllm-project/vllm/issues/15880) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | moe;quantization |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Fused MoE config for Nvidia RTX 3090

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi there, I'm running a setup for 16x3090 for DeepSeek-R1 AWQ. This is working very well. I've noticed that it's missing the Fused Moe config: ``` (VllmWorker rank=15 pid=863) WARNING 03-30 07:46:52 [fused_moe.py:885] Using default MoE config. Performance might be sub-optimal! Config file not found at /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/configs/E=256,N=128,device_name=NVIDIA_GeForce_RTX_3090,dtype=int4_w4a16.json ``` Could I have direction to build this config myself, or where to start? It would be massively appreciated. I looked at the script, but i saw the dtype could not be set to w4a16. Thank you! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: layers/fused_moe/configs/E=256,N=128,device_name=NVIDIA_GeForce_RTX_3090,dtype=int4_w4a16.json ``` Could I have direction to build this config myself, or where to start? It would be massively appreciated. I looked at th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: IA_GeForce_RTX_3090,dtype=int4_w4a16.json ``` Could I have direction to build this config myself, or where to start? It would be massively appreciated. I looked at the script, but i saw the dtype could not be set to w4a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Fused MoE config for Nvidia RTX 3090 feature request;stale ### 🚀 The feature, motivation and pitch Hi there, I'm running a setup for 16x3090 for DeepSeek-R1 AWQ. This is working very well. I've noticed that i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Fused MoE config for Nvidia RTX 3090 feature request;stale ### 🚀 The feature, motivation and pitch Hi there, I'm running a setup for 16x3090 for DeepSeek-R1 AWQ. This is working very well. I've noticed that i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Fused MoE config for Nvidia RTX 3090 feature request;stale ### 🚀 The feature, motivation and pitch Hi there, I'm running a setup for 16x3090 for DeepSeek-R1 AWQ. This is working very well. I've noticed that i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
