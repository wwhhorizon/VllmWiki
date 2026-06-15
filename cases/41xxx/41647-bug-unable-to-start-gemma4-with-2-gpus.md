# vllm-project/vllm#41647: [Bug]: Unable to start Gemma4 with 2 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#41647](https://github.com/vllm-project/vllm/issues/41647) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to start Gemma4 with 2 GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running gemma4 on 2 h200 GPUs, vllm stalls with this message on an openshift cluster, I've tested with version version 0.20.0 and 0.19.1. Settings ```yaml apiVersion: apps/v1 kind: Deployment metadata: namespace: genai-models name: google-gemma-4-31b-it-h200-vllm-deploy labels: app: google-gemma-4-31b-it-3-deploy app.kubernetes.io/part-of: google-gemma-4-31b-it-vllm spec: replicas: 1 revisionHistoryLimit: 1 strategy: type: Recreate selector: matchLabels: app: google-gemma-4-31b-it-vllm-pod template: metadata: labels: app: google-gemma-4-31b-it-vllm-pod spec: serviceAccountName: genai-models-anyuid-serviceaccount securityContext: privileged: true volumes: - name: model persistentVolumeClaim: claimName: huggingface-pv-filesystem - name: dshm emptyDir: medium: Memory sizeLimit: "32G" containers: - name: google-gemma-4-31b-it-vllm-pod command: ["/bin/sh", "-c"] args: - > vllm serve google/gemma-4-31B-it --served-model-name google/gemma-4-31B-it --kv-cache-dtype fp8 --max-model-len 200000 --dtype auto --async-scheduling --tensor-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.90 --enable-chunked-prefill --enable-au...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: e --gpu-memory-utilization 0.90 --enable-chunked-prefill --enable-auto-tool-choice --reasoning-parser gemma4 --tool-call-parser gemma4 --limit-mm-per-prompt '{"image": 2, "audio": 1}' --chat-template exampl
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vllm stalls with this message on an openshift cluster, I've tested with version version 0.20.0 and 0.19.1. Settings ```yaml apiVersion: apps/v1 kind: Deployment metadata: namespace: genai-models name: google-gemma-4-31b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Unable to start Gemma4 with 2 GPUs bug ### Your current environment ### 🐛 Describe the bug When running gemma4 on 2 h200 GPUs, vllm stalls with this message on an openshift cluster, I've tested with version versi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --served-model-name google/gemma-4-31B-it --kv-cache-dtype fp8 --max-model-len 200000 --dtype auto --async-scheduling --tensor-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.90
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: onnector_stats=None, waiting_lora_adapters={}, running_lora_adapters={}, cudagraph_stats=None, perf_stats=None) (EngineCore pid=591) ERROR 05-04 08:51:40 [v1/engine/core.py:1138] EngineCore encountered a fatal error. (E...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
