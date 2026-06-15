# vllm-project/vllm#34098: [Bug]: GLM-4.7-Flash requires transformers from git (glm4_moe_lite but Transformers does not recognize this architecture)

| 字段 | 值 |
| --- | --- |
| Issue | [#34098](https://github.com/vllm-project/vllm/issues/34098) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.7-Flash requires transformers from git (glm4_moe_lite but Transformers does not recognize this architecture)

### Issue 正文摘录

### Your current environment ## GLM 4.7 flash : Model architecture not supported GLM-4.7-Flash (`zai-org/GLM-4.7-Flash`) fails to load with vLLM because the model uses the `glm4_moe_lite` architecture which is only available in transformers `main` branch, not in any released PyPI version. Same issue as #33580 - GLM-4.7-Flash fails to load with `glm4_moe_lite` architecture error in vLLM nightly. ## Bug description GLM-4.7-Flash model fails to load with ValidationError despite using `trust_remote_code=True`. The error indicates Transformers doesn't recognize `glm4_moe_lite` architecture. ```python pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig Value error, The checkpoint you are trying to load has model type `glm4_moe_lite` but Transformers does not recognize this architecture. ``` ## Environment * vLLM: 0.15.1 (or even nightly) * vllm/vllm-openai:nightly and 0.15.1 Docker image * Model: zai-org/GLM-4.7-Flash ### config ```HCL - name: "glm-47-flash" repository: "vllm/vllm-openai" tag: "latest" # or nightly modelURL: "/data/models/glm-47-flash" replicaCount: 1 requestGPU: 1 requestCPU: 8 requestMemory: "64Gi" pvcStorage: "80Gi" storageClass: "shared-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: s only available in transformers `main` branch, not in any released PyPI version. Same issue as #33580 - GLM-4.7-Flash fails to load with `glm4_moe_lite` architecture error in vLLM nightly. ## Bug description GLM-4.7-Fl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: this architecture) bug ### Your current environment ## GLM 4.7 flash : Model architecture not supported GLM-4.7-Flash (`zai-org/GLM-4.7-Flash`) fails to load with vLLM because the model uses the `glm4_moe_lite` architec...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: fill: true enablePrefixCaching: true maxModelLen: 8192 dtype: "bfloat16" extraArgs: - "--disable-log-requests" - "--gpu-memory-utilization=0.60" - "--trust-remote-code" - "--enable-auto-tool-choice" - "--tool-call-parse...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ightly modelURL: "/data/models/glm-47-flash" replicaCount: 1 requestGPU: 1 requestCPU: 8 requestMemory: "64Gi" pvcStorage: "80Gi" storageClass: "shared-vast" vllmConfig: enableChunkedPrefill: true enablePrefixCaching: t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: m/entrypoints/cli/main.py", line 73, in main (APIServer pid=1) args.dispatch_function(args) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 111, in cmd (APIServer pid...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
