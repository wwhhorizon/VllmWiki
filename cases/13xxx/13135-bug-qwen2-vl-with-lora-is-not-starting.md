# vllm-project/vllm#13135: [Bug]: qwen2-vl with lora is not starting

| 字段 | 值 |
| --- | --- |
| Issue | [#13135](https://github.com/vllm-project/vllm/issues/13135) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen2-vl with lora is not starting

### Issue 正文摘录

### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 10.2.1 20200825 (Alibaba 10.2.1-3 2.17) Clang version: Could not collect CMake version: version 3.26.4 Libc version: glibc-2.32 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.9.151-015.ali3000.alios7.x86_64-x86_64-with-glibc2.32 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 Nvidia driver version: 535.161.08 cuDNN version: Probably one of the following: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_ops_train...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 2-vl with lora is not starting bug ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Serv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: qwen2-vl with lora is not starting bug ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: lm.entrypoints.openai.api_server --model /workspace/Qwen2-VL-2B-Instruct-FP8-Dynamic --port 9122 --trust-remote-code --enforce-eager --max-num-seqs 5 --max-model-len 4096 --gpu-memory-utilization 0.6 --enable-lora --max...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
