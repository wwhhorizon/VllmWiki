# vllm-project/vllm#38309: [Bug]: microsoft/Phi-4-reasoning-vision-15B Fails to startup

| 字段 | 值 |
| --- | --- |
| Issue | [#38309](https://github.com/vllm-project/vllm/issues/38309) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: microsoft/Phi-4-reasoning-vision-15B Fails to startup

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve \ microsoft/Phi-4-reasoning-vision-15B \ -tp 2 \ --trust-remote-code \ --async-scheduling \ --enable-chunked-prefill \ --enable-prefix-caching \ --limit-mm-per-prompt '{"image": 10}' ``` fails to load the model ``` (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:297] (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:297] █ █ █▄ ▄█ (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:297] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.18.0 (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:297] █▄█▀ █ █ █ █ model microsoft/Phi-4-reasoning-vision-15B (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:297] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:297] (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:233] non-default args: {'model_tag': 'microsoft/Phi-4-reasoning-vision-15B', 'model': 'microsoft/Phi-4-reasoning-vision-15B', 'trust_remote_code': True, 'tensor_parallel_size': 2, 'enable_prefix_caching': True, 'limit_mm_per_prompt': {'image': 10}, 'enable_chunked_prefill': True, 'async_scheduling': True} (APIServer pid=1481120) A new version of the following files was downloaded from htt...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: caching \ --limit-mm-per-prompt '{"image": 10}' ``` fails to load the model ``` (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:297] (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:297] █ █ █▄ ▄█ (APIServer...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: =1481120) INFO 03-23 16:02:22 [utils.py:297] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.18.0 (APIServer pid=1481120) INFO 03-23 16:02:22 [utils.py:297] █▄█▀ █ █ █ █ model microsoft/Phi-4-reasoning-vision-15B (APIServer pid=1481120) IN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ion. (APIServer pid=1481120) INFO 03-23 16:02:31 [model.py:533] Resolved architecture: TransformersForCausalLM (APIServer pid=1481120) INFO 03-23 16:02:31 [model.py:1582] Using max model len 32768 (APIServer pid=1481120...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: tp 2 \ --trust-remote-code \ --async-scheduling \ --enable-chunked-prefill \ --enable-prefix-caching \ --limit-mm-per-prompt '{"image": 10}' ``` fails to load the model ``` (APIServer pid=1481120) INFO 03-23 16:02:22 [u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
