# vllm-project/vllm#32410: [Bug][XPU]: Failed to serve w4a16 Qwen3 VL MoE on Intel Arc Pro B60

| 字段 | 值 |
| --- | --- |
| Issue | [#32410](https://github.com/vllm-project/vllm/issues/32410) |
| 状态 | closed |
| 标签 | bug;intel-gpu;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][XPU]: Failed to serve w4a16 Qwen3 VL MoE on Intel Arc Pro B60

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to run a w4a16 weight (EmbeddedLLM/Qwen3-VL-30B-A3B-Instruct.w4a16) created using llm_compressor. The weight is working fine on A10, and mi300x. However, when i tried to use it with Intel Arc Pro B60 I encountered the following error. The weight loaded, however, when trying to determined the vram usage it failed. I'm following the build command from the docs, and built the docker image using the branch `releases/v0.14.0` command: ``` VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_TARGET_DEVICE=xpu vllm serve EmbeddedLLM/Qwen3-VL-30B-A3B-Instruct.w4a16 --tensor-parallel-size 4 --data-parallel-size 1 --max-model-len 65536 --enforce-eager --block-size 64 --max_num_batched_tokens 8192 --disable-log-requests --port 8006 ``` Error: ``` [0;36m(APIServer pid=2616)[0;0m INFO 01-15 10:42:37 [api_server.py:1278] vLLM API server version 0.14.0rc2.dev2+g2c24bc699 [0;36m(APIServer pid=2616)[0;0m INFO 01-15 10:42:37 [utils.py:254] non-default args: {'model_tag': 'EmbeddedLLM/Qwen3-VL-30B-A3B-Instruct.w4a16', 'port': 8006, 'model': 'EmbeddedLLM/Qwen3-VL-30B-A3B-Instruct.w4a16', 'trust_remote_code': True, 'max_model_len': 65536, 'enforce_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: when trying to determined the vram usage it failed. I'm following the build command from the docs, and built the docker image using the branch `releases/v0.14.0` command: ``` VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_TARG...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug][XPU]: Failed to serve w4a16 Qwen3 VL MoE on Intel Arc Pro B60 bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug I'm trying to run a w4a16 weight (EmbeddedLLM/Qwen3-VL-30B-A3B-Instruct.w4a16)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 16) created using llm_compressor. The weight is working fine on A10, and mi300x. However, when i tried to use it with Intel Arc Pro B60 I encountered the following error. The weight loaded, however, when trying to deter...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Bug][XPU]: Failed to serve w4a16 Qwen3 VL MoE on Intel Arc Pro B60 bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug I'm trying to run a w4a16 weight (EmbeddedLLM/Qwen3-VL-30B-A3B-Instruct.w4a16)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ]: Failed to serve w4a16 Qwen3 VL MoE on Intel Arc Pro B60 bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug I'm trying to run a w4a16 weight (EmbeddedLLM/Qwen3-VL-30B-A3B-Instruct.w4a16) created u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
