# vllm-project/vllm#11630: [Bug]:  Dimension mismatch error will occur during batch inference when processing image embeddings with minicpmv

| 字段 | 值 |
| --- | --- |
| Issue | [#11630](https://github.com/vllm-project/vllm/issues/11630) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Dimension mismatch error will occur during batch inference when processing image embeddings with minicpmv

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (conda-forge gcc 14.2.0-1) 14.2.0 Clang version: Could not collect CMake version: version 3.26.4 Libc version: glibc-2.17 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.105.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version: 545.23.08 cuDNN version: Probably one of the following: /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.9.1 /usr/local...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: r current environment ``` Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: minicpmv bug ### Your current environment ``` Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Dimension mismatch error will occur during batch inference when processing image embeddings with minicpmv bug ### Your current environment ``` Collecting environment information... PyTorch version: 2.5.1+cu124 Is...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _model_len=2048, gpu_memory_utilization=0.9, max_num_seqs=5, dtype="auto", ) messages = [{"role": "user", "content": f"( ./ )\n{question}"}] prompt = tokenizer.apply_chat_template( messages, tokenize=False, add_generati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .1.5 [pip3] torchvision==0.20.1+cu124 [pip3] transformers==4.46.3 [pip3] triton==3.1.0 [conda] blas 1.0 mkl [conda] cuda-cudart 11.8.89 0 nvidia [conda] cuda-cupti 11.8.87

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
