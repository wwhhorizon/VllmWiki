# vllm-project/vllm#10819: [Bug]: The model output is abnormal when I use 2:4 sparsity

| 字段 | 值 |
| --- | --- |
| Issue | [#10819](https://github.com/vllm-project/vllm/issues/10819) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The model output is abnormal when I use 2:4 sparsity

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm compressing a qwen2.5_7b model using llmcompressor. But I encountered some issues. First, I failed to load the `stage_sparsity` model. Additionally, when I use the `stage_quantization` model for inference with vllm, the output is abnormal. You can reproduce my issue by following these steps. - Run [`llm-compressor/examples/quantization_2of4_sparse_w4a16/llama7b_sparse_w4a16.py`](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_2of4_sparse_w4a16/llama7b_sparse_w4a16.py), to get the model with the following configuration: - Setting `model_stub = Qwen/Qwen2.5-7B-Instruct`. - Using the recipe below: ``` sparsity_stage: run_type: oneshot sparsity_modifiers: SparseGPTModifier: sparsity: 0.5 mask_structure: "2:4" sequential_update: false quantization_stage: run_type: oneshot quantization_modifiers: GPTQModifier: ignore: ["lm_head"] config_groups: group_0: weights: num_bits: 4 type: "int" symmetric: true strategy: "channel" targets: ["Linear"] ``` - The output of `stage_quantization` model is abnormal: (please set MODEL_PATH to the stage_quantization model yourself) ``...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: on: - Setting `model_stub = Qwen/Qwen2.5-7B-Instruct`. - Using the recipe below: ``` sparsity_stage: run_type: oneshot sparsity_modifiers: SparseGPTModifier: sparsity: 0.5 mask_structure: "2:4" sequential_update: false...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: The model output is abnormal when I use 2:4 sparsity bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm compressing a qwen2.5_7b model using llmcompressor. But I encou...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: to load the `stage_sparsity` model. Additionally, when I use the `stage_quantization` model for inference with vllm, the output is abnormal. You can reproduce my issue by following these steps. - Run [`llm-compressor/ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bb) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gemm_linear;hardware_porting;model_support;sampling_logits cuda;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
