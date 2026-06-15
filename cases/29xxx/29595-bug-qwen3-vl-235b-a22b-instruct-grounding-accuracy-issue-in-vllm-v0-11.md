# vllm-project/vllm#29595: [Bug]: Qwen3-VL-235B-A22B-Instruct Grounding Accuracy Issue in vLLM (>= v0.11.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#29595](https://github.com/vllm-project/vllm/issues/29595) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 46; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;moe;operator;quantization;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-235B-A22B-Instruct Grounding Accuracy Issue in vLLM (>= v0.11.1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are observing degraded grounding accuracy when running Qwen3-VL-235B-A22B-Instruct model with vLLM versions 0.11.1 and 0.11.2. The model's grounding capabilities (spatial understanding and object localization) show significant precision degradation compared to previous vLLM versions. The model produces incorrect bounding box coordinates and poor spatial reasoning results. ### Reproduction Deploy Code ``` nohup python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 30000 --model Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 --served-model-name qwen3-vl-235b-a22b-instruct --max-model-len 64K --tensor-parallel-size 8 --pipeline-parallel-size 1 --trust-remote-code --max-num-seqs 16 --dtype bfloat16 --enable-log-requests --enable-auto-tool-choice --tool-call-parser hermes --async-scheduling --gpu-memory-utilization 0.95 --enable-expert-parallel --limit-mm-per-prompt.video 0 --mm_encoder_tp_mode="data" --mm_processor_cache_type="shm" & ``` ### Expected Behavior - Accurate bounding box coordinates ([x1, y1, x2, y2] format) - Precise spatial relationship descriptions - Consistent object localization ### Actual Behavior (vLLM 0.11....

## 现有链接修复摘要

#30525 [Release 2.10] Update to Torch 2.10 - final release

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 5B-A22B-Instruct Grounding Accuracy Issue in vLLM (>= v0.11.1) bug;torch.compile ### Your current environment ### 🐛 Describe the bug We are observing degraded grounding accuracy when running Qwen3-VL-235B-A22B-Instruct...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ver --host 0.0.0.0 --port 30000 --model Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 --served-model-name qwen3-vl-235b-a22b-instruct --max-model-len 64K --tensor-parallel-size 8 --pipeline-parallel-size 1 --trust-remote-code --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-VL-235B-A22B-Instruct Grounding Accuracy Issue in vLLM (>= v0.11.1) bug;torch.compile ### Your current environment ### 🐛 Describe the bug We are observing degraded grounding accuracy when running Qwen3-VL-2...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: [Bug]: Qwen3-VL-235B-A22B-Instruct Grounding Accuracy Issue in vLLM (>= v0.11.1) bug;torch.compile ### Your current environment ### 🐛 Describe the bug We are observing degraded grounding accuracy when running Qwen3-VL-2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ing box coordinates ([x1, y1, x2, y2] format) - Precise spatial relationship descriptions - Consistent object localization ### Actual Behavior (vLLM 0.11.1/0.11.2) - Incorrect or invalid bounding box coordinates - Poor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30525](https://github.com/vllm-project/vllm/pull/30525) | closes_keyword | 0.95 | [Release 2.10] Update to Torch 2.10 - final release | FIX #29595 FIX #33888 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
