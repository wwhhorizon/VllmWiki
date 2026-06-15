# vllm-project/vllm#37103: [Bug]: UserWarning: Input tensor shape suggests potential format mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#37103](https://github.com/vllm-project/vllm/issues/37103) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: UserWarning: Input tensor shape suggests potential format mismatch

### Issue 正文摘录

### Your current environment System: Model and command line: ### 🐛 Describe the bug From time to time, I can see this message in the log: ```text (EngineCore pid=365) /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fla/ops/utils.py:113: UserWarning: Input tensor shape suggests potential format mismatch: seq_len (23) < num_heads (64). This may indicate the inputs were passed in head-first format [B, H, T, ...] when head_first=False was specified. Please verify your input tensor format matches the expected shape [B, T, H, ...]. ``` And from time to time, I have "API Error" message on application side. I don't know if it is related. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: passed in head-first format [B, H, T, ...] when head_first=False was specified. Please verify your input tensor format matches the expected shape [B, T, H, ...]. ``` And from time to time, I have "API Error" message on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: UserWarning: Input tensor shape suggests potential format mismatch bug ### Your current environment System: Model and command line: ### 🐛 Describe the bug From time to time, I can see this message in the log: ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ectness ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;quantization;sampling;triton build_error;mismatch;nan_inf;slowdow...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: inputs were passed in head-first format [B, H, T, ...] when head_first=False was specified. Please verify your input tensor format matches the expected shape [B, T, H, ...]. ``` And from time to time, I have "API Error"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: UserWarning: Input tensor shape suggests potential format mismatch bug ### Your current environment System: Model and command line: ### 🐛 Describe the bug From time to time, I can see this message in the log: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
