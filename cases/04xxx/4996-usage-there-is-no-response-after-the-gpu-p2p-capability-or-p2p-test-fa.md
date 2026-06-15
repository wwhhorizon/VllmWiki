# vllm-project/vllm#4996: [Usage]: There is no response after the "GPU P2P capability or P2P test failed" warning is displayed. What can I do?

| 字段 | 值 |
| --- | --- |
| Issue | [#4996](https://github.com/vllm-project/vllm/issues/4996) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: There is no response after the "GPU P2P capability or P2P test failed" warning is displayed. What can I do?

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 16.04.7 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~16.04) 7.5.0 Clang version: Could not collect CMake version: version 3.27.7 Libc version: glibc-2.23 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.4.0-210-generic-x86_64-with-glibc2.23 Is CUDA available: True CUDA runtime version: 11.7.64 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Quadro RTX 6000 GPU 1: Quadro RTX 6000 GPU 2: Quadro RTX 6000 GPU 3: Quadro RTX 6000 GPU 4: Quadro RTX 6000 GPU 5: Quadro RTX 6000 GPU 6: Quadro RTX 6000 GPU 7: Quadro RTX 6000 Nvidia driver version: 550.67 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.1.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.1.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.1.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.1.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.1.1 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.1.1 /usr/lib/x86_64-linux-gnu/libcudnn_ops_trai...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: isplayed. What can I do? usage ### Your current environment ``` PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 16.04.7 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Usage]: There is no response after the "GPU P2P capability or P2P test failed" warning is displayed. What can I do? usage ### Your current environment ``` PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 11.7.64 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Quadro RTX 6000 GPU 1: Quadro RTX 6000 GPU 2: Quadro RTX 6000 GPU 3: Quadro RTX 6000 GPU 4: Quadro RTX 6000 GPU 5:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: hat --model llm_models/Qwen1.5-4B-Chat --trust-remote-code --port 9741 --dtype float16 --tensor-parallel-size 2 --gpu-memory-utilization 0.55 --max-model-len 5120 --enable-prefix-caching --enforce-eager` to test the rea...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 8 [pip3] torchaudio==2.1.2+cu118 [pip3] torchvision==0.16.2+cu118 [pip3] triton==2.1.0 [conda] numpy 1.24.4 pypi_0 pypi [conda] torch 2.1.2+cu118 pypi_0 pypi [conda] torchaudio 2.1.2+cu118

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
