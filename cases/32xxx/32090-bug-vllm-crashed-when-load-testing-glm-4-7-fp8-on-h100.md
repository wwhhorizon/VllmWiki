# vllm-project/vllm#32090: [Bug]: vLLM crashed when load testing GLM 4.7 FP8 on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#32090](https://github.com/vllm-project/vllm/issues/32090) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashed when load testing GLM 4.7 FP8 on H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran `zai-org/GLM-4.7-FP8` on 8xH100 with this args: ``` - "--gpu-memory-utilization=0.9" - "--tensor-parallel-size=8" - "--max-num-batched-tokens=65536" - "--max-num-seqs=512" - "--enable-auto-tool-choice" - "--tool-call-parser=glm47" - "--reasoning-parser=glm45" - "--speculative-config.method=mtp" - "--speculative-config.num_speculative_tokens=1" - "--served-model-name=glm-4.7-fp8" - "--enable-expert-parallel" ``` The inference starts without any issue, however when doing the benchmark: ``` vllm bench serve --model glm-4.7-fp8 --tokenizer zai-org/GLM-4.7-FP8 --dataset-name random --host --port 80 --random-input-len 2048 --random-output-len 128 --request-rate inf --num-prompts 128 ``` the server crashed with this error: ``` (APIServer pid=1) ERROR 01-10 07:09:06 [serving_completion.py:512] ^^^^^^^^^^^^^ (APIServer pid=1) ERROR 01-10 07:09:06 [serving_completion.py:512] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/output_processor.py", line 73, in get (APIServer pid=1) ERROR 01-10 07:09:06 [serving_completion.py:512] raise output (APIServer pid=1) ERROR 01-10 07:09:06 [serving_completion.py:512] File "/usr/local/...

## 现有链接修复摘要

#32512 Fail-fast guard: block MTP on GLM-4.7-FP8 to avoid CUDA illegal access

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vLLM crashed when load testing GLM 4.7 FP8 on H100 bug;stale ### Your current environment ### 🐛 Describe the bug I ran `zai-org/GLM-4.7-FP8` on 8xH100 with this args: ``` - "--gpu-memory-utilization=0.9" - "--ten...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: vLLM crashed when load testing GLM 4.7 FP8 on H100 bug;stale ### Your current environment ### 🐛 Describe the bug I ran `zai-org/GLM-4.7-FP8` on 8xH100 with this args: ``` - "--gpu-memory-utilization=0.9" - "--ten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vLLM crashed when load testing GLM 4.7 FP8 on H100 bug;stale ### Your current environment ### 🐛 Describe the bug I ran `zai-org/GLM-4.7-FP8` on 8xH100 with this args: ``` - "--gpu-memory-utilization=0.9" - "--ten...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ool-call-parser=glm47" - "--reasoning-parser=glm45" - "--speculative-config.method=mtp" - "--speculative-config.num_speculative_tokens=1" - "--served-model-name=glm-4.7-fp8" - "--enable-expert-parallel" ``` The inferenc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32512](https://github.com/vllm-project/vllm/pull/32512) | mentioned | 0.6 | Fail-fast guard: block MTP on GLM-4.7-FP8 to avoid CUDA illegal access | on GLM-4.7-FP8 to avoid CUDA illegal access This is a mitigation for vllm-project/vllm#32090. Problem: recent nightlies reported CUDA illegal memory access when running zai-org/GL… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
