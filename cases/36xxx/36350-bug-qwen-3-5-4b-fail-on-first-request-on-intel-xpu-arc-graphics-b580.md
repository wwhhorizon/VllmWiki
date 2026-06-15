# vllm-project/vllm#36350: [Bug]: Qwen 3.5 4B fail on first request on Intel XPU (Arc Graphics B580)

| 字段 | 值 |
| --- | --- |
| Issue | [#36350](https://github.com/vllm-project/vllm/issues/36350) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen 3.5 4B fail on first request on Intel XPU (Arc Graphics B580)

### Issue 正文摘录

### Your current environment 2x Intel Arc B580 12GB GPUs ### 🐛 Describe the bug Qwen 3 models runs fine, but the new Qwen 3.5 models seems to load just fine but then crash on first request of inference. Seeing the open PR https://github.com/vllm-project/vllm/pull/33657 is Qwen 3.5 not supported on XPU yet? Start command: ``` #!/bin/bash export VLLM_TARGET_DEVICE=xpu export VLLM_WORKER_MULTIPROC_METHOD=spawn vllm serve /home/arli/models/Qwen3.5-4B \ --gpu-memory-utilization 0.9 --max-model-len 16384 --port 8000 \ --max-num-seqs 8 -tp 2 --attention-backend TRITON_ATTN \ --served-model-name test ``` ``` (vllm) arli@arli-arc-server:~/vllm$ ./qwen.sh (APIServer pid=9233) INFO 03-07 12:28:30 [utils.py:292] (APIServer pid=9233) INFO 03-07 12:28:30 [utils.py:292] █ █ █▄ ▄█ (APIServer pid=9233) INFO 03-07 12:28:30 [utils.py:292] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.1.dev14581+g85f50eb41 (APIServer pid=9233) INFO 03-07 12:28:30 [utils.py:292] █▄█▀ █ █ █ █ model /home/arli/models/Qwen3.5-4B (APIServer pid=9233) INFO 03-07 12:28:30 [utils.py:292] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=9233) INFO 03-07 12:28:30 [utils.py:292] (APIServer pid=9233) INFO 03-07 12:28:30 [utils.py:228] non-default args: {'model_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen 3.5 4B fail on first request on Intel XPU (Arc Graphics B580) bug ### Your current environment 2x Intel Arc B580 12GB GPUs ### 🐛 Describe the bug Qwen 3 models runs fine, but the new Qwen 3.5 models seems to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: pid=9233) INFO 03-07 12:28:30 [utils.py:292] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.1.dev14581+g85f50eb41 (APIServer pid=9233) INFO 03-07 12:28:30 [utils.py:292] █▄█▀ █ █ █ █ model /home/arli/models/Qwen3.5-4B (APIServer pid=9233)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Qwen 3.5 4B fail on first request on Intel XPU (Arc Graphics B580) bug ### Your current environment 2x Intel Arc B580 12GB GPUs ### 🐛 Describe the bug Qwen 3 models runs fine, but the new Qwen 3.5 models seems to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 9 --max-model-len 16384 --port 8000 \ --max-num-seqs 8 -tp 2 --attention-backend TRITON_ATTN \ --served-model-name test ``` ``` (vllm) arli@arli-arc-server:~/vllm$ ./qwen.sh (APIServer pid=9233) INFO 03-07 12:28:30 [uti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
