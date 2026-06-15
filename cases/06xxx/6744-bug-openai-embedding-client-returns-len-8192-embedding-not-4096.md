# vllm-project/vllm#6744: [Bug]: openai_embedding_client returns len 8192 embedding not 4096

| 字段 | 值 |
| --- | --- |
| Issue | [#6744](https://github.com/vllm-project/vllm/issues/6744) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: openai_embedding_client returns len 8192 embedding not 4096

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] onnx==1.14.1 [pip3] onnxruntime==1.18.1 [pip3] sentence-transformers==3.0.1 [pip3] torch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.42.4 [pip3] triton==2.3.1 vLLM Version: 0.5.3 ### 🐛 Describe the bug My vllm version is the latest version, v0.5.3 post1 first i launch a embedding server as below `python3 -m vllm.entrypoints.openai.api_server --model Salesforce/SFR-Embedding-Mistral --dtype bfloat16 --enforce-eager --max-model-len 8192` Salesforce/SFR-Embedding-Mistral is an embedding model which has the same architecture with intfloat/e5-mistral then i use https://github.com/vllm-project/vllm/blob/main/examples/openai_embedding_client.py to test online embedding result. And returns a tensor of 8192 le...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: entrypoints.openai.api_server --model Salesforce/SFR-Embedding-Mistral --dtype bfloat16 --enforce-eager --max-model-len 8192` Salesforce/SFR-Embedding-Mistral is an embedding model which has the same architecture with i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ding not 4096 bug ### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 Nvi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: : N/A Is XNNPACK available: True Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] onnx==1.14.1 [pip3] onnxruntime==1.18.1 [pip3] sentence...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: A40 Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 Nvidia driver version: 53...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
