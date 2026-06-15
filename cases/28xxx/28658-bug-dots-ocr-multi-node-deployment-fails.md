# vllm-project/vllm#28658: [Bug]: dots.ocr multi-node deployment fails

| 字段 | 值 |
| --- | --- |
| Issue | [#28658](https://github.com/vllm-project/vllm/issues/28658) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: dots.ocr multi-node deployment fails

### Issue 正文摘录

### Your current environment I'm using the **vLLM Production Stack Helm chart** (0.1.7) --- ### Helm values ```yaml servingEngineSpec: runtimeClassName: "" modelSpec: - name: "dotsocr" repository: "vllm/vllm-openai" tag: "nightly" modelURL: "rednote-hilab/dots.ocr" replicaCount: 1 requestCPU: 10 requestMemory: "20Gi" requestGPU: 1 vllmConfig: v1: 1 tensorParallelSize: 1 pipelineParallelSize: 2 maxModelLen: 4096 dtype: "bfloat16" extraArgs: - "--trust-remote-code" - "--served-model-name=dotsocr" shmSize: "20Gi" raySpec: headNode: requestCPU: 15 requestMemory: "20Gi" requestGPU: 1 ``` ### 🐛 Describe the bug I'm running into an issue **specific to the model `rednote-hilab/dots.ocr`** when enabling distributed execution with: - tensor_parallel_size = 1 - pipeline_parallel_size = 2 (or higher) The **exact same setup works with other models** (Qwen, DeepSeek-OCR,...). Only `dots.ocr` crashes during engine initialization. I tried "latest" and "nightly" tags but same result. **Note:** If I simply change `modelURL` to another model, the deployment starts successfully. Single-Node Multi-GPU (tensor_parallel_size >=2 and pipeline_parallel_size=1 ) works fine with dots.ocr. --- ## Error logs...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: -- ### Helm values ```yaml servingEngineSpec: runtimeClassName: "" modelSpec: - name: "dotsocr" repository: "vllm/vllm-openai" tag: "nightly" modelURL: "rednote-hilab/dots.ocr" replicaCount: 1 requestCPU: 10 requestMemo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: equestGPU: 1 ``` ### 🐛 Describe the bug I'm running into an issue **specific to the model `rednote-hilab/dots.ocr`** when enabling distributed execution with: - tensor_parallel_size = 1 - pipeline_parallel_size = 2 (or...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ize: 1 pipelineParallelSize: 2 maxModelLen: 4096 dtype: "bfloat16" extraArgs: - "--trust-remote-code" - "--served-model-name=dotsocr" shmSize: "20Gi" raySpec: headNode: requestCPU: 15 requestMemory:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: " modelURL: "rednote-hilab/dots.ocr" replicaCount: 1 requestCPU: 10 requestMemory: "20Gi" requestGPU: 1 vllmConfig: v1: 1 tensorParallelSize: 1 pipelineParallelSize: 2 maxModelLen: 4096 dtype: "bfloat16" ex
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ...). Only `dots.ocr` crashes during engine initialization. I tried "latest" and "nightly" tags but same result. **Note:** If I simply change `modelURL` to another model, the deployment starts successfully. Single-Node...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
