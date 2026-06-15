# vllm-project/vllm#26843: [Bug]: Undefined symbol cutlass_moe_mm_sm100 on SM120 CUDA builds (macro enabled, grouped_mm_c3x_sm100.cu not compiled)

| 字段 | 值 |
| --- | --- |
| Issue | [#26843](https://github.com/vllm-project/vllm/issues/26843) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Undefined symbol cutlass_moe_mm_sm100 on SM120 CUDA builds (macro enabled, grouped_mm_c3x_sm100.cu not compiled)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I built vLLM from source and in my terminal I ran: ```bash python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen1.5-MoE-A2.7B-Chat \ --port 8080 \ --dtype auto \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.92 \ --max-model-len 4096 \ --enable-lora \ --lora-modules qwen_moe_lora=/data/lora/moe_lora_dummy \ --log-level INFO ``` I got this error: ``` INFO 10-14 20:10:47 [__init__.py:224] Automatically detected platform cuda. Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/data/work/vllm/vllm/entrypoints/openai/api_server.py", line 41, in from vllm.config import VllmConfig File "/data/work/vllm/vllm/config/__init__.py", line 15, in from vllm.config.lora import LoRAConfig File "/data/work/vllm/vllm/config/lora.py", line 15, in from vllm.platforms import current_platform File "/data/work/vllm/vllm/platforms/__init__.py", line 254, in __getattr__ _current_platform = resolve_obj_by_qualname(platform_cls_qualname)() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/work/vllm/vllm/utils/__init__.py", line 2504, in resolve_obj_by_qualname modu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Undefined symbol cutlass_moe_mm_sm100 on SM120 CUDA builds (macro enabled, grouped_mm_c3x_sm100.cu not compiled) bug;stale ### Your current environment ### 🐛 Describe the bug I built vLLM from source and in my te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Undefined symbol cutlass_moe_mm_sm100 on SM120 CUDA builds (macro enabled, grouped_mm_c3x_sm100.cu not compiled) bug;stale ### Your current environment ### 🐛 Describe the bug I built vLLM from source and in my te...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rminal I ran: ```bash python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen1.5-MoE-A2.7B-Chat \ --port 8080 \ --dtype auto \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.92 \ --max-model-len 4096 \ -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Undefined symbol cutlass_moe_mm_sm100 on SM120 CUDA builds (macro enabled, grouped_mm_c3x_sm100.cu not compiled) bug;stale ### Your current environment ### 🐛 Describe the bug I built vLLM from source and in my te...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Undefined symbol cutlass_moe_mm_sm100 on SM120 CUDA builds (macro enabled, grouped_mm_c3x_sm100.cu not compiled) bug;stale ### Your current environment ### 🐛 Describe the bug I built vLLM from source and in my te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
