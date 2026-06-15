# vllm-project/vllm#25751: [Bug]: tensorizer model loading with tensor parallelism increases memory requirements

| 字段 | 值 |
| --- | --- |
| Issue | [#25751](https://github.com/vllm-project/vllm/issues/25751) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tensorizer model loading with tensor parallelism increases memory requirements

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serializing / deserializing `meta-llama/Meta-Llama-3-70B-Instruct` with `tensorizer` and `tensor-parallel-size 4` it's expected that this requires with `bfloat16` roughly 140GB of VRAM. However, it requires about ~70GB instead of expected ~35GB GPU memory for each of the 4 GPUs. Can be reproduced with (vllm v10.0.2): ``` # serialize VLLM_LOGGING_LEVEL=DEBUG python vllm/examples/others/tensorize_vllm_model.py --enforce-eager --model meta-llama/Meta-Llama-3-70B-Instruct --dtype bfloat16 --tensor-parallel-size 4 --pipeline-parallel-size 1 serialize --serialized-directory ./meta_llama_3_70B_instruct_tensorized_pp1_tp4 # deserialize VLLM_LOGGING_LEVEL=DEBUG python vllm/examples/others/tensorize_vllm_model.py --enforce-eager --model meta-llama/Meta-Llama-3-70B-Instruct --dtype bfloat16 --tensor-parallel-size 4 --pipeline-parallel-size 1 --dtype bfloat16 deserialize --path-to-tensors ./meta_llama_3_70B_instruct_tensorized_pp1_tp4/vllm/meta-llama/Meta-Llama-3-70B-Instruct/900865aaee914de5a58e0b76b2d513c6/model-rank-%03d.tensors ``` where the deserialize then prints: ``` VLLM_LOGGING_LEVEL=DEBUG python vllm/examples/others/tensorize_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: tensorizer model loading with tensor parallelism increases memory requirements bug;unstale ### Your current environment ### 🐛 Describe the bug When serializing / deserializing `meta-llama/Meta-Llama-3-70B-Instruc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: hows that after model loading each GPU uses 41096MiB memory. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependenc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: zer` and `tensor-parallel-size 4` it's expected that this requires with `bfloat16` roughly 140GB of VRAM. However, it requires about ~70GB instead of expected ~35GB GPU memory for each of the 4 GPUs. Can be reproduced w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: tensorizer model loading with tensor parallelism increases memory requirements bug;unstale ### Your current environment ### 🐛 Describe the bug When serializing / deserializing `meta-llama/Meta-Llama-3-70B-Instruc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: odel loading with tensor parallelism increases memory requirements bug;unstale ### Your current environment ### 🐛 Describe the bug When serializing / deserializing `meta-llama/Meta-Llama-3-70B-Instruct` with `tensorizer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
