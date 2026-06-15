# vllm-project/vllm#36615: [Bug]: unknown error trying to run vllm v0.17.0 with ROCm on Radeon 8060S (gfx1151)

| 字段 | 值 |
| --- | --- |
| Issue | [#36615](https://github.com/vllm-project/vllm/issues/36615) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: unknown error trying to run vllm v0.17.0 with ROCm on Radeon 8060S (gfx1151)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text vllm serve Qwen/Qwen2.5-1.5B-Instruct ``` Results in an error, but for the life of me I can't see what it is in this backtrace and I suspect the root cause is actually absent from this log output: ```text WARNING 03-10 19:47:32 [gpt_oss_triton_kernels_moe.py:56] Using legacy triton_kernels on ROCm (APIServer pid=407452) INFO 03-10 19:47:33 [utils.py:302] (APIServer pid=407452) INFO 03-10 19:47:33 [utils.py:302] █ █ █▄ ▄█ (APIServer pid=407452) INFO 03-10 19:47:33 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.0 (APIServer pid=407452) INFO 03-10 19:47:33 [utils.py:302] █▄█▀ █ █ █ █ model Qwen/Qwen2.5-1.5B-Instruct (APIServer pid=407452) INFO 03-10 19:47:33 [utils.py:302] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=407452) INFO 03-10 19:47:33 [utils.py:302] (APIServer pid=407452) INFO 03-10 19:47:33 [utils.py:238] non-default args: {'model_tag': 'Qwen/Qwen2.5-1.5B-Instruct', 'model': 'Qwen/Qwen2.5-1.5B-Instruct'} (APIServer pid=407452) INFO 03-10 19:47:35 [model.py:531] Resolved architecture: Qwen2ForCausalLM (APIServer pid=407452) INFO 03-10 19:47:35 [model.py:1554] Using max model len 32768 (APIServer pid=407452) INFO 03-10 19:47:35...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d=407452) INFO 03-10 19:47:33 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.0 (APIServer pid=407452) INFO 03-10 19:47:33 [utils.py:302] █▄█▀ █ █ █ █ model Qwen/Qwen2.5-1.5B-Instruct (APIServer pid=407452) INFO 03-10 19:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Your current environment ### 🐛 Describe the bug ```text vllm serve Qwen/Qwen2.5-1.5B-Instruct ``` Results in an error, but for the life of me I can't see what it is in this backtrace and I suspect the root cause is actu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: ly absent from this log output: ```text WARNING 03-10 19:47:32 [gpt_oss_triton_kernels_moe.py:56] Using legacy triton_kernels on ROCm (APIServer pid=407452) INFO 03-10 19:47:33 [utils.py:302] (APIServer pid=407452) INFO...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: unknown error trying to run vllm v0.17.0 with ROCm on Radeon 8060S (gfx1151) bug;rocm ### Your current environment ### 🐛 Describe the bug ```text vllm serve Qwen/Qwen2.5-1.5B-Instruct ``` Results in an error, but...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
