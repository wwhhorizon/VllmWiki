# vllm-project/vllm#28854: [Bug]: Deploy vllm on kubernetes: RuntimeError: Unexpected error from cudaGetDeviceCount()

| 字段 | 值 |
| --- | --- |
| Issue | [#28854](https://github.com/vllm-project/vllm/issues/28854) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deploy vllm on kubernetes: RuntimeError: Unexpected error from cudaGetDeviceCount()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I try deploy a vllm deployment example on a kubernetes cluster, I get the following error output: And abou the deployment file: The part that confuses me most is that when I start a new pod and use the same image and command, the pod reports no problem: ```text kubectl get pod NAME READY STATUS RESTARTS AGE vllm-pod 1/1 Running 0 2d22h ``` The nvidia driver, nvidia container toolkit and nvidia gpu operator is installed: ```text gpu-operator gpu-feature-discovery-fhmqg 1/1 Running 0 2d21h gpu-operator gpu-feature-discovery-krqlb 1/1 Running 0 2d21h gpu-operator gpu-operator-1763128337-node-feature-discovery-gc-7546fc4dwzf7b 1/1 Running 0 2d21h gpu-operator gpu-operator-1763128337-node-feature-discovery-master-64869klw6 1/1 Running 0 2d21h gpu-operator gpu-operator-1763128337-node-feature-discovery-worker-9dcht 1/1 Running 0 2d21h gpu-operator gpu-operator-1763128337-node-feature-discovery-worker-kn4k7 1/1 Running 0 2d21h gpu-operator gpu-operator-58bd54b485-xqglk 1/1 Running 0 2d21h gpu-operator nvidia-container-toolkit-daemonset-85c92 1/1 Running 0 2d21h gpu-operator nvidia-container-toolkit-daemonset-pbx9p 1/1 Running 0 2d2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: The nvidia driver, nvidia container toolkit and nvidia gpu operator is installed: ```text gpu-operator gpu-feature-discovery-fhmqg 1/1 Running 0 2d21h gpu-operator gpu-feature-discovery-krqlb
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Deploy vllm on kubernetes: RuntimeError: Unexpected error from cudaGetDeviceCount() bug ### Your current environment ### 🐛 Describe the bug When I try deploy a vllm deployment example on a kubernetes cluster, I g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency;shape Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: GI CI PID Type Process name GPU Memory | | ID ID Usage | |=========================================================================================| | No running processes

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
