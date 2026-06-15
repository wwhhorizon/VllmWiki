# vllm-project/vllm#30165: [Bug]: GLM-4.6-AWQ model outputs garbled text on vllm/vllm-openai:v0.10.2-x86_64

| 字段 | 值 |
| --- | --- |
| Issue | [#30165](https://github.com/vllm-project/vllm/issues/30165) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.6-AWQ model outputs garbled text on vllm/vllm-openai:v0.10.2-x86_64

### Issue 正文摘录

### Your current environment GPU: H800 Docker image: vllm/vllm-openai:v0.10.2-x86_64 with vllm=0.10.2, transformers=4.56.1, torch=2.8.0+cu128 and autoawq=0.2.9 (manually installed) ### 🐛 Describe the bug Hello VLLM developers, I am using your vllm/vllm-openai:v0.10.2-x86_64 Docker image, deployed on a Linux server with 6 H800 GPUs. The model I am trying to serve is: [GLM-4.6-AWQ](https://modelscope.cn/models/tclf90/GLM-4.6-AWQ), the model's config.json file contains following content: ``` "quantization_config": { "quant_method": "awq_marlin", "bits": 4, "group_size": 128, "version": "gemm", "zero_point": true, "modules_to_not_convert": ["embed_tokens", "shared_experts", "shared_head", "lm_head"] } ``` After entering the Docker container, I ran the following command:： ``` vllm serve \ /data \ --served-model-name glm46 \ --enable-auto-tool-choice \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --swap-space 16 \ --max-num-seqs 32 \ --max-model-len 8192 \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 4 \ --trust-remote-code \ --host 0.0.0.0 \ --port 8000 ``` The server starts successfully: (Apologies for the photo format, as our computers are offline.) However, the out...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: openai:v0.10.2-x86_64 bug;stale ### Your current environment GPU: H800 Docker image: vllm/vllm-openai:v0.10.2-x86_64 with vllm=0.10.2, transformers=4.56.1, torch=2.8.0+cu128 and autoawq=0.2.9 (manually installed) ### 🐛...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -4.6-AWQ), the model's config.json file contains following content: ``` "quantization_config": { "quant_method": "awq_marlin", "bits": 4, "group_size": 128, "version": "gemm", "zero_point": true, "modules_to_not_convert...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GLM-4.6-AWQ model outputs garbled text on vllm/vllm-openai:v0.10.2-x86_64 bug;stale ### Your current environment GPU: H800 Docker image: vllm/vllm-openai:v0.10.2-x86_64 with vllm=0.10.2, transformers=4.56.1, torc...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: od": "awq_marlin", "bits": 4, "group_size": 128, "version": "gemm", "zero_point": true, "modules_to_not_convert": ["embed_tokens", "shared_experts", "shared_head", "lm_head"] } ``` After entering the Docker container, I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ! s ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
