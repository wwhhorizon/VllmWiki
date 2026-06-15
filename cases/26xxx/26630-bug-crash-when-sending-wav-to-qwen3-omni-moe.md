# vllm-project/vllm#26630: [Bug]: crash when sending wav to qwen3_omni_moe

| 字段 | 值 |
| --- | --- |
| Issue | [#26630](https://github.com/vllm-project/vllm/issues/26630) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: crash when sending wav to qwen3_omni_moe

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve /jr-sec-ai/open-models/Qwen/Qwen3-Omni-30B-A3B-Instruct --served-model-name Qwen3-Omni-30B-A3B-Instruct --dtype bfloat16 --max-model-len 65536 --allowed-local-media-path / -tp 8 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser hermes` ``` POST /v1/chat/completions { "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": [ { "type": "audio_url", "audio_url": { "url": "https://freedata.oss-cn-beijing.aliyuncs.com/freedata/magicdatatech/MDT-ASR-E026/WAV/20200321_2P_mac_oppor15_gongsi_03702.wav" } }, {"type": "text", "text": "提取每个人说的话。"} ]} ] } ``` It show the errors and exit ``` RuntimeError: split_with_sizes expects split_sizes to sum exactly to 3000 (input tensor's size at dimension 0), but got split_sizes=[100, 100, 100, 100... ``` Here is the full log: [error_log.txt](https://github.com/user-attachments/files/22863431/error_log.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -Omni-30B-A3B-Instruct --served-model-name Qwen3-Omni-30B-A3B-Instruct --dtype bfloat16 --max-model-len 65536 --allowed-local-media-path / -tp 8 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser herm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: crash when sending wav to qwen3_omni_moe bug ### Your current environment ### 🐛 Describe the bug `vllm serve /jr-sec-ai/open-models/Qwen/Qwen3-Omni-30B-A3B-Instruct --served-model-name Qwen3-Omni-30B-A3B-Instruct...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: crash when sending wav to qwen3_omni_moe bug ### Your current environment ### 🐛 Describe the bug `vllm serve /jr-sec-ai/open-models/Qwen/Qwen3-Omni-30B-A3B-Instruct --served-model-name Qwen3-Omni-30B-A3B-Instruct...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
