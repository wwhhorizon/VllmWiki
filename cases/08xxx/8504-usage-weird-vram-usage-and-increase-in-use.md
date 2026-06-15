# vllm-project/vllm#8504: [Usage]: Weird vram usage and increase in use

| 字段 | 值 |
| --- | --- |
| Issue | [#8504](https://github.com/vllm-project/vllm/issues/8504) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;sampling;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Weird vram usage and increase in use

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0+cu121 GPU models and configuration: GPU 0: Tesla T4 GPU 1: Tesla T4 GPU 2: Tesla T4 GPU 3: Tesla T4 Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvidia-cuda-nvrtc-cu12==12.1.105 [pip3] nvidia-cuda-runtime-cu12==12.1.105 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.0.2.54 [pip3] nvidia-curand-cu12==10.3.2.106 [pip3] nvidia-cusolver-cu12==11.4.5.107 [pip3] nvidia-cusparse-cu12==12.1.0.106 [pip3] nvidia-ml-py==12.560.30 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] nvidia-nvjitlink-cu12==12.6.68 [pip3] nvidia-nvtx-cu12==12.1.105 [pip3] pyzmq==26.2.0 [pip3] torch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.2 [pip3] triton==3.0.0 ``` ### How would you like to use vllm First of all I wanted to thanks all of the contributors of this library, you are doing an amazing job. I'm currently running an inference server using Vllm 0.6.0 and I cannot get my head around how the Vram is used, and I think that I don't understand some parameters of the library. With my current setup (4 * nvidia T4@16Go Vram) I have around 64...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: and increase in use usage ### Your current environment ```text PyTorch version: 2.4.0+cu121 GPU models and configuration: GPU 0: Tesla T4 GPU 1: Tesla T4 GPU 2: Tesla T4 GPU 3: Tesla T4 Versions of relevant libraries: [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### Your current environment ```text PyTorch version: 2.4.0+cu121 GPU models and configuration: GPU 0: Tesla T4 GPU 1: Tesla T4 GPU 2: Tesla T4 GPU 3: Tesla T4 Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvidia-cuda-nvrtc-cu12==12.1.105 [pip3] nvidia-cuda-runtime-cu12==12.1.105 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: "model":"Meta-Llama-3.1-8B-Instruct", "tensor_parallel_size":4, "dtype":"float16", "max_model_len":29000, "gpu_memory_utilization":0.95 } ``` ```python with open("engine_config.json") as f: engine_args = json.load(f) en...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ---------+ ``` vram after question: (it's just a dummy question to start evaluating his knowledge of AWS) "In aws how can i creae multiple micro service that are able to communicate with each other ?" ```text +---------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
