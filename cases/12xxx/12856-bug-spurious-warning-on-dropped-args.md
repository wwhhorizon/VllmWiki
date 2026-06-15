# vllm-project/vllm#12856: [Bug]: Spurious warning on dropped args

| 字段 | 值 |
| --- | --- |
| Issue | [#12856](https://github.com/vllm-project/vllm/issues/12856) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Spurious warning on dropped args

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using `Qwen2-VL` to generate captions for short video clips, I'm passing the following to vllm: ```python llm = LLM( model=weight_file, limit_mm_per_prompt={"image": 10, "video": 10}, quantization="fp8", max_seq_len_to_capture=16384, mm_processor_kwargs={ "do_resize": False, "do_rescale": False, "do_normalize": False, }, ) ``` The `mm_processor_kwargs` args seems to have an effect, but I get warnings like these: ```console WARNING 02-06 22:57:39 utils.py:1474] The following intended overrides are not keyword-only args and and will be dropped: {'do_resize', 'do_rescale', 'do_normalize'} ``` They seem to be spurious since the args are being applied. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: del=weight_file, limit_mm_per_prompt={"image": 10, "video": 10}, quantization="fp8", max_seq_len_to_capture=16384, mm_processor_kwargs={ "do_resize": False, "do_rescale": False, "do_normalize": False, }, ) ``` The `mm_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;quan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: bug ### Your current environment ### 🐛 Describe the bug I'm using `Qwen2-VL` to generate captions for short video clips, I'm passing the following to vllm: ```python llm = LLM( model=weight_file, limit_mm_per_prompt={"i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;fp8;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
