# vllm-project/vllm#22793: [Usage]: VLLM crash - Latest Docker Image - GPT-OSS-20B - on RTX5090

| 字段 | 值 |
| --- | --- |
| Issue | [#22793](https://github.com/vllm-project/vllm/issues/22793) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;kernel;moe;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: VLLM crash - Latest Docker Image - GPT-OSS-20B - on RTX5090

### Issue 正文摘录

### Your current environment I tried to use the 20b model on my one RTX5090 with the latest docker image. Sadly VLLM crash quite quickly. I can watch how the model gets loaded into the VRAM of the RTX 5090 but than gets unloaded in matter of the crash. Someone can help? **Docker Startup** sudo docker run \ --gpus device=1 \ -v $HOME/.cache/huggingface:/root/.cache/huggingface \ --name vllmgpt \ -p 5678:8000 \ --ipc=host \ -e VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 \ -e VLLM_USE_TRTLLM_ATTENTION=1 \ -e VLLM_USE_TRTLLM_DECODE_ATTENTION=1 \ -e VLLM_USE_TRTLLM_CONTEXT_ATTENTION=1 \ -e VLLM_USE_FLASHINFER_MXFP4_MOE=1 \ vllm/vllm-openai:gptoss \ --model openai/gpt-oss-20b \ --async-scheduling **LOG**: ```text INFO 08-12 14:36:59 [__init__.py:241] Automatically detected platform cuda. ESC[1;36m(APIServer pid=1)ESC[0;0m INFO 08-12 14:37:01 [api_server.py:1787] vLLM API server version 0.10.2.dev2+gf5635d62e.d20250807 ESC[1;36m(APIServer pid=1)ESC[0;0m INFO 08-12 14:37:01 [utils.py:326] non-default args: {'model': 'openai/gpt-oss-20b', 'async_scheduling': True} ESC[1;36m(APIServer pid=1)ESC[0;0m INFO 08-12 14:37:09 [config.py:726] Resolved architecture: GptOssForCausalLM ESC[1;36m(APISer...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Usage]: VLLM crash - Latest Docker Image - GPT-OSS-20B - on RTX5090 usage;stale ### Your current environment I tried to use the 20b model on my one RTX5090 with the latest docker image. Sadly VLLM crash quite quickly....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: \ -e VLLM_USE_TRTLLM_CONTEXT_ATTENTION=1 \ -e VLLM_USE_FLASHINFER_MXFP4_MOE=1 \ vllm/vllm-openai:gptoss \ --model openai/gpt-oss-20b \ --async-scheduling **LOG**: ```text INFO 08-12 14:36:59 [__init__.py:241] Automatica...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: sage]: VLLM crash - Latest Docker Image - GPT-OSS-20B - on RTX5090 usage;stale ### Your current environment I tried to use the 20b model on my one RTX5090 with the latest docker image. Sadly VLLM crash quite quickly. I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: VLLM crash - Latest Docker Image - GPT-OSS-20B - on RTX5090 usage;stale ### Your current environment I tried to use the 20b model on my one RTX5090 with the latest docker image. Sadly VLLM crash quite quickly....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: VLLM crash - Latest Docker Image - GPT-OSS-20B - on RTX5090 usage;stale ### Your current environment I tried to use the 20b model on my one RTX5090 with the latest docker image. Sadly VLLM crash quite quickly....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
