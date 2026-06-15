# vllm-project/vllm#36099: [Bug]: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#36099](https://github.com/vllm-project/vllm/issues/36099) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory

### Issue 正文摘录

### Your current environment ```text (.venv) btcc@spark-4ddc:~/my-project$ python collect_env.py /home/btcc/my-project/.venv/lib/python3.12/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cpu Is debug build : False CUDA used to build PyTorch : Could not collect ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jan 8 2026, 11:30:50) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-1015-nvidia-aarch64-with-glibc2.39 ============================== CUDA / GPU Info...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Bug]: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory bug ### Your current environment ```text (.venv) btcc@spark-4ddc:~/my-project$ python collect_env.py /home/btcc/my-project/....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory bug ### Your current environment ```text (.venv) btcc@spark-4ddc:~/my-project$ python collect_env.py /home/btcc/my-project/....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: or you. import pynvml # type: ignore[import] Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti==13.0.85...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti ecv afp wfxt 型号名称： Cortex-A725 型号： 1 每个核的线程数： 1 每个座的核数： 10 座：

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
