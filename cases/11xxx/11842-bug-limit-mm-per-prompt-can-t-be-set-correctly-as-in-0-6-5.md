# vllm-project/vllm#11842: [Bug]: “limit-mm-per-prompt” can't be set correctly as in 0.6.5

| 字段 | 值 |
| --- | --- |
| Issue | [#11842](https://github.com/vllm-project/vllm/issues/11842) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | cuda;gemm;kernel;operator |
| 症状 | build_error;mismatch;oom |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: “limit-mm-per-prompt” can't be set correctly as in 0.6.5

### Issue 正文摘录

### Your current environment ```text vllm==0.6.6.post1 cuda==12.4 ubuntu==22.04 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I run the following server command in v0.6.6.post1: ```bash python -m vllm.entrypoints.openai.api_server \ --model "./Qwen2-VL-7B-Instruct" \ --served-model-name "Qwen2-VL-7B-Instruct" \ --device cuda \ --limit-mm-per-prompt image=8 ``` it warns that: ```text WARNING 01-08 18:59:14 model_runner.py:1279] Computed max_num_seqs (min(256, 32768 // 180224)) to be less than 1. Setting it to the minimum value of 1. Token indices sequence length is longer than the specified maximum sequence length for this model (163840 > 32768). Running this sequence through the model will result in indexing errors WARNING 01-08 18:59:32 processing.py:878] The context length (32768) of the model is too short to hold the multi-modal embeddings in the worst case (163840 tokens in total, out of which {'image': 163840} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`. `...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: minimum value of 1. Token indices sequence length is longer than the specified maximum sequence length for this model (163840 > 32768). Running this sequence through the model will result in indexing errors WARNING 01-0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: environment ```text vllm==0.6.6.post1 cuda==12.4 ubuntu==22.04 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I run the following server command in v0.6.6.post1: ```bash python -m vllm.entrypoints.o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: as in 0.6.5 bug ### Your current environment ```text vllm==0.6.6.post1 cuda==12.4 ubuntu==22.04 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I run the following server command in v0.6.6.post1: ```...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: `text ...... ../aten/src/ATen/native/cuda/IndexKernel.cu:93: operator(): block: [8274,0,0], thread: [123,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of bounds"` failed. ../aten/src/ATen/native/c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: d_api;model_support;multimodal_vlm cuda;gemm;kernel;operator build_error;mismatch;oom env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
