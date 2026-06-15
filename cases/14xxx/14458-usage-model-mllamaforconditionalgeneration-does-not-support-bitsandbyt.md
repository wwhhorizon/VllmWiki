# vllm-project/vllm#14458: [Usage]: Model MllamaForConditionalGeneration does not support BitsAndBytes quantization yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#14458](https://github.com/vllm-project/vllm/issues/14458) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Model MllamaForConditionalGeneration does not support BitsAndBytes quantization yet.

### Issue 正文摘录

I'm trying to deploy VLLM into a Sagemaker endpoint for a fine tuned meta-llama/Llama-3.2-11B-Vision model lora adapter using quantization following this [tutorial.](https://aws.amazon.com/blogs/machine-learning/easily-deploy-and-manage-hundreds-of-lora-adapters-with-sagemaker-efficient-multi-adapter-inference/) I can see that quantization has been supported [since 0.6.4](https://github.com/vllm-project/vllm/releases/tag/v0.6.4). In the cloudwatch logs I'm seeing `Model MllamaForConditionalGeneration does not support BitsAndBytes quantization yet.` I'm using the following code. Notice that the inference_image_uri comes from [here](https://github.com/aws/deep-learning-containers/blob/master/available_images.md), and it uses VLLM==0.7.1. ``` inference_image_uri = "763104351884.dkr.ecr.us-east-2.amazonaws.com/djl-inference:0.32.0-lmi14.0.0-cu126" env = { "HF_MODEL_ID": f"{s3_model_path}", "OPTION_ROLLING_BATCH": "lmi-dist", "OPTION_MAX_ROLLING_BATCH_SIZE": "16", "OPTION_TENSOR_PARALLEL_DEGREE": "max", "OPTION_ENABLE_LORA": "true", "OPTION_MAX_LORAS": "30", "OPTION_MAX_CPU_LORAS": "70", "OPTION_DTYPE": "fp16", "OPTION_MAX_MODEL_LEN": "6000", "OPTION_QUANTIZE": "bitsandbytes", "OPTION_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Model MllamaForConditionalGeneration does not support BitsAndBytes quantization yet. usage I'm trying to deploy VLLM into a Sagemaker endpoint for a fine tuned meta-llama/Llama-3.2-11B-Vision model lora adapter...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: age]: Model MllamaForConditionalGeneration does not support BitsAndBytes quantization yet. usage I'm trying to deploy VLLM into a Sagemaker endpoint for a fine tuned meta-llama/Llama-3.2-11B-Vision model lora adapter us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng/easily-deploy-and-manage-hundreds-of-lora-adapters-with-sagemaker-efficient-multi-adapter-inference/) I can see that quantization has been supported [since 0.6.4](https://github.com/vllm-project/vllm/releases/tag/v0....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s", "OPTION_LOAD_FORMAT": "bitsandbytes", } create_model_response = sm_client.create_model( ModelName = model_name, ExecutionRoleArn = role, PrimaryContainer = { "Image": inference_image_uri, "Environment": env, }, ) ``...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
