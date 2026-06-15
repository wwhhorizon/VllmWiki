# vllm-project/vllm#3617: [Bug]: ValueError: bytes must be in range(0, 256)

| 字段 | 值 |
| --- | --- |
| Issue | [#3617](https://github.com/vllm-project/vllm/issues/3617) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: bytes must be in range(0, 256)

### Issue 正文摘录

### Your current environment ```text root@3b4826375ab0:/workspace# python collect_env.py Collecting environment information... PyTorch version: 2.1.2 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (ppc64le) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.28.4 Libc version: glibc-2.35 Python version: 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 16:04:32) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.15.0-100-generic-ppc64le-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.91 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB Nvidia driver version: 535.161.07 cuDNN version: Probably one of the following: /usr/local/cuda-12.2/targets/ppc64le-linux/lib/libcudnn.so.8 /usr/local/cuda-12.2/targets/ppc64le-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-12.2/targets/ppc64le-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-12.2/targets/ppc64le-linux/lib/libcudnn_cnn_infer.so.8 /usr/local/cuda-12.2/targets/p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ace# python collect_env.py Collecting environment information... PyTorch version: 2.1.2 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (ppc64le) GCC version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment information... PyTorch version: 2.1.2 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (ppc64le) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rams(temperature=0.8, top_p=0.95) llm = LLM( model="./models", dtype="float16", tensor_parallel_size=4, enforce_eager=False, trust_remote_code=True, load_format='safetensors' ) outputs = llm.generate(prompts, sampling_p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: @3b4826375ab0:/workspace# python collect_env.py Collecting environment information... PyTorch version: 2.1.2 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s of relevant libraries: [pip3] numpy==1.24.3 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] cudatoolkit 11.8.0 hedcfb66_13 conda-forge [conda] libmagma 2.7.2 he288b6c_2 conda-forge [conda] libmagma_sparse 2.7.2

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
