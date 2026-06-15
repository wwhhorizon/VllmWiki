# vllm-project/vllm#28278: [Bug]: vLLM v0.11.0 container in k8s pod Fails to Load GLM-4.6-FP8 Model During CUDA Graph Capture， But v0.10.2 is OK.

| 字段 | 值 |
| --- | --- |
| Issue | [#28278](https://github.com/vllm-project/vllm/issues/28278) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM v0.11.0 container in k8s pod Fails to Load GLM-4.6-FP8 Model During CUDA Graph Capture， But v0.10.2 is OK.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GLM-4.6 Model is [GLM-4.6-FP8](https://modelscope.cn/models/ZhipuAI/GLM-4.6-FP8). ## Reproduction Steps 1. Deploy GLM-4.6 model using vLLM v0.10.2 with the specified parameters - works correctly 2. Deploy GLM-4.6 model using the same parameters with vLLM v0.11.0 3. Application starts initialization but crashes during CUDA Graph capture phase ## Observed Behavior - vLLM v0.10.2: Model loads successfully and operates normally - vLLM v0.11.0: Application exits abnormally during "Capture CUDA Graph" phase ## Expected Behavior vLLM v0.11.0 should be able to load GLM-4.6 model using the same parameters that work in v0.10.2 without requiring configuration changes. ## Error Details - **Failure point**: CUDA Graph capture phase - **Result**: Application exit/termination - **Version dependency**: Issue only occurs in v0.11.0, not in v0.10.2 ## YAML ```yaml servingEngineSpec: enableEngine: true labels: environment: "production" release: "production" modelSpec: # GLM-4.6-FP8 - name: "glm-46x" repository: "vllm/vllm-openai" tag: "v0.11.0" modelURL: "GLM-4.6x" imagePullPolicy: "IfNotPresent" nodeSelectorTerms: - matchExpressions: - key: kubern...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eproduction Steps 1. Deploy GLM-4.6 model using vLLM v0.10.2 with the specified parameters - works correctly 2. Deploy GLM-4.6 model using the same parameters with vLLM v0.11.0 3. Application starts initialization but c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Load GLM-4.6-FP8 Model During CUDA Graph Capture， But v0.10.2 is OK. bug;stale ### Your current environment ### 🐛 Describe the bug GLM-4.6 Model is [GLM-4.6-FP8](https://modelscope.cn/models/ZhipuAI/GLM-4.6-FP8). ## Rep...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: vLLM v0.11.0 container in k8s pod Fails to Load GLM-4.6-FP8 Model During CUDA Graph Capture， But v0.10.2 is OK. bug;stale ### Your current environment ### 🐛 Describe the bug GLM-4.6 Model is [GLM-4.6-FP8](https:/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vLLM v0.11.0 container in k8s pod Fails to Load GLM-4.6-FP8 Model During CUDA Graph Capture， But v0.10.2 is OK. bug;stale ### Your current environment ### 🐛 Describe the bug GLM-4.6 Model is [GLM-4.6-FP8](https://models...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM v0.11.0 container in k8s pod Fails to Load GLM-4.6-FP8 Model During CUDA Graph Capture， But v0.10.2 is OK. bug;stale ### Your current environment ### 🐛 Describe the bug GLM-4.6 Model is [GLM-4.6-FP8](https:/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
