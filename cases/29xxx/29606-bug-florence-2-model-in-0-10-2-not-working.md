# vllm-project/vllm#29606: [Bug]: Florence 2 model in 0.10.2 not working

| 字段 | 值 |
| --- | --- |
| Issue | [#29606](https://github.com/vllm-project/vllm/issues/29606) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Florence 2 model in 0.10.2 not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Every time i try to load the model in the 0.10.2 vllm version i get the same error. In the 0.8.0 there was another error related to the llm head weights not been initialized. ```python LLM( model="microsoft/Florence-2-large", tokenizer="facebook/bart-large", max_num_seqs=8, trust_remote_code=True, limit_mm_per_prompt={"image": 1}, dtype="half", ) ``` The full error is: ``` [rank0]: pydantic_core._pydantic_core.ValidationError: 1 validation error for VllmConfig [rank0]: Value error, No model architectures are specified [type=value_error, input_value=ArgsKwargs((), {'model_co...'instance_id': '9e326'}), input_type=ArgsKwargs] [rank0]: For further information visit https://errors.pydantic.dev/2.12/v/value_error [rank0]:[W1127 12:57:15.585304442 ProcessGroupNCCL.cpp:1538] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator()) `` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Describe the bug Every time i try to load the model in the 0.10.2 vllm version i get the same error. In the 0.8.0 there was another error related to the llm head weights not been initialized. ```python LLM( model="micro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Florence 2 model in 0.10.2 not working bug ### Your current environment ### 🐛 Describe the bug Every time i try to load the model in the 0.10.2 vllm version i get the same error. In the 0.8.0 there was another er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rror: 1 validation error for VllmConfig [rank0]: Value error, No model architectures are specified [type=value_error, input_value=ArgsKwargs((), {'model_co...'instance_id': '9e326'}), input_type=ArgsKwargs] [rank0]: For...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ote_code=True, limit_mm_per_prompt={"image": 1}, dtype="half", ) ``` The full error is: ``` [rank0]: pydantic_core._pydantic_core.ValidationError: 1 validation error for VllmConfig [rank0]: Value error, No model archite...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
