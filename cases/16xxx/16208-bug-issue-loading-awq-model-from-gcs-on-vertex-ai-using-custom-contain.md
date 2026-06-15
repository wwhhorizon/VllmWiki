# vllm-project/vllm#16208: [Bug]:  Issue loading AWQ model from GCS on Vertex AI using Custom Container. How to use a custom model with LLM from GCS.

| 字段 | 值 |
| --- | --- |
| Issue | [#16208](https://github.com/vllm-project/vllm/issues/16208) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Issue loading AWQ model from GCS on Vertex AI using Custom Container. How to use a custom model with LLM from GCS.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Environment: Platform: Google Cloud Vertex AI Custom Container Deployment Container Image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:20250202_0916_RC00 vLLM Version: Logs indicate multiple potential versions within the container environment (potentially a patched 0.1.dev1+g4f51006.d20250202 or a base 0.8.2 - clarification needed). Deployment Method: Using Vertex AI Python SDK (aiplatform.Model.upload) with artifact_uri pointing to a GCS location, relying on the container's internal logic to use AIP_STORAGE_URI. Container arguments specified during Model.upload. Hardware: g2-standard-8 machine with 1 x NVIDIA_L4 GPU. Model: Custom model, quantized using AWQ. Stored in GCS bucket (gs://custom-model/model/my_model_awq/). Problem Description: When attempting to deploy the custom AWQ model to a Vertex AI endpoint using the specified Google container image, the deployment fails during container startup. Initial Error (Container Logs): With container arguments --quantization=awq --dtype=half set during Model.upload, the container fails with: ValueError: Cannot find the config file for awq Troubles...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: : Google Cloud Vertex AI Custom Container Deployment Container Image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:20250202_0916_RC00 vLLM Version: Logs indicate multiple potential v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: are: g2-standard-8 machine with 1 x NVIDIA_L4 GPU. Model: Custom model, quantized using AWQ. Stored in GCS bucket (gs://custom-model/model/my_model_awq/). Problem Description: When attempting to deploy the custom AWQ mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Issue loading AWQ model from GCS on Vertex AI using Custom Container. How to use a custom model with LLM from GCS. bug ### Your current environment ### 🐛 Describe the bug Environment: Platform: Google Cloud Verte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
