# vllm-project/vllm#14415: [Bug]: vLLM-0.7.2 reports "No CUDA GPUs are available" while vllm-0.6.6.post1 works fine on kuberay under same environment conditions.

| 字段 | 值 |
| --- | --- |
| Issue | [#14415](https://github.com/vllm-project/vllm/issues/14415) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM-0.7.2 reports "No CUDA GPUs are available" while vllm-0.6.6.post1 works fine on kuberay under same environment conditions.

### Issue 正文摘录

### Your current environment ## 🐛 Describe the bug ### Description When deploying Qwen2.5-0.5B model using kuberay with vLLM 0.7.2, encountering "RuntimeError: No CUDA GPUs are available" error. However, the same deployment works fine with vLLM 0.6.6.post1 under identical environment conditions. ### Environment Information - Container Image: rayproject/ray:2.43.0-py39-cu124 - vLLM: - Failed version: 0.7.2 - Working version: 0.6.6.post1 - Model: Qwen2.5-0.5B ### Steps to Reproduce Using kuberay to deploy `RayService` with image `rayproject/ray:2.43.0-py39-cu124`, the RayService is: ```yam apiVersion: ray.io/v1 kind: RayService metadata: name: qwen2005-0005b-vllm07 spec: serveConfigV2: | applications: - name: llm route_prefix: / import_path: latest-serve:model deployments: - name: VLLMDeployment num_replicas: 1 ray_actor_options: num_cpus: 4 runtime_env: working_dir: "https://xxx/vllm_script.zip" pip: - "vllm==0.7.2" env_vars: MODEL_ID: "Qwen/Qwen2.5-0.5B" TENSOR_PARALLELISM: "1" PIPELINE_PARALLELISM: "1" rayClusterConfig: headGroupSpec: rayStartParams: dashboard-host: '0.0.0.0' template: spec: containers: - name: ray-head image: rayproject/ray:2.43.0-py39-cu124 imagePullPolicy: IfN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: - Container Image: rayproject/ray:2.43.0-py39-cu124 - vLLM: - Failed version: 0.7.2 - Working version: 0.6.6.post1 - Model: Qwen2.5-0.5B ### Steps to Reproduce Using kuberay to deploy `RayService` with image `rayproject...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: nt environment ## 🐛 Describe the bug ### Description When deploying Qwen2.5-0.5B model using kuberay with vLLM 0.7.2, encountering "RuntimeError: No CUDA GPUs are available" error. However, the same deployment works fin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vLLM-0.7.2 reports "No CUDA GPUs are available" while vllm-0.6.6.post1 works fine on kuberay under same environment conditions. bug;ray;stale ### Your current environment ## 🐛 Describe the bug ### Description Whe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: cu124`, the RayService is: ```yam apiVersion: ray.io/v1 kind: RayService metadata: name: qwen2005-0005b-vllm07 spec: serveConfigV2: | applications: - name: llm route_prefix: / import_path: latest-serve:model deployments...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 6.post1 works fine on kuberay under same environment conditions. bug;ray;stale ### Your current environment ## 🐛 Describe the bug ### Description When deploying Qwen2.5-0.5B model using kuberay with vLLM 0.7.2, encounte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
