# vllm-project/vllm#29369: [Bug]: nixl connector PD disagg stuck at INFO logging level

| 字段 | 值 |
| --- | --- |
| Issue | [#29369](https://github.com/vllm-project/vllm/issues/29369) |
| 状态 | open |
| 标签 | bug |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;gemm;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nixl connector PD disagg stuck at INFO logging level

### Issue 正文摘录

### Your current environment / ### 🐛 Describe the bug cc EPD authors @fake0fan @knlnguyen1802 @herotai214 @khuonglmhw cc @NickLucche Following #29248 having issue with the EPD disagg feature, I found that simply running PD disagg with nixl connector with `export VLLM_LOGGING_LEVEL=INFO` would also stuck at the decode instance when streaming for the 1st request. `export VLLM_LOGGING_LEVEL=DEBUG` avoids the issue and works fine, but I think there are still some defects that worth paying attention... My starting script for PD disagg with nixl connector using `/tests/v1/kv_connector/nixl_integration/toy_proxy_server.py`: ```shell #!/bin/bash set -xe echo "🚧🚧 Running NIXL CONNECTOR!!!!!!!! 🚧🚧" MODEL_NAME= LOG_PATH= mkdir -p $LOG_PATH # Cleanup function cleanup() { echo "Stopping everything…" trap - INT TERM USR1 # prevent re-entrancy # Kill all tracked PIDs for pid in "${PIDS[@]}"; do if kill -0 "$pid" 2>/dev/null; then echo "Killing process $pid" kill "$pid" 2>/dev/null fi done # Wait a moment for graceful shutdown sleep 2 # Force kill any remaining processes for pid in "${PIDS[@]}"; do if kill -0 "$pid" 2>/dev/null; then echo "Force killing process $pid" kill -9 "$pid" 2>/dev/null fi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: `shell #!/bin/bash set -xe echo "🚧🚧 Running NIXL CONNECTOR!!!!!!!! 🚧🚧" MODEL_NAME= LOG_PATH= mkdir -p $LOG_PATH # Cleanup function cleanup() { echo "Stopping everything…" trap - INT TERM USR1 # prevent re-entrancy # Kil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: connector with `export VLLM_LOGGING_LEVEL=INFO` would also stuck at the decode instance when streaming for the 1st request. `export VLLM_LOGGING_LEVEL=DEBUG` avoids the issue and works fine, but I think there are still...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory attention;cache;cuda;gemm;quantization;sampling slowdown dtype;env_dependency;memory_layout Your cur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ne" && return 0 || return 1 } ### NIXL A=2 B=3 C=6661 D=6662 PORT=9775 CUDA_VISIBLE_DEVICES=$A VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve $MODEL_NAME \ --port $C \ --enforce-eager \ --gpu-memory-utilization 0.8 \ --tru...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: mance attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory attention;cache;cuda;gemm;quantization;sampling slowdown dtype;env_dependency;mem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
