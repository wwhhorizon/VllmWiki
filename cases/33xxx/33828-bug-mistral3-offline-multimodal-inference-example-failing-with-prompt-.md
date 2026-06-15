# vllm-project/vllm#33828: [Bug]: mistral3 offline multimodal inference example failing with prompt placeholder error

| 字段 | 值 |
| --- | --- |
| Issue | [#33828](https://github.com/vllm-project/vllm/issues/33828) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: mistral3 offline multimodal inference example failing with prompt placeholder error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The offline example for multimodal inference with `mistralai/Mistral-Small-3.1-24B-Instruct-2503` and mistral_common 1.9.0 fails during pre-processing with: ```RuntimeError: Expected there to be 1 prompt placeholders corresponding to 1 image items, but instead found 0 prompt placeholders! Make sure the implementation of `_call_hf_processor` and `_get_mm_fields_config` are consistent with each other.``` `python3 examples/offline_inference/vision_language.py -m mistral3` ``` (EngineCore_DP0 pid=1126) INFO 02-04 21:08:56 [core.py:272] init engine (profile, create kv cache, warmup model) took 17.31 seconds INFO 02-04 21:08:56 [llm.py:349] Supported tasks: ['generate'] Adding requests: 0%| | 0/4 [00:00 main(args) File "/vllm-workspace/examples/offline_inference/vision_language.py", line 2514, in main outputs = llm.generate( ^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/llm.py", line 426, in generate self._validate_and_add_requests( File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/llm.py", line 1706, in _validate_and_add_requests raise e File "/usr/local/lib/python3.12/dist-packages/vllm/ent...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: mistral3 offline multimodal inference example failing with prompt placeholder error bug;unstale ### Your current environment ### 🐛 Describe the bug The offline example for multimodal inference with `mistralai/Mis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: multimodal inference example failing with prompt placeholder error bug;unstale ### Your current environment ### 🐛 Describe the bug The offline example for multimodal inference with `mistralai/Mistral-Small-3.1-24B-Instr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cache;cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: g The offline example for multimodal inference with `mistralai/Mistral-Small-3.1-24B-Instruct-2503` and mistral_common 1.9.0 fails during pre-processing with: ```RuntimeError: Expected there to be 1 prompt placeholders...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: (EngineCore_DP0 pid=1126) INFO 02-04 21:08:56 [core.py:272] init engine (profile, create kv cache, warmup model) took 17.31 seconds INFO 02-04 21:08:56 [llm.py:349] Supported tasks: ['generate'] Adding requests: 0%|

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
