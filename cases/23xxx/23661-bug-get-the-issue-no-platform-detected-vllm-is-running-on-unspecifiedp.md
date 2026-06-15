# vllm-project/vllm#23661: [Bug]: Get the issue No platform detected, vLLM is running on UnspecifiedPlatform when deploy on kubernetes using GPU time slicing

| 字段 | 值 |
| --- | --- |
| Issue | [#23661](https://github.com/vllm-project/vllm/issues/23661) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Get the issue No platform detected, vLLM is running on UnspecifiedPlatform when deploy on kubernetes using GPU time slicing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am deploying my project to Elastic Kubernetes Service. Below is my config when running on docker. which is alrady running well: ``` vllm: image: vllm/vllm-openai:v0.9.2 command: [ "--model=/root/model/model_v0.0", "--served-model-name=model_cni_v1", "--port=8008", "--max-num-seqs=4", "--max_model_len=32000", "--limit-mm-per-promp=image=10", "--quantization=fp8", "--trust-remote-code" ] ports: - "8008:8008" deploy: resources: reservations: devices: - capabilities: [gpu] ipc: host ``` Then I convert into deployment to deploy to kubernetes ``` apiVersion: apps/v1 kind: Deployment metadata: name: vllm labels: app: vllm spec: replicas: 1 selector: matchLabels: app: vllm template: metadata: labels: app: vllm spec: containers: - name: vllm image: vllm/vllm-openai:v0.9.2 command: - python3 - -m - vllm.entrypoints.openai.api_server - --model=/root/model/model_v0.0 - --served-model-name=model_cni_v1 - --port=8008 - --max-num-seqs=4 - --max_model_len=32000 - --limit-mm-per-promp=image=10 - --quantization=fp8 - --trust-remote-code ports: - containerPort: 8008 resources: limits: nvidia.com/gpu: 1 volumeMounts: - name: model-volume mountPath...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Get the issue No platform detected, vLLM is running on UnspecifiedPlatform when deploy on kubernetes using GPU time slicing bug;stale ### Your current environment ### 🐛 Describe the bug I am deploying my project...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ax_model_len=32000", "--limit-mm-per-promp=image=10", "--quantization=fp8", "--trust-remote-code" ] ports: - "8008:8008" deploy: resources: reservations: devices: - capabilities: [gpu] ipc: host ``` Then I con
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ing on UnspecifiedPlatform /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:991: UserWarning: CUDA initialization: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: logits;speculative_decoding cuda;fp8;gemm;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ug I am deploying my project to Elastic Kubernetes Service. Below is my config when running on docker. which is alrady running well: ``` vllm: image: vllm/vllm-openai:v0.9.2 command: [ "--model=/root/model/model_v0.0",...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23662: Should have ROCm label: NO (0 matches) #23661: Should have ROCm label: NO (0 matches) #23655: Should have ROCm label: NO (0 matches) #23645: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
