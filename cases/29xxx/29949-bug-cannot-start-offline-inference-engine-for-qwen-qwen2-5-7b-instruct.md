# vllm-project/vllm#29949: [Bug]: Cannot start offline inference engine for Qwen/Qwen2.5-7B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#29949](https://github.com/vllm-project/vllm/issues/29949) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot start offline inference engine for Qwen/Qwen2.5-7B-Instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM(model="Qwen/Qwen2.5-7B-Instruct") ``` However, there is no problem when using online server ```bash vllm serve Qwen/Qwen2.5-7B-Instruct ``` > [!NOTE] > The compilation config (model_len, seq_len) is different, but this should not be the problem. Because it still raises error when I copy the compilation config to the offline engine ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM(model="Qwen/Qwen2.5-7B-Instruct") ``` However, there is no problem when using online server ```bash vllm serve Qwen/Qwen2.5-7B-Ins...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Cannot start offline inference engine for Qwen/Qwen2.5-7B-Instruct bug ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM(model="Qwen/Qwen2.5-7B-Instruct") ``` However, t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ted_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;quantization;sampling;triton build_error;crash;nan_inf dty...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ine ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: orrectness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;quantizatio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
