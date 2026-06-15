# vllm-project/vllm#21278: [Performance]: Speculative decoding doesn't seem to speed up inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#21278](https://github.com/vllm-project/vllm/issues/21278) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Speculative decoding doesn't seem to speed up inference?

### Issue 正文摘录

### Proposal to improve performance I want to improve the inference speed of Qwen3-32B-FP8 on NVIDIA L20. Currently, the inference speed is as follows: - Single card: 13-14 tokens/s - Dual cards: 20-21 tokens/s So I try VLLM's speculative decoding with Qwen3's small sized models, executing a command like this: ``` python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9997 --model "/path/to/Qwen3-32B-FP8/" --served-model-name qwen3 --seed 42 --max-model-len 10240 -tp 2 --speculative_config '{"model": "/path/to/Qwen3-4B-FP8/", "max_model_len": 10240, "num_speculative_tokens": 3}' ``` But it turns out that it leads to a slower inference speed (around 10-11 tokens/s). I don't know if it's normal. By the way, I would appreciate it if you have any other suggestions for improving this model's inference speed... ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake ver...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: 10-11 tokens/s). I don't know if it's normal. By the way, I would appreciate it if you have any other suggestions for improving this model's inference speed... ### Report of performance regression _No response_ ### Misc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: cards: 20-21 tokens/s So I try VLLM's speculative decoding with Qwen3's small sized models, executing a command like this: ``` python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9997 --model "/path/to/Qw...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: improve performance I want to improve the inference speed of Qwen3-32B-FP8 on NVIDIA L20. Currently, the inference speed is as follows: - Single card: 13-14 tokens/s - Dual cards: 20-21 tokens/s So I try VLLM's speculat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: roposal to improve performance I want to improve the inference speed of Qwen3-32B-FP8 on NVIDIA L20. Currently, the inference speed is as follows: - Single card: 13-14 tokens/s - Dual cards: 20-21 tokens/s So I try VLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Speculative decoding doesn't seem to speed up inference? performance;stale ### Proposal to improve performance I want to improve the inference speed of Qwen3-32B-FP8 on NVIDIA L20. Currently, the inferenc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
