# vllm-project/vllm#26902: [Bug]: Qwen3-VL-8B-Thinking under vLLM shows inaccurate temporal localization compared to Transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#26902](https://github.com/vllm-project/vllm/issues/26902) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-8B-Thinking under vLLM shows inaccurate temporal localization compared to Transformers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Summary I’m using Qwen3-VL-8B-Thinking for a video moment retrieval task, and I noticed a significant difference in behavior between vLLM and Transformers inference: 1. When running the same prompt and video(link: https://pan.quark.cn/s/58d7264426b0, ~6mins) input through both frameworks, the time range grounding from the vLLM inference are noticeably less accurate, while Transformers produces more precise temporal localization results. 2. Moreover, when using vLLM, the model is likely output repetitive or meaningless text loops. The prompt and model output are shown below. (⚠️ Careful — long text below.) The correct time range should be - **[17s, 36s]** for elderly people doing exercises - **[205s, 260s]** for people playing basketball** Could you please help check whether this is a known issue or provide suggestions on possible causes or fixes? Happy to share more logs or debugging info if needed — thanks a lot for your help! ### Reproduce Below are the vLLM setting and inference code of vLLM and transformers. ```bash vllm serve Qwen/Qwen3-VL-8B-Thinking \ --tensor-parallel-size 8 \ --allowed-local-media-path / \ --mm-encod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: M and Transformers inference: 1. When running the same prompt and video(link: https://pan.quark.cn/s/58d7264426b0, ~6mins) input through both frameworks, the time range grounding from the vLLM inference are noticeably l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL-8B-Thinking under vLLM shows inaccurate temporal localization compared to Transformers bug ### Your current environment ### 🐛 Describe the bug ### Summary I’m using Qwen3-VL-8B-Thinking for a video momen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: f8) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: debugging info if needed — thanks a lot for your help! ### Reproduce Below are the vLLM setting and inference code of vLLM and transformers. ```bash vllm serve Qwen/Qwen3-VL-8B-Thinking \ --tensor-parallel-size 8 \ --al...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding cuda;gemm;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
