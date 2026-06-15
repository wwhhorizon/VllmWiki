# vllm-project/vllm#8116: [Bug]: Loading GPTQ-quantized GPTBigCode fails in weight_loader_v2 of qptq_marlin

| 字段 | 值 |
| --- | --- |
| Issue | [#8116](https://github.com/vllm-project/vllm/issues/8116) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Loading GPTQ-quantized GPTBigCode fails in weight_loader_v2 of qptq_marlin

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading a gptbigcode model that has been quantized with gptq the loading fails and prints this stacktrace: ``` File "/home/develop/.local/lib/python3.11/site-packages/vllm/model_executor/models/gpt_bigcode.py", line 356, in load_weights weight_loader(param, loaded_weight) File "/home/develop/.local/lib/python3.11/site-packages/vllm/model_executor/layers/linear.py", line 779, in weight_loader_v2 self._load_fused_module_from_checkpoint(param, loaded_weight) File "/home/develop/.local/lib/python3.11/site-packages/vllm/model_executor/layers/linear.py", line 762, in _load_fused_module_from_checkpoint loaded_weight_shard = loaded_weight.narrow(param.output_dim, ``` The problem is that the marlin kernel is used ("The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel." appears in the log) and this kernel is using vLLMParameters since https://github.com/vllm-project/vllm/pull/7281. Forcing the use of `qptq` instead of `marlin` with `--quantization gptq` allows us to load and run the model correctly because the equivalent change in GPTQ hasn't been merged yet (https://github.com/vllm-project/vllm/pull/7976)....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vLLMParameters since https://github.com/vllm-project/vllm/pull/7281. Forcing the use of `qptq` instead of `marlin` with `--quantization gptq` allows us to load and run the model correctly because the equivalent change i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: em. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;quantization;speculative_decoding cuda;kernel;operator;quantization;triton build_error env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Loading GPTQ-quantized GPTBigCode fails in weight_loader_v2 of qptq_marlin bug ### Your current environment ### 🐛 Describe the bug When loading a gptbigcode model that has been quantized with gptq the loading fai...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: erged yet (https://github.com/vllm-project/vllm/pull/7976). But someone else in our team tested this PR and got similar results. The first parameter that fails to be loaded is `transformer.h.0.attn.c_attn.g_idx` I've tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
